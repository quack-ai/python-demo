import pytest

from my_lib.users import validate_user_info


@pytest.mark.parametrize(
    "user_info, is_valid",
    [
        [{"name": "Richard Hendricks"}, False],
        [
            {
                "created": "2023-05-15T14:42:47.571141",
                "updated_at": "2023-05-15T15:24:27.648219",
                "name": "Richard Hendricks",
            },
            False,
        ],
        [
            {
                "created_at": "2023-05-15T14:42:47.571141",
                "updated_at": "2023-05-15T15:24:27.648219",
                "name": "Richard Hendricks",
            },
            True,
        ],
    ],
)
def test_validate_user_info(user_info, is_valid):
    assert validate_user_info(user_info) is is_valid
