from fastapi import APIRouter, Depends
from src.infra.sqlalchemy.schemas import schemas
from sqlalchemy.orm import Session 
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db

rotas = APIRouter()

@rotas.post('/usuario')
def CriarUser(user:schemas.Usuario,db:Session=Depends(get_db)):
    newUser = RepositorioUsuario(db).NovoUsuario(user)
    return newUser

@rotas.get('/usuario')
def PegarProduto(db:Session=Depends(get_db)):
    return  RepositorioUsuario(db).ListarUser()

@rotas.delete('/usuario/{user_id}')
def apagarUser(user_id:int,db:Session=Depends(get_db)):
   return RepositorioUsuario(db).Remover(user_id)
