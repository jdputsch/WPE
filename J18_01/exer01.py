#!/usr/bin/env python
from collections import defaultdict

USER_PROMPT = 'Tell me where you went: '

def parse_input(input_line):
    city, state = input_line.split(',')
    city = city.strip()
    state = state.strip()
    return (city, state)

def get_user_input(travels):
    while True:
        try:
            input_line = input(USER_PROMPT)
            if not input_line:
                break
            city, state = parse_input(input_line)
            travels[state][city] += 1
        except ValueError:
            print("That's not a legal city, state combination")
            pass
    return travels

def travel_report(travels):
    print("You visited:")
    for state in sorted(travels):
        print(state)
        for city in sorted(travels[state]):
            count = ''
            if travels[state][city] > 1:
                count = ' (%s)' % travels[state][city]
            print('    %s%s' % (city, count))


def main():
    travels = defaultdict(lambda: defaultdict(int))
    travels = get_user_input(travels)
    travel_report(travels)

if __name__ == '__main__':
    main()