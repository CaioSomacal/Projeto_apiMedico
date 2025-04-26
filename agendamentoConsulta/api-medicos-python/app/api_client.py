import httpx
import os
from fastapi import HTTPException

AGENDAMENTOS_API_URL = os.getenv("AGENDAMENTOS_API_URL", "http://localhost:8003")

class AgendamentosClient:
    @staticmethod
    async def verificar_disponibilidade(medico_id: int, data_hora: str):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{AGENDAMENTOS_API_URL}/agendamentos/disponibilidade",
                    params={"medico_id": medico_id, "data_hora": data_hora}
                )
                response.raise_for_status()
                return response.json()["disponivel"]
        except httpx.HTTPStatusError as e:
            raise HTTPException(
                status_code=502,
                detail=f"Erro ao verificar disponibilidade: {e.response.text}"
            )

    @staticmethod
    async def criar_agendamento(dados: dict):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{AGENDAMENTOS_API_URL}/agendamentos",
                    json=dados
                )
                response.raise_for_status()
                return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(
                status_code=502,
                detail=f"Erro ao criar agendamento: {e.response.text}"
            )