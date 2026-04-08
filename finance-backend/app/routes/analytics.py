from fastapi import APIRouter, Depends
from sqlalchemy import func
from app.db.database import SessionLocal
from app.db.models import Transaction
from sqlalchemy.orm import Session
from app.dependencies.roles import authorize
from app.dependencies.db import get_db

router = APIRouter(tags=["Analytics"])


@router.get("/analytics/summary")
def get_summary(
    db: Session = Depends(get_db),
    user = Depends(authorize(["admin", "analyst"]))
):
    db = SessionLocal()

    total_income = db.query(func.sum(Transaction.amount))\
        .filter(Transaction.type == "income").scalar() or 0

    total_expense = db.query(func.sum(Transaction.amount))\
        .filter(Transaction.type == "expense").scalar() or 0

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": total_income - total_expense
    }
    
@router.get("/analytics/category")
def category_breakdown(
    db: Session = Depends(get_db),
    user = Depends(authorize(["admin", "analyst"]))
):
    db = SessionLocal()

    data = db.query(
        Transaction.category,
        func.sum(Transaction.amount)
    ).group_by(Transaction.category).all()

    return [{"category": c, "total": t} for c, t in data]

@router.get("/analytics/recent")
def recent_transactions(
    db: Session = Depends(get_db),
    user = Depends(authorize(["admin", "analyst", "viewer"]))
):
    db = SessionLocal()

    return db.query(Transaction)\
        .order_by(Transaction.id.desc())\
        .limit(5)\
        .all()
        
@router.get("/analytics/monthly")
def monthly_trends(
    db: Session = Depends(get_db),
    user = Depends(authorize(["admin", "analyst"]))
):
    db = SessionLocal()

    data = db.query(
        func.strftime("%Y-%m", Transaction.date),
        func.sum(Transaction.amount)
    ).group_by(func.strftime("%Y-%m", Transaction.date)).all()

    return [{"month": m, "total": t} for m, t in data]