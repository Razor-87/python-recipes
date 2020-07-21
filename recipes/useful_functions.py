# -*- coding: utf-8 -*-
from typing import Any, Generator, Iterable, List, Optional, TextIO


def array_shift(data, shift):
    # left rotation
    from collections import deque
    items = deque(data)
    items.rotate(-shift)
    return items


def majority_element(arr: list) -> int:
    arr.sort()
    return arr[len(arr) // 2]


def pop_append(data: list, shift: int) -> list:
    for _ in range(shift):
        data.append(data.pop(0))
    return data


def find_idx(required_el: Any, lst: List[Any]) -> Optional[int]:
    # list.index() without raise an exception
    if required_el in {*lst}:
        return lst.index(required_el)
    return None


def bytes2human(n):
    """
    http://code.activestate.com/recipes/578019

    >>> bytes2human(10000)
    '9.8K'
    >>> bytes2human(100001221)
    '95.4M'
    """
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n


def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


def int_from_bytes(xbytes: bytes) -> int:
    return int.from_bytes(xbytes, 'big')


def int_to_bytes_sign(i: int, *, signed: bool = False) -> bytes:
    length = ((i + ((i * signed) < 0)).bit_length() + 7 + signed) // 8
    return i.to_bytes(length, byteorder='big', signed=signed)


def bytes_to_int_sign(b: bytes, *, signed: bool = False) -> int:
    return int.from_bytes(b, byteorder='big', signed=signed)


def datetime_now(fmt="%Y-%m-%d %H:%M:%S"):
    from datetime import datetime
    return datetime.now().strftime(fmt)


def elapsed_time() -> Generator:
    from time import monotonic
    start = monotonic()
    while True:
        yield monotonic() - start


def timeit_(param: str, n: int = 10000) -> float:
    from timeit import timeit
    return timeit(param, number=n, globals=globals())


def compare(fs, args):
    import timeit
    from matplotlib import pyplot as plt
    for f in fs:
        plt.plot(args,
                 [timeit.timeit(str(f(arg)), number=10000000) for arg in args],
                 label=f.__name__)
    plt.legend()
    plt.grid(True)
    plt.show()


def shorthand_dict(names):
    """
    >>> context = {"user_id": 42, "user_ip": "1.2.3.4"}
    >>> mode, action_type = "force", 7
    >>> shorthand_dict(["context", #doctest: +NORMALIZE_WHITESPACE
    ... "mode", "action_type"])
    {'context': {'user_id': 42, 'user_ip': '1.2.3.4'},
    'mode': 'force', 'action_type': 7}
    """
    from inspect import currentframe
    lcls = currentframe().f_back.f_locals
    return {k: lcls[k] for k in names}


def string_validators(string: str) -> list:
    """
    >>> string_validators('qA2')
    [True, True, True, True, True]
    >>> string_validators('123')
    [True, False, True, False, False]
    """
    dict_methods = {
        'isalnum': (char.isalnum() for char in string),
        'isalpha': (char.isalpha() for char in string),
        'isdigit': (char.isdigit() for char in string),
        'islower': (char.islower() for char in string),
        'isupper': (char.isupper() for char in string),
    }
    return [*map(any, dict_methods.values())]


def unique(iterable, seen=None):
    seen = set(seen or [])
    acc = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            acc.append(item)
    return acc


def unique_stable(arr: Iterable) -> Generator:
    dupes = set()
    for val in arr:
        if val not in dupes:
            dupes.add(val)
            yield val


def unique_mutable_elements(seq):
    """
    Amount different mutable/immutable elements

    >>> len_mutable_elements([1, [2], 1, [2], 3])
    4
    """
    return len({id(el) for el in seq})


def ifile(name: str) -> Generator:
    with open(name, encoding='utf-8') as f:
        yield from f


def download_file_in_chunks(url, filename, chunk_size=512):
    from requests import get
    response = get(url, stream=True, allow_redirects=True)
    with open(filename, "wb") as handle:
        # handle.write(response.content)
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:  # filter out keep-alive new chunks
                handle.write(chunk)


def yield_from_merging(*iterables, sorting=True, reverse=False, key=None):
    """
    >>> [*yield_from_merging([5, 3, 1, 0], [7, 8, 0, 9, 8])]
    [0, 0, 1, 3, 5, 7, 8, 8, 9]
    >>> [*yield_from_merging([5, 3, 1, 0], [7, 8, 0, 9, 8], reverse=True)]
    [9, 8, 8, 7, 5, 3, 1, 0, 0]
    """
    from heapq import merge
    if sorting:
        iterables = (sorted(iterable, reverse=reverse, key=None)
                     for iterable in iterables)
    yield from merge(*iterables, reverse=reverse, key=None)


def string_to_dict(s: str,
                   key_first: bool = True,
                   types: Optional[tuple] = None) -> dict:
    lst = s.split()
    zipped = zip(lst[::2], lst[1::2]) if key_first else zip(
        lst[1::2], lst[::2])
    if types is None:
        return dict(zipped)
    key_type, value_type = types if key_first else reversed(types)
    return {key_type(key): value_type(value) for key, value in zipped}


def search_lines(lines: TextIO, pattern: str, history: int = 5) -> Generator:
    from collections import deque
    previous_lines: deque = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


def chain(*iterables: Iterable) -> Generator:
    """
    >>> [*chain(['A', 'B', 'C'], [0, 1, 2])]
    ['A', 'B', 'C', 0, 1, 2]
    """
    for i in iterables:
        yield from i


def updown(n: int) -> Generator:
    """
    >>> [*updown(3)]
    [1, 2, 3, 2, 1]
    """
    yield from range(1, n)
    yield from range(n, 0, -1)


def chunks(g, n=2):
    """
    Collect data into chunks of a maximum size
    chunks('ABCDEFG', 3) --> ABC DEF G
    """
    from itertools import islice, repeat
    yield from map(lambda it: islice(it, n), repeat(iter(g)))


def chunks_(string, k):
    yield from zip(*(iter(string), ) * k)


def grouper(iterable: Iterable,
            n: int,
            fillvalue: Optional[str] = '') -> Generator[str, None, None]:
    """
    Collect data into fixed-length chunks or blocks
    grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx

    >>> big_string = "gfdgfgdgdbvcgjkjhddfgr hfghfgf kjhkhjtgg ghfvbvcbcvfhjkh"
    >>> [''.join(chunk) for chunk #doctest: +NORMALIZE_WHITESPACE
    ... in grouper(big_string, 10, '_')]
    ['gfdgfgdgdb', 'vcgjkjhddf', 'gr hfghfgf',
    ' kjhkhjtgg', ' ghfvbvcbc', 'vfhjkh____']
    """
    from itertools import zip_longest
    args = (iter(iterable), ) * n
    yield from zip_longest(fillvalue=fillvalue, *args)


def roundrobin(*iterables):
    """
    Recipe credited to George Sakkis
    roundrobin('ABC', 'D', 'EF') --> A D E B F C
    """
    import itertools
    num_active = len(iterables)
    nexts = itertools.cycle(iter(it).__next__ for it in iterables)
    while num_active:
        try:
            for nxt in nexts:
                yield nxt()
        except StopIteration:
            # Remove the iterator we just exhausted from the cycle.
            num_active -= 1
            nexts = itertools.cycle(itertools.islice(nexts, num_active))


def unique_everseen(iterable, key=None):
    """
    List unique elements, preserving order. Remember all elements ever seen.
    unique_everseen('AAAABBBCCDAABBB') --> A B C D
    unique_everseen('ABBCcAD', str.lower) --> A B C D
    """
    from itertools import filterfalse
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in filterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element