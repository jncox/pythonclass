"""A module for demonstrating exceptions."""

import sys

from math import log

def string_log(s):
    v = convert(s)
    return log(v)

def convert(s):
    """Convert to an integer."""
    x = -1
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}"\
              .format(str(e)),
              file=sys.stderr)
        raise