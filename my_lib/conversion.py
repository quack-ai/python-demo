# Copyright (C) 2023, Quack AI.

# This program is licensed under the Apache License 2.0.
# See LICENSE or go to <https://www.apache.org/licenses/LICENSE-2.0> for full license details.

from typing import List

__all__ = ["convert_fahrenheit_to_celsius", "log_message"]


def convert_fahrenheit_to_celsius(input_temperatures: List[float]) -> List[float]:
    """Converts temperatures from Fahrenheit to Celsius.

    Args:
        input_temperatures: the list of temperatures in Fahrenheit

    Returns:
        the temperatures converted to Celsius
    """

    return [(fahrenheit_temp - 32) * 5 / 9 for fahrenheit_temp in input_temperatures]


def log_message(message):
	"""Logs a message

	Args:
		message: a string
	"""
	import logging
	logging.info(message)
