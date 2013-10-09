"""
Plugin to us FOAAS.herokuapp.com
"""
import requests
from util import hook

@hook.command(nick=None)
def fu(inp, nick=''):
    """.fu :to :from"""

    headers = {"accept": "text/plain"}
    url = "http://foaas.heroku.com/off/%s/%s" % (inp, nick)

    resp = requests.get(url, headers=headers)

    return resp.content.replace("- ", "", 1)
