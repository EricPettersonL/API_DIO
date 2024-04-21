from pydantic import BaseModel

class SchemaBase(BaseModel):
    class Config:
        extra = "forbid"
        from_attributes = True