from typing import BinaryIO

import pandas as pd
from pandas import DataFrame


def load_spend_from_excel(file: BinaryIO) -> DataFrame:
    """Load raw spend data from an Excel file into a DataFrame."""
    return pd.read_excel(file)
