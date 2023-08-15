from sqlalchemy.orm import Session
from src.infra.sqlalchemy.schemas import schemas
from src.infra.sqlalchemy.models import modelos
from sqlalchemy import delete, update , select

class repositorioProduto():
    def __init__(self,db:Session):
        self.db = db

    def criar(self,produto:schemas.Produto):
        db_produto = modelos.Produto(
            nome = produto.nome,
            preco = produto.preco,
            detalhamento = produto.detalhamento,
            disponivel = produto.disponivel,
            usuario_id = produto.usuario_id
        )

        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto
    
    def listar(self):
        return self.db.query(modelos.Produto).all()

    def RemoverProduto(self,prod_id:int):
      print(prod_id)
      delete_produto = delete(modelos.Produto).where(modelos.Produto.id == prod_id)
      self.db.execute(delete_produto)
      self.db.commit()
      return True
    
    def editar(self, id: int , produto:schemas.Produto):
        smt = (
            update(modelos.Produto).
            where(modelos.Produto.id == id).values(
            nome = produto.nome,
            preco = produto.preco,
            detalhamento = produto.detalhamento,
            disponivel = produto.disponivel
            )
        )
        self.db.execute(smt)
        self.db.commit()

    def BuscaPorID(self, id:int):
        consulta = select(modelos.Produto).where(modelos.Produto.id == id)
        produto = self.db.execute(consulta).first()
        return produto