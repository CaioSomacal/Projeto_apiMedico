from app.repositories.medico_repository import MedicoRepository
from app.models.schemas import MedicoCreate, MedicoResponse
from fastapi import Depends, HTTPException
from typing import List
from app.cache.redis_cache import cache, invalidate_cache

class MedicoService:
    def __init__(self, repo: MedicoRepository = Depends()):
        self.repo = repo
    
    async def create_medico(self, medico: MedicoCreate) -> MedicoResponse:
        try:
            result = self.repo.create(medico)
            invalidate_cache("medico")
            return result
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    
    async def get_medico(self, medico_id: int) -> MedicoResponse:
        return self.repo.get_by_id(medico_id)
    
    async def get_all_medicos(self) -> List[MedicoResponse]:
        return self.repo.get_all()
    
    async def get_medico_by_crm(self, crm: str) -> MedicoResponse:
        return self.repo.get_by_crm(crm)
