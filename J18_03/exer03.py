#!/usr/bin/env python

import fileinput
import re

LOG_FIELD_PATTERN = re.compile(r'(?P<ip_address>\d{1,3}\.\d{1,3}\.\d{1,'
                               r'3}\.\d{1,3})'
                               r'[^[]+\[(?P<timestamp>[^]]+)\]'
                               r'\s+"(?P<request>[^"]+)"')

result = []
for line in fileinput.input():
    m = LOG_FIELD_PATTERN.match(line)
    result.append(m.groupdict())

print(result)
