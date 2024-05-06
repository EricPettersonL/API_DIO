from fastapi import APIRouter, status
from API.contrib.dependencies import DatabaseDependency

router = APIRouter()

@router.post(path="/", summary="Cadastra um novo atleta", status_code=status.HTTP_201_CREATED)
async def post_atleta(db_session: DatabaseDependency):
    pass
