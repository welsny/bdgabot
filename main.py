#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import requests

def send_alert():
    """
    TODO: Send an alert to the user when the page updates
    """
    pass

if __name__ == '__main__':
    file = '/Users/lola/code/bdgabot/data.md5'

    with open(file) as f:
        prev = f.read()

    r = requests.get('https://shop.bdgastore.com/collections/new-arrivals')
    curr = hashlib.md5(r.text.encode('utf-8')).hexdigest()

    if prev != curr:
        print 'not equal'
        send_alert()
        with open(file, 'w') as f:
            f.write(curr)

    else:
        print 'equal'

