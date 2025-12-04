from pydantic import BaseModel
from datetime import date

class DetalhesOferta(BaseModel):
    nome_oferta: str
    detalhes: str
    id_oferta: str

class PrazoCancelamento(BaseModel):
    dias_restantes: int
    data_limite: date
    detalhe: str

class InformacoesCliente(BaseModel):
    msisdn: str
    nome_cliente: str
    operadora: str
    status_bilhete: str
    oferta_aceita: DetalhesOferta
    prazo_cancelamento: PrazoCancelamento

def mock_db_lookup(msisdn: str) -> InformacoesCliente | None:
    if msisdn == "5511987654321":
        return InformacoesCliente(
            msisdn=msisdn,
            nome_cliente="João da Silva",
            operadora="Telecom Fictícia",
            status_bilhete="Ativo",
            oferta_aceita=DetalhesOferta(
                nome_oferta="Plano Fictício",
                detalhes="5GB de internet, ligações ilimitadas",
                id_oferta="12345"
            ),
            prazo_cancelamento=PrazoCancelamento(
                dias_restantes=15,
                data_limite=date(2025, 12, 31),
                detalhe="Cancelamento gratuito até a data limite"
            )
        )
    return None

def validate_msisdn(msisdn: str) -> None:
    if not msisdn.isdigit():
        raise ValueError("MSISDN inválido ou mal formatado")
    if not (11 <= len(msisdn) <= 13):
        raise ValueError("MSISDN inválido ou mal formatado")
