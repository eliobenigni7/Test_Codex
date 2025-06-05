"""TCO prediction utilities."""
from __future__ import annotations

import random
from typing import Iterable, List

import pandas as pd


def monte_carlo_tco(
    history: Iterable[float],
    years: int,
    iterations: int = 1000,
    seed: int | None = None,
) -> pd.DataFrame:
    """Run Monte Carlo simulation to forecast future TCO.

    Parameters
    ----------
    history:
        Historical TCO values ordered chronologically.
    years:
        Number of future years to forecast.
    iterations:
        How many simulation runs to perform.
    seed:
        Optional random seed for reproducible results.

    Returns
    -------
    pandas.DataFrame
        DataFrame with shape ``(iterations, years)`` containing simulated
        TCO values for each future year.
    """
    hist = list(history)
    if seed is not None:
        random.seed(seed)
    if len(hist) < 2:
        raise ValueError("Need at least two historical observations")

    growth_rates: List[float] = [
        (cur - prev) / prev for prev, cur in zip(hist, hist[1:])
    ]
    mu = sum(growth_rates) / len(growth_rates)
    sigma = (sum((g - mu) ** 2 for g in growth_rates) / len(growth_rates)) ** 0.5

    results = pd.DataFrame(
        index=range(iterations), columns=range(1, years + 1), dtype=float
    )
    last_cost = hist[-1]
    for i in range(iterations):
        cost = last_cost
        for year in range(1, years + 1):
            growth = random.gauss(mu, sigma)
            cost *= 1 + growth
            results.at[i, year] = cost
    return results
