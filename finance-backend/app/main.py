from fastapi import FastAPI
from fastapi import Depends
from app.dependencies.db import get_db
from app.db.database import Base, engine
from app.routes import auth, transaction, analytics
from app.db import models

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/",tags=["System"])
def root():
    return {"message":"Finance Backend Running"}

@app.get("/test-db",tags=["System"])
def test_db(db=Depends(get_db)):
    return {"message":"DB Connected"}

app.include_router(auth.router)
app.include_router(transaction.router)
app.include_router(analytics.router)