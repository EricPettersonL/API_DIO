from datetime import datetime

from API.contrib.models_base import BaseModel
from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class AtletaModel(BaseModel):
    __tablename__ = "atleta"
    
    pk_id: Mapped[int] = mapped_column(Integer,primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11),unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(10), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    categoria: Mapped["CategoriaModel"] = relationship(back_populates="atleta")
    categoria_id: Mapped[int] = mapped_column(Integer, ForeignKey("categorias.pk_id"))
    centro_treinamento: Mapped["CentroTreinamentoModel"] = relationship(back_populates="atleta")
    centro_treinamento_id: Mapped[int] = mapped_column(Integer, ForeignKey("centros_treinamento.pk_id"))