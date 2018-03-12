#!/bin/env python

def multiziperator(*args):
    """Return elements of iterable inputs one at a time.

    Args:
        *args: One or more iterables
    
    Yields:
        Return elements of each input, interleaved, one at a time.

    Example:
        Given:
            letters = 'abcde'
            numbers = [1,2,3,4,5]
            symbols = '!@#$%'

            for one_item in multiziperator(letters, numbers, symbols):
                print(one_item)
        Returns:
            a
            1
            !
            etc.
    """
    item_index = 0
    while True:
        for args_index in range(0, len(args)):
            try:
                yield args[args_index][item_index]
            except IndexError:
                raise StopIteration
        item_index += 1



def main():
    letters = 'abcde'
    numbers = [1,2,3,4,5]
    symbols = '!@#$%'

    for one_item in multiziperator(letters, numbers, symbols):
        print(one_item)


if __name__ == '__main__':
    main()