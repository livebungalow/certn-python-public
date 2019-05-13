import responses
import pytest

import certn
from . import test_responses, util

url = f'{util.BASE_URL}/v1'


@responses.activate
def test_login_fail():
    responses.add(
        responses.POST,
        f'{url}/authenticate/',
        json=test_responses.AUTH_RESPONSE_FAIL,
        status=401,
    )

    with pytest.raises(certn.errors.InvalidRequestError):
        certn.Client(
            username=util.USERNAME, password=util.PASSWORD, environment=util.ENVIRONMENT
        )


@responses.activate
def test_login(client):

    assert client.user_id is not None, 'Username was not set'
    assert client.token is not None, 'Token was not set'


@responses.activate
def test_logout_all(client):

    responses.add(responses.POST, f'{url}/logoutall/', status=204)

    response = client.Auth.logout_all()
    assert response is None


@responses.activate
def test_logout(client):

    responses.add(responses.POST, f'{url}/logout/', status=204)
    response = client.Auth.logout()
    assert response is None


@responses.activate
def test_list_logins(client):

    responses.add(
        responses.GET,
        f'{url}/authenticate/',
        json=test_responses.AUTH_RESPONSE_LIST_LOGINS,
        status=200,
    )

    client.Auth.list()
