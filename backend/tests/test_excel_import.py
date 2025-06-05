from io import BytesIO

import pandas as pd

from app.services.excel_import import load_spend_from_excel


def test_load_spend_from_excel():
    df = pd.DataFrame({"application_id": ["123"], "amount": [10.0]})
    buf = BytesIO()
    df.to_excel(buf, index=False)
    buf.seek(0)

    loaded = load_spend_from_excel(buf)

    assert list(loaded.columns) == ["application_id", "amount"]
    assert loaded.shape == (1, 2)
    assert float(loaded.loc[0, "amount"]) == 10.0
