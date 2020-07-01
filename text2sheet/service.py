# -*- coding: utf-8 -*-

import gspread
import json
import pytz
from datetime import datetime
from loguru import logger
from pytz import timezone
from urllib.parse import unquote

CREDENTIALS_FILE = 'gauth.json'
PHONE_NUMBERS_FILE = 'phone_numbers.json'
"""
This file contains a list of names and phone numbers who will be sending a text.
If the list gets too long, then this can be moved to some database.
Data looks like the following:
[
    {
        "name": "person_name",
        "phone": "persons_phone"
    },
    ...
]
"""
PHONE_NUMBERS = json.load(open(PHONE_NUMBERS_FILE, 'r'))


def handler(event, context):
    # Your code goes here!
    logger.info('Event: {event}', event=event)
    msg_body = unquote(event['Body'])
    sender = unquote(event['From'])
    logger.info('Body: {msg_body}', msg_body=msg_body)
    logger.info('Sender: {sender}', sender=sender)

    sender_name = next((item['name'] for item in PHONE_NUMBERS if item['phone'] == sender),
                       None)
    if sender_name is None:
        raise ValueError('Sender Unknown!')

    # get current time in San Francisco, CA time
    date_format = '%m/%d/%Y %H:%M:%S %Z'
    date = datetime.now(tz=pytz.utc)
    logger.info('Current date & time in UTC is: {}', date.strftime(date_format))

    date = date.astimezone(timezone('US/Pacific'))
    sf_date_as_string = date.strftime(date_format)

    logger.info('SF date & time is {}:', sf_date_as_string)

    # Get Google Spreadsheet and Worksheet Name based on Sender Name
    gc = gspread.service_account(CREDENTIALS_FILE)  # uses credentials from a file
    sh = gc.open('Weights')  # Spreadsheet name is `Weights`
    worksheet = sh.worksheet(sender_name)  # Worksheet name is the same as the sender name

    # Append a new row with just two columns
    worksheet.append_row([sf_date_as_string, msg_body])

    # Return value to text back via Twilio
    return '<?xml version=\"1.0\" encoding=\"UTF-8\"?>'\
           '<Response><Message><Body>Your message has been recorded!</Body></Message></Response>'
