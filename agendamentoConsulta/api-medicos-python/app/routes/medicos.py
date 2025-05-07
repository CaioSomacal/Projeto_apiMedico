from fastapi import APIRouter, Depends, HTTPException, Request
from app.services.medico_service import MedicoService
from app.models.schemas import MedicoCreate, MedicoResponse
from app.cache.redis_cache import cache
from typing import List

router = APIRouter()

@router.post("/", response_model=MedicoResponse, status_code=201)
async def create_medico(
    medico: MedicoCreate,
    service: MedicoService = Depends()
):
    return await service.create_medico(medico)

@router.get("/{medico_id}", response_model=MedicoResponse)
@cache(key_prefix="medico", ttl=300)
async def get_medico(
    request: Request,
    medico_id: int,
    service: MedicoService = Depends()
):
    return await service.get_medico(medico_id)

@router.get("/", response_model=List[MedicoResponse])
@cache(key_prefix="medicos_list", ttl=120)
async def get_all_medicos(
    request: Request,
    service: MedicoService = Depends()
):
    return await service.get_all_medicos()

@router.get("/crm/{crm}", response_model=MedicoResponse)
@cache(key_prefix="medico_crm", ttl=300)
async def get_medico_by_crm(
    request: Request,
    crm: str,
    service: MedicoService = Depends()
):
    return await service.get_medico_by_crm(crm)
