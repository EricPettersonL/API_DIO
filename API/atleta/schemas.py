from typing import Annotated, Optional

from pydantic import Field, PositiveFloat

from API.categoria.schemas import Categoria
from API.centro_treinamento.schemas import CentroTreinamentoAtleta
from API.contrib.schema_base import OutSchema, SchemaBase


class Atleta(SchemaBase):
    nome: Annotated[str, Field(description="Nome do atleta", example="Maria", min_length=3, max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta", example="12345678900", min_length=11, max_length=11)]
    idade: Annotated[int, Field(description="Idade do atleta", example= 21, gt=0)]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", example=80.0, gt=0)]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta", example=1.80, gt=0)]
    sexo: Annotated[str, Field(description="Sexo do atleta", example= "Feminino", min_length=0, max_length=10)]
    categoria: Annotated[Categoria, Field(description="Categoria do atleta")]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description="Centro de treinamento do atleta")]


class AtletaTeste(SchemaBase):
    nome: Annotated[str, Field(description="Nome do atleta")]
    categoria: Annotated[Categoria, Field(description="Categoria do atleta")]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description="Centro de treinamento do atleta")]
    
class AtletaOutTeste(AtletaTeste, OutSchema):
    pass
    
class AtletaIn(Atleta):
    pass    
class AtletaOut(Atleta, OutSchema):
    pass

class AtletaUpdate(SchemaBase):
    nome: Annotated[Optional[str], Field(None,description="Nome do atleta", example="Maria", min_length=3, max_length=50)]
    idade: Annotated[Optional[int], Field(None,description="Idade do atleta", example= 21)]
    
