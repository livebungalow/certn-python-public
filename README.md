# certn-python

A Python client for [Certn. API](https://certn.co/api/)

[![Latest PyPI version](https://img.shields.io/pypi/v/certn-python.svg)](https://pypi.python.org/pypi/certn-python)

[![Latest Travis CI build status](https://travis-ci.com/livebungalow/certn-python-public.png)](https://travis-ci.com/livebungalow/certn-python-public)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

## Installation

```bash
pip install certn-python
```

## Requirements

- ```requests>=2,<3```

## Basic Usage

Submit an application and check its results

```python
from certn import Client
import time


client = Client(username='*****' password='***')

body = {
    "information": {
        "first_name": "Fake",
        "last_name": "Name",
        "date_of_birth": "1987-03-04",
        "addresses": [
            {
                "address": "123 fakestreet",
                "city": "VICTORIA",
                "province_state": "BC",
                "country": "CA"
            }
        ]
    }
}

application = client.Applications.quick(body)

while application.status == 'Analyzing':
    time.sleep(5)  # 2-10 seconds to process, but can occasionally take up to 300 seconds
    application = client.Applicants.get(application.id)

print('Application has returned!')

client.logout()
```

Invite an applicant to apply

```python
from certn import Client

client = Client(username='*****' password='***')

body = {
    'email': 'fake@fake.com',
    'email_applicants': False
}

application = client.Applications.invite(body)

client.logout()
```

List all the logged in sessions and log them all count

```python

from certn import Client

client = Client(username='*****' password='***')

client.Auth.list()

client.Auth.logout_all()
```

add a property, list, get the property information and remove the property

```python
from certn import Client

client = Client(username='*****' password='***')

body = {
    'address': '123 fakestreet',
    'city': 'VICTORIA',
    'province_state': 'BC',
    'owner_id': client.user_id,
}

property = client.Properties.add(body)

client.Properties.list()

client.Properties.get(property.get('id'))

client.Properties.delete(property.get('id'))

client.logout()
```

add a listing, list, get the listings information and remove the listing

```python
from certn import Client

client = Client(username='*****' password='***')

body = {
    'address': '123 fakestreet',
    'city': 'VICTORIA',
    'province_state': 'BC',
    'owner_id': client.user_id,
}

property = client.Properties.add(body)

body = {
    'rent': 1000,
    'owner_id': client.user_id,
    'property_id': property.get('id'),
    'notification_list_ids': [],
}

listing = client.Listings.add(body)

client.Listings.list()

client.Listings.get(listing.get('id'))

client.Listings.delete(listing.get('id'))

client.Properties.delete(property.get('id'))

client.logout()
```

can also be called alternatively

```python
from certn import Client

with Client(username, password) as client:
    client.Listings.list()

```

## Authors

[certn-python](#certn-python) was written by [Bungalow Living](engineering@bungalow.com).
