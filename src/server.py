from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.rotas import rotas_produto,rotas_usuario

app = FastAPI()

# CORS
app.add_middleware(CORSMiddleware,
    allow_origins=['http://127.0.0.1:8000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROTAS PRODUTO
app.include_router(rotas_produto.rotas)
# ROTAS USUARIOS
app.include_router(rotas_usuario.rotas)        
