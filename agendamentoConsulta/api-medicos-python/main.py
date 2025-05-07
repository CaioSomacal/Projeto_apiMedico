from fastapi import FastAPI
from app.routes import medicos
from app.database.connection import init_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API de Médicos",
    description="Microserviço para gestão de médicos",
    version="1.0.0"
)

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializa banco de dados
init_db()

# Inclui as rotas
app.include_router(medicos.router, prefix="/api/medicos")

@app.get("/")
async def health_check():
    return {"status": "API de Médicos operacional"}
