"""crispdm — small, well-documented helpers shared across the use-case notebooks.

The package is organised to mirror the CRISP-DM phases so that, while working
through a notebook, you can see exactly which phase a helper belongs to:

    from crispdm import data_understanding as du
    from crispdm import data_preparation as dp
    from crispdm import evaluation as ev

Nothing here hides the interesting work — each function is short and readable
on purpose. The point is to remove boilerplate (missing-value tables, a stock
preprocessing pipeline, standard evaluation plots) so the notebooks can focus
on the *reasoning* of each phase rather than plumbing.
"""

from . import data_preparation, data_understanding, evaluation

__all__ = ["data_understanding", "data_preparation", "evaluation"]
__version__ = "0.1.0"
