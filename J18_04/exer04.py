#!/usr/bin/env python

import arrow
import re

LOG_FIELD_PATTERN = re.compile(r'(?P<ip_address>\d{1,3}\.\d{1,3}\.\d{1,'
                               r'3}\.\d{1,3})'
                               r'[^[]+\[(?P<timestamp>[^]]+)\]'
                               r'\s+"(?P<request>[^"]+)"')


class LogDicts:

    def __init__(self, log_file):
        self.entries = []
        with open(log_file) as f:
            for line in f.readlines():
                m = LOG_FIELD_PATTERN.match(line)
                self.entries.append(m.groupdict())
                self.entries[-1]['timestamp'] = arrow.get(
                    self.entries[-1]['timestamp'], 'DD/MMM/YYYY:HH:mm:ss Z')
                pass

    def dicts(self, key=None):
        if key:
            return sorted(self.entries, key)
        else:
            return self.entries

    def earliest(self):
        return min(self.entries, key=lambda x: x['timestamp'])

    def for_ip(self, ip_address, key=None):
        res = [e for e in self.entries if e['ip_address'] == ip_address]
        if key:
            return sorted(res, key)
        else:
            return res

    def for_request(self, text, key=None):
        res = [e for e in self.entries if text in e['request']]
        if key:
            return sorted(res, key)
        else:
            return res

    def iterdicts(self, key=None):
        if key:
            for i in sorted(self.entries, key):
                yield i
        else:
            for i in self.entries:
                yield i

    def latest(self):
        return max(self.entries, key=lambda x: x['timestamp'])

if __name__ == "__main__":
    ld = LogDicts('mini-access-log.txt')

    ld.dicts()

    pass