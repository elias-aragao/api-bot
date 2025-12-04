import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_success_msisdn_found(client):
    response = client.get("/api/v1/informacoes-cliente/5511987654321")
    assert response.status_code == 200
    data = response.json()
    assert data["status_bilhete"] == "Ativo"
    assert data["nome_cliente"] == "João da Silva"
    assert data["operadora"] == "Telecom Fictícia"
    assert data["oferta_aceita"]["nome_oferta"] == "Plano Fictício"

def test_failure_msisdn_not_found(client):
    response = client.get("/api/v1/informacoes-cliente/99999999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Cliente não encontrado"

def test_failure_invalid_msisdn_format(client):
    response = client.get("/api/v1/informacoes-cliente/ABC12345")
    assert response.status_code == 400
