# coding: utf-8
from __future__ import unicode_literals
import requests
import bs4


class Item(object):
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def price(self):
        return self._price

    @property
    def name(self):
        return self._name


class PriceList(object):
    _ENDPOINT = 'http://csgo.exchange/prices/'
    _content = []
    _MAP = (
        ('data-ft', ' (Field-Tested)'),
        ('data-fn', ' (Factory New)'),
        ('data-ww', ' (Well-Worn)'),
        ('data-mw', ' (Minimal Wear)'),
        ('data-bs', ' (Battle-Scarred)'),
        ('data-vn', ''),
    )
    _KNIFES = (
        'Bayonet',
        'Butterfly Knife',
        'Falchion Knife',
        'Flip Knife',
        'Gut Knife',
        'Huntsman Knife',
        'Karambit',
        'M9 Bayonet',
        'Shadow Daggers',
        'Bowie Knife',
    )

    def prices(self):
        response = requests.get(self._ENDPOINT)
        self._content = bs4.BeautifulSoup(response.content, 'html.parser')
        for row in self._content.find_all('tr', {'class': 'cItem'}):
            for name, price in self._get_items_from_row(row):
                yield Item(name, price)

    def _get_items_from_row(self, row):
        name = row.find('a').text
        name = name.replace('StatTrak', 'StatTrak™')
        for knife in self._KNIFES:
            if name.find(knife) > -1:
                name = '★ %s' % name
                break
        for arg_name, postfix in self._MAP:
            value = float(row.get(arg_name, 0))
            if value == 0:
                continue
            yield (name + postfix, value)
