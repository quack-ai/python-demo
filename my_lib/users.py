# Copyright (C) 2023, Quack AI.

# This program is licensed under the Apache License 2.0.
# See LICENSE or go to <https://www.apache.org/licenses/LICENSE-2.0> for full license details.

from datetime import datetime
from typing import Any, Dict, List

__all__ = ["greet_contributor", "process_table"]


def greet_contributor(name: str) -> str:
    """Creates a string message to greet the contributor.

    Args:
        name: name of the person to greet

    Returns:
        the greeting message
    """
    return f"Hello {name}! Nice to meet you."


def validate_user_info(user_info: Dict[str, Any]) -> bool:
    """Validate each payload to avoid errors later in backend

    Args:
        user_info: a dictionary with at least 3 entries (created_at, updated_at, name)
    Returns:
        whether the payload can be processed
    """
    # Mandatory fields
    if any(key not in user_info for key in {"created_at", "updated_at", "name"}):
        return False
    # Check datetime
    if user_info["created_at"] > user_info["updated_at"] or user_info["updated_at"] > datetime.utcnow().isoformat():
        return False
    # Check identity
    if len(user_info["name"]) < 5:
        return False

    return True


def process_table(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Process the SQL table to only keep the ones that aren't corrupted

    Args:
        users: list where each element is a user entry from the table
    Returns:
        the list of processable user payloads
    """
    valid_users = [user for user in users if validate_user_info(user)]
    return valid_users
