# Copyright (C) 2023, Quack AI.

# This program is licensed under the Apache License 2.0.
# See LICENSE or go to <https://www.apache.org/licenses/LICENSE-2.0> for full license details.

from collections import defaultdict
from typing import Dict, List

__all__ = ["Developer"]


class Developer:
	def __init__(self, name: str, language: str, num_commits: int, years_of_xp: int) -> None:
		self.name = name
		self.language = language
		self.num_commits = num_commits
		self.years_of_xp = years_of_xp


def analyze_team(developers: List[Developer]) -> Dict[str, int]:
	"""Check the current technology split of a dev population"""

	language_count = defaultdict(int)
	for dev in developers:
		language_count[dev.language] += 1

	return language_count
