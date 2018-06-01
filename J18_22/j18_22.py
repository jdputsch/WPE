# -*- coding: utf-8 -*-
# vim: set ai sm sw=4 sts=4 ts=8 syntax=python
# vim: set filetype=python fileencoding=utf-8:

import time

MIN_DELAY = 60.0

function_called_time = {}

class TooSoonError(Exception):
    pass

def once_per_minute(function):
    """Limit execution of function to once per minute."""

    def wrapper(*args, **kwargs):
        now = time.time()
        timer_start = function_called_time.setdefault(function, now)
        delay = now - timer_start
        if now is timer_start or delay > MIN_DELAY:
            if delay > MIN_DELAY:
                function_called_time[function] = now
            return function(*args, **kwargs)
        else:
            raise TooSoonError(
                "Wait another {} seconds".format(
                    MIN_DELAY - delay))
    return wrapper


@once_per_minute
def hello(name):
    return "Hello, {}".format(name)

def main():
    for i in range(30):
        print(i)
        try:
            time.sleep(3)
            print(hello("attempt {}".format(i)))
        except TooSoonError as e:
            print("Too soon: {}".format(e))

if __name__ == "__main__":
    main()