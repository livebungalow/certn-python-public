import responses

from . import test_responses, util


url = f'{util.BASE_URL}/v2/properties'


@responses.activate
def test_properties_list(client):

    responses.add(
        responses.GET, f'{url}/', json=test_responses.PROPERTIES_LIST_RESPONSE, status=200
    )

    client.Properties.list()


@responses.activate
def test_properties_get(client):

    listings = test_responses.PROPERTIES_LIST_RESPONSE.get('results')

    listing_id = listings[0].get('id')

    responses.add(
        responses.GET,
        f'{url}/{listing_id}',
        json=test_responses.PROPERTIES_LIST_RESPONSE,
        status=200,
    )

    client.Properties.get(listing_id)


@responses.activate
def test_properties_add(client):

    body = {
        'address': '123 Fakestreet',
        'city': 'Victoria',
        'province_state': 'BC',
        'owner_id': client.user_id,
    }

    responses.add(
        responses.POST, f'{url}/', json=test_responses.PROPERTY_GET_RESULT, status=200
    )

    client.Properties.add(body)


@responses.activate
def test_properties_update(client):

    property_id = test_responses.PROPERTY_GET_RESULT.get(id)

    responses.add(
        responses.PUT,
        f'{url}/{property_id}/',
        json=test_responses.PROPERTY_GET_RESULT,
        status=200,
    )

    body = {'city': 'Abotsford'}

    client.Properties.update(property_id, body)


@responses.activate
def test_properties_delete(client):

    property_id = test_responses.PROPERTY_GET_RESULT.get(id)

    responses.add(responses.DELETE, f'{url}/{property_id}/', json='', status=200)

    client.Properties.delete(property_id)
