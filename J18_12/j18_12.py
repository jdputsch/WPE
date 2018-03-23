# -*- coding: utf-8 -*-
# vim: set ai sm sw=4 sts=4 ts=8 syntax=python
# vim: set filetype=python fileencoding=utf-8:

import hashlib
import os

class DirFileHash(object):

    def __init__(self, path):
        if not os.path.isdir(path):
            raise ValueError("Path is not a directory: '%'" % path)
        else:
            self.path = path

    def __getitem__(self, key):
        try:
            with open(os.path.join(self.path, key), 'rb') as file:
                return hashlib.md5(file.read()).hexdigest()
        except (FileNotFoundError, TypeError):
            return None


def main():
    d = DirFileHash('/etc/')
    print(d['hosts'])
    print(d['no_such_file'])
    print(d[2])





if __name__ == '__main__':
    main()
