# Copyright (C) 2023, Quack AI.

# This program is licensed under the Apache License 2.0.
# See LICENSE or go to <https://www.apache.org/licenses/LICENSE-2.0> for full license details.

from typing import List


def makeUpper(welcome_sentence: str) -> str:
	return welcome_sentence.upper()


def add_prefix(sentence_sequence: List[str], prefix: str) -> List[str]:
	out = []
	for sentence in sentence_sequence:
		out.append(f"{prefix} {sentence}")

	return out