from fastapi import FastAPI
from .routers import pool

app = FastAPI()

app.include_router(pool.router)
