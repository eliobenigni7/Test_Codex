from app.models.application import Application
from app.models.cost_entry import CostEntry


def test_application_model():
    app = Application(name="Test")
    assert app.name == "Test"


def test_cost_entry_model():
    cost = CostEntry(amount=10.0)
    assert cost.amount == 10.0
