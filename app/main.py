from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, users, items
from app.db.session import engine
from app.models import base

base.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API REST Python",
    description="REST API com FastAPI, PostgreSQL e JWT",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(items.router, prefix="/items", tags=["Items"])


@app.get("/", tags=["Root"])
def root():
    return {"message": "API REST Python - FastAPI", "docs": "/docs"}
