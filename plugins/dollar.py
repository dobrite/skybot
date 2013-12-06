"""
Plugin to for value of a dollar
"""
import random
from util import hook

@hook.command(autohelp=False)
def dollar(inp, say=None):
    """.dollar"""

    adj = random.choice(['hella', 'buttload'])

    val = {
        'dollar': '$1.00',
        'high': '$1.00',
        'low': '$1.00',
        'vol': 'a %s USD' % adj,
    }

    say("Current: \x0307%(dollar)s\x0f - High: \x0307%(high)s\x0f"
        " - Low: \x0307%(low)s\x0f - Volume: %(vol)s" % val)
