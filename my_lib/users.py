# Copyright (C) 2023, Quack AI.

# This program is licensed under the Apache License 2.0.
# See LICENSE or go to <https://www.apache.org/licenses/LICENSE-2.0> for full license details.

__all__ = ["userGreeter"]


class userGreeter:
	"""Implements a user handling agent

	Args:
		name: the user name
	"""
	def __init__(self, name: str) -> None:
		self.name = name

	def greet(self):
		"""Returns a greeting message"""
		return "Hello " + self.name + "! Nice to meet you."
