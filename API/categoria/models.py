from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from API.atleta.models import AtletaModel
from API.contrib.models_base import BaseModel


class CategoriaModel(BaseModel):
    __tablename__ = "categorias"
    
    pk_id: Mapped[int] = mapped_column(Integer,primary_key=True)
    nome: Mapped[str] = mapped_column(String(50),unique=True, nullable=False)
    atleta: Mapped["AtletaModel"] = relationship(back_populates="categoria")