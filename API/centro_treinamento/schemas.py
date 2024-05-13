from typing import Annotated

from pydantic import UUID4, Field

from API.contrib.schema_base import SchemaBase


class CentroTreinamento(SchemaBase):
    nome: Annotated[str, Field(description="Nome do centro de treinamento ", example="CT King", min_length=1, max_length=20)]
    endereco: Annotated[str, Field(description="Endereço do centro de treinamento ", example="Rua dos Bobos, 0", min_length=1, max_length=60)]
    proprietario: Annotated[str, Field(description="Proprietario do centro de treinamento ", example="Marcos", min_length=1, max_length=30)]
    
class CentroTreinamentoAtleta(SchemaBase):
    nome: Annotated[str, Field(description="Nome do centro de treinamento ", example="CT King", min_length=1, max_length=20)]
    
class CentroTreinamentoOut(CentroTreinamento):
    id: Annotated[UUID4, Field(description="ID do centro de treinamento")]