# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..diacritics import ACUTE
from ..utils import replacer

AREPLACE = {
    ACUTE + 'E': 'Є',
    ACUTE + 'U': 'Ю',
    ACUTE + 'A': 'Я',
}
JREPLACE = {
    'JE': 'Є',
    'JU': 'Ю',
    'JA': 'Я',
}


def get_convert():
    data = AREPLACE.copy()
    data.update({i.lower(): o.lower() for i, o in AREPLACE.items()})
    data.update(JREPLACE)
    data.update({i.title(): o for i, o in JREPLACE.items()})
    data.update({i.lower(): o.lower() for i, o in JREPLACE.items()})
    return replacer(data)


convert = get_convert()
