from sqlalchemy.orm import Session
from ..models.medico import Medico
from ..schemas.medico import MedicoCreate

class MedicoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100):
        return self.db.query(Medico).offset(skip).limit(limit).all()

    def get_by_id(self, medico_id: int):
        return self.db.query(Medico).filter(Medico.id == medico_id).first()

    def get_by_crm(self, crm: str):
        return self.db.query(Medico).filter(Medico.crm == crm).first()

    def create(self, medico: MedicoCreate):
        db_medico = Medico(**medico.dict())
        self.db.add(db_medico)
        self.db.commit()
        self.db.refresh(db_medico)
        return db_medico

    def delete(self, medico_id: int):
        medico = self.db.query(Medico).filter(Medico.id == medico_id).first()
        if medico:
            self.db.delete(medico)
            self.db.commit()
        return medico