
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.schemas.schemas import Usuario
from src.infra.sqlalchemy.models import modelos
from sqlalchemy import delete, update

class RepositorioUsuario():
    def __init__(self,db:Session):
       self.db =db

    def NovoUsuario(self, usuario = Usuario ):
        novoUser = modelos.Usuario(
            nome= usuario.nome,
            telefone= usuario.telefone
        )
       
        self.db.add(novoUser)
        self.db.commit()
        self.db.refresh(novoUser)
        return novoUser
        
    def ListarUser(self):
        return self.db.query(modelos.Usuario).all()
    
    def Remover(self,usuario:int):
        user_id = delete(modelos.Usuario).where(modelos.Usuario.id == usuario)
        self.db.execute(user_id)
        self.db.commit()
        return True
       

   
