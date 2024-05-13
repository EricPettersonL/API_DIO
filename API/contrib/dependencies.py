from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from API.configs.database import get_async_session

DatabaseDependency = Annotated[AsyncSession, Depends(get_async_session)]
