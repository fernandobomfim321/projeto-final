from core.usuario.usuario_repository import AlunoRepository
from core.usuario.usuario  import Usuario

class UsuarioService:
    def __init__(self):
        self.repository = AlunoRepository()

    def listar_usuarios(self): 
        return self.repository.listar()
    
    def adicionar_usuario(self, aluno):
        if isinstance(usuario, Usuario):
            return self.repository.adicionar(aluno)
        else:
            return None
        
    def atualizar_aluno(self, usuario):
        if isinstance(usuario,usuario):
            if usuario.id > 0:
                return self.repository.atualizar(usuario)
            else:
                return "ID do usuario é obrigatório para a atualização"
        else:
            return None
    def remover_usuario(self,usuario_id):
        sucesso = self.repository.remover(usuario_id)
        if not sucesso:
            return None
        else:
            return {'id':usuario_id, "removido": True}
        
    def obter_usuario_por_id(self, aluno_id):
        usuario = self.repository.obter_por_id(usuario_id)
        if not usuario:
            return None
        else:
            return usuario 