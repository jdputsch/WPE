# -*- coding: utf-8 -*-
# vim: set ai sm sw=4 sts=4 ts=8 syntax=python
# vim: set filetype=python fileencoding=utf-8:

import sys

class Tee(object):
    """A 'tee' like class."""

    def __init__(self, *args):
        """Write output to one or more file-like objects.

        Args:
            *args: One or more file-like object
        """
        if not args:
            raise TypeError("Tee() needs at least one file-like argument")

        self._files = args

    def __enter__(self):
        """Since we are passed open file descriptors, just return self"""
        return(self)

    def __exit__(self, type, value, traceback):
        for f in self._files:
            f.flush()
            f.close()

    def write(self, string):
        """Write the given string to each file object"""
        for f in self._files:
            f.write(string)



def main():
    import sys
    f1 = open('/tmp/tee1.txt', 'w')
    f2 = open('/tmp/tee2.txt', 'w')
    t = Tee(sys.stdout, f1, f2)
    t.write('abc\n')
    t.write('def\n')
    t.write('ghi\n')
    f1.close()
    f2.close()

    f1 = open('/tmp/tee1_ctx.txt', 'w')
    f2 = open('/tmp/tee2_ctx.txt', 'w')
    with Tee(sys.stdout, f1, f2) as t:
        t.write('abc\n')
        t.write('def\n')
        t.write('ghi\n')


if __name__ == "__main__":
    main()