from src.models.usuario_model import UsuarioModel


class UsuarioService:
    # _usuarios: list[UsuarioModel] = []

    @classmethod
    def criar(cls, usuario: UsuarioModel) -> UsuarioModel:
        cls._usuarios.append(usuario)
        return usuario
