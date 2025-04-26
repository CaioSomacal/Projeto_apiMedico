from fastapi import FastAPI
from app.models.medico import Base  # ← Import absoluto
from app.configs.database import engine
from app.routers.medicos import router as medicos_router

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Médicos",
    description="Sistema de Agendamento Médico",
    version="1.0.0"
)

app.include_router(medicos_router)

@app.get("/")
async def root():
    return {"message": "Bem-vindo à API de Médicos"}