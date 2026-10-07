from fastapi import APIRouter, status

from src.models.usuario_model import UsuarioModel
from src.services.usuario_service import UsuarioService

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def criar_usuario(usuario: UsuarioModel) -> UsuarioModel:
    return UsuarioService.criar(usuario)
