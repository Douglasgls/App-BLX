from fastapi import APIRouter, Depends ,HTTPException
from src.infra.sqlalchemy.repositorios.produto import repositorioProduto
from src.infra.sqlalchemy.schemas import schemas
from sqlalchemy.orm import Session 
from src.infra.sqlalchemy.config.database import get_db



rotas = APIRouter()


@rotas.post('/produto')
def CriarProduto(produto:schemas.Produto, db:Session=Depends(get_db)):
    novo_produto = repositorioProduto(db).criar(produto)
    return novo_produto

@rotas.get('/produto')
def PegarProduto(db:Session=Depends(get_db)):
    return  repositorioProduto(db).listar()


@rotas.delete('/produto/{prod_id}')
def DeleteProduto(prod_id:int,db:Session=Depends(get_db)):
    return repositorioProduto(db).RemoverProduto(prod_id)


@rotas.put('/produto/{id}')
def atualizarProduto(id:int , produto:schemas.Produto, db:Session=Depends(get_db)):
    novo_produto = repositorioProduto(db).editar(id, produto)
    return {'mensangem': 'produto'}

@rotas.get('/produto/{id_prod}')
def buscarPorId(id_prod:int ,db:Session=Depends(get_db)):
    produto_procurado = repositorioProduto(db).BuscaPorID(id_prod)
    if not produto_procurado:
        raise HTTPException(status_code=404,detail=f'id não encontrado {id}')
    return produto_procurado