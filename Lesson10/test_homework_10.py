import pytest
import requests

passwords = [
    ("Positive1"),
    ("Positive1235679"),
    ("Test_123"),
    ("TooLongNegativeTest1"),
    ("negativetest2"),
    ("negativetest*"),
    ("")
]

counter = 22
@pytest.mark.parametrize('password', passwords)
def test_check_password(password):
    global counter
    test_dict = {
        "name": "Julia",
        "lastName": "Ivanova",
        "email": f"email{counter}@test.com",
        "password": password,
        "repeatPassword": password
    }

    session = requests.session()
    response = session.post("https://qauto2.forstudy.space/api/auth/signup", json=test_dict)

    counter += 1
    assert response.status_code == 201

