from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from API.categoria.models import CategoriaModel
from API.categoria.schemas import Categoria, CategoriaOut
from API.contrib.dependencies import DatabaseDependency

router = APIRouter()

@router.post(path="/", summary="Cadastra uma nova categoria", status_code=status.HTTP_201_CREATED, response_model=CategoriaOut)
async def post(db_session: DatabaseDependency, categoria_in: Categoria = Body(...)) -> CategoriaOut:
    try:
        categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
        categoria_model = CategoriaModel(**categoria_out.model_dump())
        
        db_session.add(categoria_model)
        await db_session.commit()
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_303_SEE_OTHER, detail=f"A categoria {categoria_in.nome} já foi inserida")    


@router.get(path="/", summary="Retorna todas as categorias", response_model=list[CategoriaOut], status_code=status.HTTP_200_OK)
async def query(db_session: DatabaseDependency) -> list[CategoriaOut]:
    categorias: list[CategoriaModel] = (await db_session.execute(select(CategoriaModel))).scalars().all()
    
    return categorias

@router.get(path="/{id}", summary="Retorna uma categoria pelo ID", response_model=CategoriaOut, status_code=status.HTTP_200_OK)
async def query_by_id(db_session: DatabaseDependency, id: UUID4) -> CategoriaOut:
    categoria: CategoriaModel = (await db_session.execute(select(CategoriaModel).filter_by(id=id))).scalars().first()
    
    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Categoria não encontrada no ID {id}")
    
    return categoria
    