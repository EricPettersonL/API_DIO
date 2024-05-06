from typing import Annotated
from datetime import datetime
from pydantic import UUID4, BaseModel, Field

class SchemaBase(BaseModel):
    class Config:
        extra = "forbid"
        from_attributes = True
        
class OutSchema(SchemaBase):
    id: Annotated[UUID4, Field(description="ID do registro")] 
    created_at: Annotated[datetime, Field(description="Data de criação do registro")] 