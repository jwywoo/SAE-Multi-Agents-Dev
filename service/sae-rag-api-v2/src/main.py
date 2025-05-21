from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from functools import lru_cache

from stock_generation.router import router as stock_router

app = FastAPI(title="SAE LangGraph MVP RAG API", version="1.0.0")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stock_router)


@app.get("/")
def root():
    return {"message": "Welcome to Project SAE LangGraph RAG API Server"}
