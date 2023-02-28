# Copyright (C) 2023, Quack AI.

# This program is licensed under the Apache License 2.0.
# See LICENSE or go to <https://www.apache.org/licenses/LICENSE-2.0> for full license details.

__all__ = ["greet_contributor"]


def greet_contributor(name: str) -> str:
    """Creates a string message to greet the contributor.

    Args:
        name: name of the person to greet

    Returns:
        the greeting message
    """
    return f"Hello {name}! Nice to meet you."
