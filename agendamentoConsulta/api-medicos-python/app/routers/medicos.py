from fastapi import APIRouter, Depends, HTTPException
from .api_client import AgendamentosClient
from . import schemas

router = APIRouter(prefix="/medicos", tags=["Médicos"])

@router.get("/{medico_id}/disponibilidade")
async def verificar_disponibilidade(
    medico_id: int,
    data_hora: str,
    db: Session = Depends(database.get_db)
):
    """Endpoint usado pela API Agendamentos"""
    # Verifica se médico existe
    medico = db.query(models.Medico).get(medico_id)
    if not medico:
        raise HTTPException(status_code=404, detail="Médico não encontrado")
    
    # Aqui você pode adicionar outras regras específicas
    return {"disponivel": True}

@router.post("/{medico_id}/agendar")
async def agendar_consulta(
    medico_id: int,
    agendamento: schemas.AgendamentoRequest,
    db: Session = Depends(database.get_db)
):
    """Exemplo de uso da API Agendamentos"""
    # 1. Verifica disponibilidade
    disponivel = await AgendamentosClient.verificar_disponibilidade(
        medico_id, 
        agendamento.data_hora
    )
    
    if not disponivel:
        raise HTTPException(status_code=400, detail="Horário indisponível")
    
    # 2. Cria agendamento
    dados_agendamento = {
        "medico_id": medico_id,
        "paciente_id": agendamento.paciente_id,
        "data_hora": agendamento.data_hora
    }
    
    return await AgendamentosClient.criar_agendamento(dados_agendamento)