import responses

from . import test_responses, util

url = f'{util.BASE_URL}/v2/applicants'


@responses.activate
def test_applicants(client):

    id = 'my-fake-id'

    responses.add(
        responses.GET,
        f'{url}/{id}/',
        json=test_responses.APPLICANT_GET_RESPONSE,
        status=200,
    )

    client.Applicants.get(id)
