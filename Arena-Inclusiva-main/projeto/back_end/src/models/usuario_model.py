from pydantic import BaseModel, Field


class UsuarioModel(BaseModel):
    nome: str = Field(min_length=1, max_length=120)
    idade: int = Field(ge=0, le=130)
    deficiencia: str = Field(min_length=1, max_length=120)
