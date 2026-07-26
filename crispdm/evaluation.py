"""Phase 5 — Evaluation helpers.

Standard classification diagnostics: a tidy metrics table plus confusion-matrix
and ROC-curve plots. These let each notebook compare candidate models on the
same footing before a deployment decision is made.
"""

from __future__ import annotations

import pandas as pd


def classification_metrics(y_true, y_pred, y_score=None) -> pd.Series:
    """Return the headline classification metrics as a labelled Series.

    Reports accuracy, precision, recall and F1 (binary by default). When
    ``y_score`` — predicted probabilities or decision scores for the positive
    class — is supplied, ROC AUC is added too.

    Parameters
    ----------
    y_true : array-like
        Ground-truth labels.
    y_pred : array-like
        Predicted labels.
    y_score : array-like, optional
        Predicted probability/score for the positive class, used for ROC AUC.

    Returns
    -------
    pandas.Series
        Metric name -> value.
    """
    from sklearn.metrics import (
        accuracy_score,
        f1_score,
        precision_score,
        recall_score,
        roc_auc_score,
    )

    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1": f1_score(y_true, y_pred, zero_division=0),
    }
    if y_score is not None:
        metrics["roc_auc"] = roc_auc_score(y_true, y_score)
    return pd.Series(metrics, name="score").round(4)


def plot_confusion(y_true, y_pred, labels=None, ax=None, cmap="Blues"):
    """Plot a confusion matrix. Returns the matplotlib Axes."""
    import matplotlib.pyplot as plt
    from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix

    cm = confusion_matrix(y_true, y_pred, labels=labels)
    disp = ConfusionMatrixDisplay(cm, display_labels=labels)
    if ax is None:
        _, ax = plt.subplots(figsize=(4, 4))
    disp.plot(ax=ax, cmap=cmap, colorbar=False)
    ax.set_title("Confusion matrix")
    return ax


def plot_roc(y_true, y_score, ax=None, label=None):
    """Plot a ROC curve (with AUC in the legend). Returns the matplotlib Axes."""
    import matplotlib.pyplot as plt
    from sklearn.metrics import RocCurveDisplay

    if ax is None:
        _, ax = plt.subplots(figsize=(5, 5))
    RocCurveDisplay.from_predictions(y_true, y_score, name=label, ax=ax)
    ax.plot([0, 1], [0, 1], linestyle="--", color="grey", linewidth=1)
    ax.set_title("ROC curve")
    return ax
