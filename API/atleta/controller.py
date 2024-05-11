from datetime import datetime
from typing import Optional
from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from fastapi_pagination import Page, Params, paginate
from pydantic import UUID4
from sqlalchemy import select
from API.atleta.models import AtletaModel
from API.atleta.schemas import AtletaIn, AtletaOut, AtletaUpdate
from API.categoria.models import CategoriaModel
from API.centro_treinamento.models import CentroTreinamentoModel
from API.contrib.dependencies import DatabaseDependency

from fastapi import Query


router = APIRouter()

@router.post(path="/", summary="Cadastra um novo atleta", status_code=status.HTTP_201_CREATED)
async def post_atleta(db_session: DatabaseDependency, atleta_in: AtletaIn = Body(...)):
    categoria_nome = atleta_in.categoria.nome
    centro_treinamento_nome = atleta_in.centro_treinamento.nome
    
    
    categoria = (await db_session.execute(select(CategoriaModel).filter_by(nome=categoria_nome))).scalars().first()
    
    if not categoria:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Categoria {categoria_nome} não encontrada")
    
    centro_treinamento = (await db_session.execute(select(CentroTreinamentoModel).filter_by(nome=centro_treinamento_nome))).scalars().first()
    
    if not centro_treinamento:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Centro de treinamento {centro_treinamento_nome} não encontrada")
    
    try:
        atleta_out = AtletaOut(id=uuid4(),created_at=datetime.now(), **atleta_in.model_dump())
        atleta_model = AtletaModel(**atleta_out.model_dump(exclude={"categoria", "centro_treinamento"}))
        atleta_model.categoria_id = categoria.pk_id
        atleta_model.centro_treinamento_id = centro_treinamento.pk_id
        db_session.add(atleta_model)
        await db_session.commit()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Erro ao inserir atleta: {e}")
    



@router.get("/", summary="Retorna todos os atletas", response_model=Page[AtletaOut], status_code=status.HTTP_200_OK)
async def query(
    db_session: DatabaseDependency,
    limit: int = Query(..., gt=0),
    offset: int = Query(..., ge=0),
    nome: Optional[str] = None,
    cpf: Optional[str] = None,
) -> Page[AtletaOut]:
    query = select(AtletaModel)

    if nome:
        query = query.where(AtletaModel.nome == nome)
    if cpf:
        query = query.where(AtletaModel.cpf == cpf)

    atletas = (await db_session.execute(query)).scalars().all()
    
     # Mapear os objetos AtletaModel para dicionários
    atletas_dicts = [
        {
            'id': atleta.id,
            'created_at': atleta.created_at,
            'nome': atleta.nome,
            'categoria': atleta.categoria,
            'centro_treinamento': atleta.centro_treinamento,
            'idade': atleta.idade,
            'cpf': atleta.cpf,
            'peso': atleta.peso,
            'altura': atleta.altura,
            'sexo': atleta.sexo,

        } 
        for atleta in atletas
    ]

    # Criar instâncias de AtletaOut a partir dos dicionários mapeados
    atletas_out = [
        AtletaOut(**atleta_dict) 
        for atleta_dict in atletas_dicts
    ]
    
    paginated_atletas = paginate(atletas_out, Params(limit=limit, offset=offset))
    
    return paginated_atletas





@router.get(path="/{id}", summary="Retorna um atleta pelo ID", response_model=AtletaOut, status_code=status.HTTP_200_OK)
async def query_by_id(db_session: DatabaseDependency, id: UUID4) -> AtletaOut:
    atleta: AtletaOut = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()
    
    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Atleta não encontrada no ID {id}")
    
    return atleta


@router.patch(path="/{id}", summary="Atualiza um atleta pelo ID", response_model=AtletaOut, status_code=status.HTTP_200_OK)
async def update_by_id(db_session: DatabaseDependency, id: UUID4, atleta_up: AtletaUpdate = Body(...)):
    atleta: AtletaOut = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()
    
    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Atleta não encontrada no ID {id}")
    
    atleta_upgrade = atleta_up.model_dump(exclude_unset=True)
    for key, value in atleta_upgrade.items():
        setattr(atleta, key, value)
        
    await db_session.commit()
    await db_session.refresh(atleta)
    
    return atleta

@router.delete(path="/{id}", summary="Deleta um atleta pelo ID", status_code=status.HTTP_204_NO_CONTENT)
async def delete_by_id(db_session: DatabaseDependency, id: UUID4):
    atleta: AtletaOut = (await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()
    
    if not atleta:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Atleta não encontrada no ID {id}")
    
    await db_session.delete(atleta)
    await db_session.commit()