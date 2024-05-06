from typing import Annotated
from pydantic import UUID4, Field
from API.contrib.schema_base import SchemaBase

class Categoria(SchemaBase):
    nome: Annotated[str, Field(description="Nome da categoria", example=["Scale"], min_length=3, max_length=10)]
    
class CategoriaOut(Categoria):
    id: Annotated[UUID4, Field(description="ID da categoria")]