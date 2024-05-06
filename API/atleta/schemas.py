from typing import Annotated
from pydantic import Field, PositiveFloat

from API.contrib.schema_base import OutSchema, SchemaBase

class Atleta(SchemaBase):
    nome: Annotated[str, Field(description="Nome do atleta", example=["João", "Maria"], min_length=3, max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta", example=["12345678900", "12345678901"], min_length=11, max_length=11)]
    idade: Annotated[int, Field(description="Idade do atleta", example=[20, 21], gt=0)]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", example=[70.5, 80.0], gt=0)]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta", example=[1.70, 1.80], gt=0)]
    sexo: Annotated[str, Field(description="Sexo do atleta", example=["Masculino", "Feminino"], min_length=10, max_length=10)]


class AtletaIn(Atleta):
    pass    
class AtletaOut(Atleta, OutSchema):
    pass