#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from hermes_python.hermes import Hermes

INTENT_HOW_ARE_YOU = "hobil:how_are_you"
INTENT_COLOR = ["hobil:color"]


def main():
    with Hermes("localhost:1883") as h:
        h.subscribe_intent(INTENT_HOW_ARE_YOU, how_are_you_callback) \
         .subscribe_intent(INTENT_COLOR, color_callback) \
         .start()


def how_are_you_callback(hermes, intent_message):
    session_id = intent_message.session_id
    response = "Fine. Stop asking."
    #hermes.publish_end_session(session_id, response)
    hermes.publish_continue_session(session_id, response, INTENT_COLOR)


def color_callback(hermes, intent_message):
    session_id = intent_message.session_id
    response = "Yellow."
    hermes.publish_end_session(session_id, response)


if __name__ == "__main__":
    main()
