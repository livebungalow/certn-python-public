import responses

from . import util

url = f'{util.BASE_URL}/v2/reports'


@responses.activate
def test_reports_pdf(client):

    application_id = 'an-application-id'

    responses.add(responses.GET, f'{url}/{application_id}/pdf/', json='', status=200)

    client.Reports.pdf(application_id)


@responses.activate
def test_reports_link(client):

    application_id = 'an-application-id'

    responses.add(responses.GET, f'{url}/{application_id}/link/', json='', status=200)

    client.Reports.link(application_id)


@responses.activate
def test_reports_web(client):

    application_id = 'an-application-id'

    responses.add(responses.GET, f'{url}/{application_id}/web/', json='', status=200)

    client.Reports.web(application_id)
