import responses


from . import test_responses, util

url = f'{util.BASE_URL}/v2/listings'


@responses.activate
def test_listings_list(client):

    responses.add(
        responses.GET, f'{url}/', json=test_responses.LISTINGS_LIST_RESPONSE, status=200
    )

    client.Listings.list()


@responses.activate
def test_listings_get(client):

    listing_id = 'my-fake-id'

    responses.add(
        responses.GET,
        f'{url}/{listing_id}/',
        json=test_responses.LISTING_RESPONSE,
        status=200,
    )

    client.Listings.get(listing_id)


@responses.activate
def test_listings_add(client):

    body = {
        'rent': '2000',
        'owner_id': client.user_id,
        'property_id': 'valid-property-id',
        'notification_list_ids': [],
    }

    responses.add(
        responses.POST, f'{url}/', json=test_responses.LISTING_RESPONSE, status=200
    )

    client.Listings.add(body)


@responses.activate
def test_listings_update(client):

    listing_id = test_responses.LISTING_RESPONSE.get('id')

    responses.add(
        responses.PUT,
        f'{url}/{listing_id}/',
        json=test_responses.LISTING_RESPONSE,
        status=200,
    )

    body = {'rent': '1000'}

    client.Listings.update(listing_id, body)


@responses.activate
def test_listings_delete(client):

    listing_id = test_responses.LISTING_RESPONSE.get('id')

    responses.add(
        responses.DELETE,
        f'{url}/{listing_id}/',
        json=test_responses.AUTH_RESPONSE,
        status=200,
    )

    client.Listings.delete(listing_id)
