from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MedicoBase(BaseModel):
    nome: str
    especialidade: str
    crm: str
    telefone: Optional[str] = None

class MedicoCreate(MedicoBase):
    pass

class MedicoResponse(MedicoBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
