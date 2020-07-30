#!/usr/bin/env python

import zulip

# Keyword arguments 'email' and 'api_key' are not required if you are using ~/.zuliprc
client = zulip.Client(email="myjarvis-bot@zulipchat.com",
                      api_key="7qKiL8XHlACE6ABb6RrkEVOb0LPy08XF",
                      site="https://hack36.zulipchat.com")

# Send a private message


def send_message(message, email):
    client.send_message({
        "type": "private",
        "to": email,
        "content": message,
    })
