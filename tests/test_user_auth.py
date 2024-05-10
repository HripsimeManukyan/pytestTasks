import pytest
import source.user_auth as user_auth


def test_authenticate_valid_credentials():
    result = user_auth.authenticate(username="user", password="pass")
    assert result == True


def test_authenticate_invalid_username():
    result = user_auth.authenticate(username="Jon", password="pass")
    assert result == False


def test_authenticate_invalid_password():
    result = user_auth.authenticate(username="user", password="nopass")
    assert result == False


def test_authenticate_empty_credentials():
    result = user_auth.authenticate(username ="", password="")
    assert result == False

#
# def test_authenticate_valid_credentials():
#     assert user_auth.authenticate("example_user", "password123") == True
#
#
#
#
@pytest.mark.parametrize("username, password, expected",[("user", "pass", True),
                                                          ("jon", "pass", False),
                                                          ("user", "nopass", False) ,
                                                               ("", " ", False),
                                                                   ])
def test_authenticate(username, password, expected):
    assert user_auth.authenticate(username,password) == expected


@pytest.fixture
def valid_credentials():
    return "user", "pass"

@pytest.fixture
def invalid_credentials():
    return "invalid_user", "wrong_pass"
