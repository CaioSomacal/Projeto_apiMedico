from sqlalchemy.orm import Session
from app.database.models import MedicoDB
from app.models.schemas import MedicoCreate, MedicoResponse
from app.database import get_db
from fastapi import Depends, HTTPException
from typing import List

class MedicoRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
    
    def create(self, medico: MedicoCreate) -> MedicoResponse:
        try:
            db_medico = MedicoDB(**medico.dict())
            self.db.add(db_medico)
            self.db.commit()
            self.db.refresh(db_medico)
            return MedicoResponse.from_orm(db_medico)
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=400, detail=f"Erro ao criar médico: {str(e)}")
    
    def get_by_id(self, medico_id: int) -> MedicoResponse:
        medico = self.db.query(MedicoDB).filter(MedicoDB.id == medico_id).first()
        if not medico:
            raise HTTPException(status_code=404, detail="Médico não encontrado")
        return MedicoResponse.from_orm(medico)
    
    def get_all(self) -> List[MedicoResponse]:
        medicos = self.db.query(MedicoDB).all()
        return [MedicoResponse.from_orm(m) for m in medicos]
    
    def get_by_crm(self, crm: str) -> MedicoResponse:
        medico = self.db.query(MedicoDB).filter(MedicoDB.crm == crm).first()
        if not medico:
            raise HTTPException(status_code=404, detail="Médico não encontrado")
        return MedicoResponse.from_orm(medico)
