"""Phase 2 — Data Understanding helpers.

Exploratory data analysis (EDA) utilities: quick structural overviews and
missing-value diagnostics. These answer the two questions this phase always
opens with: *what is in this table?* and *how much of it is missing?*
"""

from __future__ import annotations

import pandas as pd


def data_overview(df: pd.DataFrame) -> pd.DataFrame:
    """Return a per-column summary of a DataFrame.

    For every column reports its dtype, count of non-null values, number and
    percentage of missing values, and the number of unique values. This is the
    first thing worth printing when you meet a new dataset.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataset to profile.

    Returns
    -------
    pandas.DataFrame
        One row per column, sorted by missing percentage (descending).
    """
    n = len(df)
    summary = pd.DataFrame(
        {
            "dtype": df.dtypes.astype(str),
            "non_null": df.notna().sum(),
            "missing": df.isna().sum(),
            "missing_pct": (df.isna().mean() * 100).round(2),
            "n_unique": df.nunique(dropna=True),
        }
    )
    summary["n_rows"] = n
    return summary.sort_values("missing_pct", ascending=False)


def missing_summary(df: pd.DataFrame, threshold: float = 0.0) -> pd.DataFrame:
    """List columns that contain missing values.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataset to inspect.
    threshold : float, default 0.0
        Only return columns whose missing *fraction* is strictly greater than
        this value (e.g. ``0.5`` to see columns that are more than half empty).

    Returns
    -------
    pandas.DataFrame
        Columns ``missing`` and ``missing_pct`` for the affected columns,
        sorted worst-first. Empty if nothing exceeds the threshold.
    """
    frac = df.isna().mean()
    affected = frac[frac > threshold].sort_values(ascending=False)
    return pd.DataFrame(
        {
            "missing": df[affected.index].isna().sum(),
            "missing_pct": (affected * 100).round(2),
        }
    )


def plot_missing(df: pd.DataFrame, kind: str = "matrix", **kwargs):
    """Visualise missingness with the ``missingno`` library.

    A thin convenience wrapper so notebooks don't repeat the import. ``kind``
    maps to a ``missingno`` function: ``"matrix"``, ``"bar"``, ``"heatmap"`` or
    ``"dendrogram"``. Extra keyword arguments pass straight through.

    Returns
    -------
    matplotlib.axes.Axes
        The axes drawn by ``missingno``.
    """
    import missingno as msno

    try:
        plot_fn = getattr(msno, kind)
    except AttributeError as exc:  # pragma: no cover - defensive
        raise ValueError(
            f"Unknown kind {kind!r}; expected one of "
            "'matrix', 'bar', 'heatmap', 'dendrogram'."
        ) from exc
    return plot_fn(df, **kwargs)
