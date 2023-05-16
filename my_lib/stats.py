# Copyright (C) 2023, Quack AI.

# This program is licensed under the Apache License 2.0.
# See LICENSE or go to <https://www.apache.org/licenses/LICENSE-2.0> for full license details.

from typing import List, Tuple

import numpy as np
import requests

__all__ = ["fetch_grades", "log_results"]


def fetch_grades(num_samples: int) -> List[float]:
    """Fetch the updated programming"""
    return np.random.rand(num_samples).tolist()


def compute_stats(grades: List[float]) -> Tuple[float, float]:
    """Computes the relevant statistics over the distribution

    Args:
            grades: the whole list of programming evaluation scores
    Returns:
            the mean and median value of the distribution
    """
    import ipdb; ipdb.set_trace()
    return (
        np.mean(grades),
        np.median(grades),
    )


def log_results(grades):
    """Aggregate the results into an easy-to-understand string

    Args:
            grades: the whole list of programming evaluation scores
    Returns:
            the summary string
    """
    stats = compute_stats(grades)
    print(stats)
    return f"The analysis was run on {len(grades)} samples\nMean: {stats[0]}\nMedian: {stats[1]}"
