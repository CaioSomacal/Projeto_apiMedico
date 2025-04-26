from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class MedicoBase(BaseModel):
    nome: str
    crm: str
    especialidade: str

class MedicoCreate(MedicoBase):
    telefone: Optional[str] = None
    email: Optional[EmailStr] = None

class Medico(MedicoBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True