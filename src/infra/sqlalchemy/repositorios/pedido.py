from sqlalchemy.orm import Session
from src.infra.sqlalchemy.schemas import schemas
from src.infra.sqlalchemy.models import modelos

class RepositorioPedido():
    def __init__(self,db:Session):
        self.db = db

    def CriarPedido(self,pedido:schemas.Pedido):
        novo_pedido = modelos.Pedido(
            quantidade= pedido.quantidade,
            entrega= pedido.entrega,
            endereco= pedido.endereco,
            observacao= pedido.observacao
        )

        self.db.add(novo_pedido)
        self.db.commit()
        self.db.refresh(novo_pedido)
        return novo_pedido

    def ListarPedidos(self):
        return self.db.query(schemas.Pedido).all()


    def removerPedido(self,pedido_id=int):
       pass