from typing import List

from pandas import DataFrame

from ..models import CostEntry


def allocate_costs(raw_spend: DataFrame) -> List[CostEntry]:
    entries = []
    for _, row in raw_spend.iterrows():
        entry = CostEntry(application_id=row["application_id"], amount=row["amount"])
        entries.append(entry)
    return entries
