import argparse
import logging

from urllib.parse import urljoin, urlparse

import requests


URL_TEMPLATE = 'https://api-ssl.bitly.com/v4/bitlinks/'


def count_clicks(token, user_args):
    link = urlparse(user_args)
    url_prefix = f'{link.netloc}{link.path}/clicks/summary/'
    url = urljoin(URL_TEMPLATE, url_prefix)

    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    clicks_count = response.json()

    return clicks_count['total_clicks']