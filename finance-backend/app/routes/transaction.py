from fastapi import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db.models import Transaction
from app.schemas.transaction import TransactionCreate
from app.dependencies.roles import authorize

router = APIRouter(tags=["Transactions"])


@router.post("/transactions")
def create_transaction(
    data: TransactionCreate,
    user=Depends(authorize(["admin", "analyst"]))
):
    db = SessionLocal()

    txn = Transaction(
        amount=data.amount,
        type=data.type,
        category=data.category,
        date=data.date,
        notes=data.notes,
        user_id=user.id
    )

    db.add(txn)
    db.commit()
    db.refresh(txn)

    return txn


@router.get("/transactions")
def get_transactions(
    user=Depends(authorize(["admin", "analyst", "viewer"]))
):
    db = SessionLocal()
    return db.query(Transaction).all()


@router.delete("/transactions/{id}")
def delete_transaction(
    id: int,
    user=Depends(authorize(["admin"]))
):
    db = SessionLocal()
    txn = db.query(Transaction).filter(Transaction.id == id).first()

    if not txn:
        raise HTTPException(status_code=404, detail="Transaction not found")

    db.delete(txn)
    db.commit()

    return {"message": "Transaction deleted"}


@router.put("/transactions/{id}")
def update_transaction(
    id: int,
    data: TransactionCreate,
    user=Depends(authorize(["admin"]))
):
    db = SessionLocal()
    txn = db.query(Transaction).filter(Transaction.id == id).first()

    if not txn:
        raise HTTPException(status_code=404, detail="Transaction not found")

    txn.amount = data.amount
    txn.type = data.type
    txn.category = data.category
    txn.date = data.date
    txn.notes = data.notes

    db.commit()
    db.refresh(txn)

    return txn


@router.get("/transactions/filter")
def filter_transactions(
    type: str = None,
    category: str = None,
    user=Depends(authorize(["admin", "analyst", "viewer"]))
):
    db = SessionLocal()
    query = db.query(Transaction)

    if type:
        query = query.filter(Transaction.type == type)

    if category:
        query = query.filter(Transaction.category == category)

    return query.all()
