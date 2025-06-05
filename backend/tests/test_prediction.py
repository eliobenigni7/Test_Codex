from app.services.prediction import monte_carlo_tco


def test_monte_carlo_shape():
    history = [100, 110, 105]
    df = monte_carlo_tco(history, years=2, iterations=5, seed=42)
    assert df.shape == (5, 2)
    assert not df.isnull().any().any()
