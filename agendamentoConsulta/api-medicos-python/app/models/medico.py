from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from ..configs.database import Base

class Medico(Base):
    __tablename__ = "medicos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    crm = Column(String(20), unique=True, nullable=False)
    especialidade = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())