from fastapi import FastAPI, APIRouter, HTTPException
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

from services import InformacoesCliente, mock_db_lookup, validate_msisdn

app = FastAPI()

router = APIRouter()

@router.get("/api/v1/informacoes-cliente/{msisdn}", response_model=InformacoesCliente)
def get_informacoes_cliente(msisdn: str):
    try:
        validate_msisdn(msisdn)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    info = mock_db_lookup(msisdn)
    if not info:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return info

app.include_router(router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    host = os.getenv("APP_HOST", "0.0.0.0")
    port = int(os.getenv("APP_PORT", "8000"))
    uvicorn.run(app, host=host, port=port)
