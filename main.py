#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codecs import open
import requests

def send_alert():
    """
    TODO: Send an alert to the user when the page updates
    """
    pass

if __name__ == '__main__':
    file = '/Users/lola/code/bdgabot/data.htm'

    with open(file, 'r', 'utf-8') as f:
        prev = f.read()

    r = requests.get('https://shop.bdgastore.com/collections/new-arrivals')
    curr = r.text

    if prev != curr:
        print 'not equal'
        with open(file, 'w', 'utf-8') as f:
            f.write(curr)

    else:
        send_alert()

