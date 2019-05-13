import responses

from . import test_responses, util

url = f'{util.BASE_URL}/v2/applications'


@responses.activate
def test_application_quick(client):

    responses.add(
        responses.POST, f'{url}/quick/', json=test_responses.QUICK_RESPONSE, status=200
    )

    client.Applications.quick(test_responses.APPLICATION_GOOD_BODY)


@responses.activate
def test_application_invite(client):

    responses.add(
        responses.POST, f'{url}/invite/', json=test_responses.INVITE_RESPONSE, status=200
    )

    body = test_responses.INVITE_BODY

    client.Applications.invite(body)
