from fastapi import APIRouter

from API.atleta.controller import router as atleta_router
from API.categoria.controller import router as categoria_router
from API.centro_treinamento.controller import \
    router as centro_treinamento_router

api_router = APIRouter()
api_router.include_router(atleta_router, prefix="/atleta", tags=["Atleta"])
api_router.include_router(categoria_router, prefix="/categoria", tags=["Categoria"])
api_router.include_router(centro_treinamento_router, prefix="/centro_treinamento", tags=["Centro de Treinamento"])
