from uuid import uuid4
from fastapi import APIRouter, HTTPException, status, Body
from pydantic import UUID4
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from API.centro_treinamento.models import CentroTreinamentoModel
from API.centro_treinamento.schemas import CentroTreinamento, CentroTreinamentoOut
from API.contrib.dependencies import DatabaseDependency

router = APIRouter()

@router.post(path="/", summary="Cadastra um novo centro de treinamento", status_code=status.HTTP_201_CREATED, response_model=CentroTreinamentoOut)
async def post(db_session: DatabaseDependency, centers_treinamento_in: CentroTreinamento = Body(...)) -> CentroTreinamentoOut:
    try:
        centro_treinamento_out = CentroTreinamentoOut(id=uuid4(), **centers_treinamento_in.model_dump())
        centro_treinamento_model = CentroTreinamentoModel(**centro_treinamento_out.model_dump())
        
        db_session.add(centro_treinamento_model)
        await db_session.commit()
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_303_SEE_OTHER, detail=f"A centro de treinamento {centers_treinamento_in.nome} já foi inserido")    



@router.get(path="/", summary="Retorna todos os centros de treinamento", response_model=list[CentroTreinamentoOut], status_code=status.HTTP_200_OK)
async def query(db_session: DatabaseDependency) -> list[CentroTreinamentoOut]:
    centros_treinamento: list[CentroTreinamentoOut] = (await db_session.execute(select(CentroTreinamentoModel))).scalars().all()
    
    return centros_treinamento

@router.get(path="/{id}", summary="Retorna um centro de treinamento pelo ID", response_model=CentroTreinamentoOut, status_code=status.HTTP_200_OK)
async def query_by_id(db_session: DatabaseDependency, id: UUID4) -> CentroTreinamentoOut:
    centro_treinamento_id: CentroTreinamentoModel = (await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id))).scalars().first()
    
    if not centro_treinamento_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Centro de treinamento não encontrado no ID {id}")
    
    return centro_treinamento_id