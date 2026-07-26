"""Phase 3 — Data Preparation helpers.

Utilities for turning a raw, cleaned table into a modelling matrix: splitting
features from the target and building a standard scikit-learn preprocessing
pipeline for mixed numeric/categorical data.
"""

from __future__ import annotations

from typing import Sequence

import pandas as pd


def split_features_target(df: pd.DataFrame, target: str):
    """Split a DataFrame into a feature matrix ``X`` and a target vector ``y``.

    Parameters
    ----------
    df : pandas.DataFrame
        The modelling table.
    target : str
        Name of the column to predict.

    Returns
    -------
    (pandas.DataFrame, pandas.Series)
        ``X`` (all columns except ``target``) and ``y`` (the ``target`` column).
    """
    if target not in df.columns:
        raise KeyError(f"target column {target!r} not found in DataFrame")
    X = df.drop(columns=[target])
    y = df[target]
    return X, y


def infer_column_types(X: pd.DataFrame):
    """Split column names into numeric and categorical lists by dtype.

    A pragmatic default used to configure a preprocessor. Numeric columns are
    those with a numeric dtype; everything else (object, category, bool) is
    treated as categorical.

    Returns
    -------
    (list[str], list[str])
        ``(numeric_columns, categorical_columns)``.
    """
    numeric = X.select_dtypes(include="number").columns.tolist()
    categorical = [c for c in X.columns if c not in numeric]
    return numeric, categorical


def build_preprocessor(
    numeric: Sequence[str],
    categorical: Sequence[str],
    scale: bool = True,
):
    """Build a scikit-learn ``ColumnTransformer`` for mixed-type features.

    Numeric columns are median-imputed and (optionally) standardised;
    categorical columns are most-frequent-imputed and one-hot encoded. The
    result plugs straight into a :class:`~sklearn.pipeline.Pipeline` in the
    Modeling phase, which keeps every transform inside cross-validation and so
    avoids leaking test information into training.

    Parameters
    ----------
    numeric, categorical : sequence of str
        Column names for each branch (see :func:`infer_column_types`).
    scale : bool, default True
        Whether to standardise numeric columns. Leave ``True`` for linear /
        distance-based models; ``False`` is fine for tree ensembles.

    Returns
    -------
    sklearn.compose.ColumnTransformer
    """
    from sklearn.compose import ColumnTransformer
    from sklearn.impute import SimpleImputer
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import OneHotEncoder, StandardScaler

    numeric_steps = [("impute", SimpleImputer(strategy="median"))]
    if scale:
        numeric_steps.append(("scale", StandardScaler()))

    categorical_pipe = Pipeline(
        [
            ("impute", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    return ColumnTransformer(
        [
            ("num", Pipeline(numeric_steps), list(numeric)),
            ("cat", categorical_pipe, list(categorical)),
        ],
        remainder="drop",
    )
