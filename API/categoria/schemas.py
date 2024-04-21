from typing import Annotated
from pydantic import Field
from API.contrib.schema_base import SchemaBase

class Categoria(SchemaBase):
    nome: Annotated[str, Field(description="Nome da categoria", example=["Scale"], min_length=3, max_length=10)]