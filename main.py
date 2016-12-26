#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import requests
import time

import twilio_credentials as tc
from twilio.rest import TwilioRestClient

def main():
    """ Check if Bodega's New Arrivals page has updated """
    file = './data.sha1'

    with open(file) as f:
        prev = f.read()

    r = requests.get('https://shop.bdgastore.com/collections/new-arrivals')
    curr = hashlib.sha1(r.text.encode('utf-8')).hexdigest()

    if prev != curr:
        print 'Stock has updated! Text alert sent.'
        send_alert()
        with open(file, 'w') as f:
            f.write(curr)

    else:
        print 'Stock has not yet updated.'

def send_alert():
    """ Sends an SMS alert via. Twilio """
    client.messages.create(to=tc.welsny_cell, from_=tc.twilio_cell,
                                     body="Bodega has updated")

if __name__ == '__main__':
    client = TwilioRestClient(tc.account_sid, tc.auth_token)
    while True:
        main()
        time.sleep(600)

