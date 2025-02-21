import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.api.dependencies import get_db

# Create a dummy result and session to override the database dependency
class DummyResult:
    def scalars(self):
        return self
    def all(self):
        return []  # Return an empty list for metrics

class DummySession:
    async def execute(self, query):
        return DummyResult()

async def override_get_db():
    yield DummySession()

# Override the dependency in the test context
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_get_metrics_endpoint():
    response = client.get("/api/v1/monitoring/metrics")
    assert response.status_code == 200
    data = response.json()
    # The endpoint is expected to return an empty list
    assert isinstance(data, list)
    assert len(data) == 0
