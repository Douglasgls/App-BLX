from pydantic import BaseModel
from typing import List,Optional

class Pedido(BaseModel):
    id:Optional[str] = None
    quantidade:int
    entrega:bool = True
    endereco:str 
    observacao: Optional[str] = None

class Usuario(BaseModel):
    id: Optional[int] = None
    nome:str
    telefone:str

class Produto(BaseModel):
    id:Optional[int] = None
    nome:str
    preco: float
    disponivel : bool =False
    detalhamento:str = None
    usuario_id: int
    usuario: Optional[Usuario] = None