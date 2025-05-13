from fastapi import FastAPI
from routers import items
from database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Grocery API")


app.include_router(items.router, prefix="/items", tags=["Items"])

