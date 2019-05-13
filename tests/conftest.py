import certn
import responses
import pytest
from . import test_responses
from . import util


@pytest.fixture
@responses.activate
def client():
    '''Test wrapper, used to initialize client for requests'''
    responses.add(
        responses.POST,
        'https://demo-api.certn.co/api/v1/authenticate/',
        json=test_responses.AUTH_RESPONSE,
        status=200,
    )
    return certn.Client(
        username=util.USERNAME, password=util.PASSWORD, environment=util.ENVIRONMENT
    )
