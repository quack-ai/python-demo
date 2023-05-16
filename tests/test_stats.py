import pytest

from my_lib.stats import compute_stats, fetch_grades, log_results


@pytest.mark.parametrize(
    "num_samples",
    [
        5,
        10,
        34,
    ],
)
def test_fetch_grades(num_samples):
    grades = fetch_grades(num_samples)
    assert isinstance(grades, list) and len(grades) == num_samples and all(isinstance(grade, float) for grade in grades)


@pytest.mark.parametrize(
    "grades, mean_val, median_val",
    [
        [
            [90, 60, 12, 64, 74],
            60,
            64,
        ],
    ],
)
def test_compute_stats(grades, mean_val, median_val):
    assert compute_stats(grades) == (mean_val, median_val)


@pytest.mark.parametrize(
    "grades, expected_str",
    [
        [[90, 60, 12, 64, 74], "The analysis was run on 5 samples\nMean: 60.0\nMedian: 64.0"],
    ],
)
def test_log_results(grades, expected_str):
    assert log_results(grades) == expected_str
