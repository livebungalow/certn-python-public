import pytest
from http import HTTPStatus
from certn import requester
from certn.errors import APIError
from . import test_responses
from unittest import mock


@pytest.mark.parametrize(
    'status,content_type,content,is_json,expected',
    [
        (HTTPStatus.NO_CONTENT, 'application/json', '', True, None),
        (HTTPStatus.NO_CONTENT, 'application/json', '', False, None),
        (HTTPStatus.OK, 'application/json', '{"abc": 123}', True, {'abc': 123}),
        (HTTPStatus.OK, 'application/json', '{"abc": 123}', False, {'abc': 123}),
        (HTTPStatus.OK, 'text/plain', 'Hello!', False, 'Hello!'),
        (HTTPStatus.OK, 'text/plain', '', True, ''),
    ],
)
def test_translate_response(status, content_type, content, is_json, expected):
    mock_response = mock.Mock()
    attrs = {
        'headers.get.return_value': content_type,
        'status_code': status,
        'text': content,
        'content': f'content-{content}',
    }
    mock_response.configure_mock(**attrs)
    output = requester.translate_response(mock_response, is_json)
    if expected is None:
        assert output is None
    elif content_type != 'application/json' and not is_json:
        assert output == f'content-{content}'
    else:
        assert output == expected
    if is_json or status == HTTPStatus.NO_CONTENT:
        mock_response.headers.get.assert_not_called()
    else:
        mock_response.headers.get.assert_called_once()


@pytest.mark.parametrize(
    'status,content_type,content,is_json',
    [
        (HTTPStatus.OK, 'text/plain', 'Hello!', True),
        (HTTPStatus.OK, 'application/json', test_responses.API_ERROR_SAMPLE_JSON, True),
        (HTTPStatus.OK, 'application/json', test_responses.API_ERROR_SAMPLE_JSON, False),
    ],
)
def test_translate_response_exception(status, content_type, content, is_json):
    mock_response = mock.Mock()
    attrs = {
        'headers.get.return_value': content_type,
        'status_code': status,
        'text': content,
        'content': f'content-{content}',
    }
    mock_response.configure_mock(**attrs)
    with pytest.raises(APIError):
        requester.translate_response(mock_response, is_json)
