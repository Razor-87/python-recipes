# -*- coding: utf-8 -*-
# @Author: razor87
# @Date:   2019-10-01 18:10:45
# @Last Modified by:   razor87
# @Last Modified time: 2019-10-02 19:59:00

bin(0x7F)
# '0b1111111'

bin(int('010101', 2))
# '0b10101'

bin(~0b11111111)  # ~255 -> -256
# '-0b100000000'

bin(0xCA)
# '0b11001010'

bin(0xFF)
# '0b11111111' -> 255

bin(0xF)
# '0b1111' -> 15

bin(0x100)
# '0b100000000' -> 256

bin(0x80)
# '0b10000000' -> 128

bin(0x40)
# '0b1000000' -> 64

bin(10)[2:], len(bin(10)[2:])
# ('1010', 4)

bin(255)[2:], len(bin(255)[2:])
# ('11111111', 8)

bin(100).count('1')
# 3

(0xFF00FF << 8) == (0xFF00FF * 2**8)  # (16711935 << 8) == (16711935 * 2**8)
# True

0b10101  # int('0b10101', 0)
# 21

0x100  # int('0x100', 16)
# 256

~0
# -1

0b100000000 - 0b100000001
# -1

0b_111_0101_0011
# 1875

hex(1_234_987)
# 0x12d82b

hex(sys.maxsize)
# '0x7fffffffffffffff'

''.join(
    map(str, (
        0xCA >> 7,
        (0xCA >> 6) % 2,
        (0xCA >> 5) % 2,
        (0xCA >> 4) % 2,
        (0xCA >> 3) % 2,
        (0xCA >> 2) % 2,
        (0xCA >> 1) % 2,
        0xCA % 2,
    )))
# '11001010'


def reverse_bits(x):
    inp_bits = bin(x)[2:]
    return f"{inp_bits} -> {inp_bits[::-1]}"


def add_by_bits_rec(i, j):
    assert i >= 0 and j >= 0
    uncommon_bits_from_both = i ^ j
    common_bits_from_both = i & j
    if common_bits_from_both == 0:
        return uncommon_bits_from_both
    return add_by_bits_rec(uncommon_bits_from_both, common_bits_from_both << 1)


def add_by_bits(a, b):
    assert a >= 0 and b >= 0
    while b:
        carry = a & b
        a ^= b
        b = carry << 1
    return a


def bits_rotate_left(byte):
    """
    Rotate bits left.
    """
    bit = byte & 0x80
    byte <<= 1
    if bit:
        byte |= 0x01
    byte &= 0xFF
    return byte


def bits_rotate_right(byte):
    """
    Rotate bits right.
    """
    byte &= 0xFF
    bit = byte & 0x01
    byte >>= 1
    if bit:
        byte |= 0x80
    return byte


def number_of_set_bits(i):
    # https://en.wikipedia.org/wiki/Hamming_weight
    assert 0 <= i < 0x100000000
    i -= ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24


def check_num_is_power_of_two(n):
    return n & (n - 1) == 0


def is_div_by_17(n):
    # true for any n of the form 2**k + 1 like 5, 9, 17, 33...
    if n == 0 or n == 17:
        return True
    elif n < 17:
        return False
    return is_div_by_17((n >> 4) - (n & 15))


def divide_by_bits(x, y):
    power_y = y
    power = 1
    loopCount = 0
    while power_y < x:
        power_y <<= 1
        power <<= 1
        loopCount += 1
    quotient = 0
    while power_y > 0:
        power_y >>= 1
        power >>= 1
        if x >= power_y:
            x -= power_y
            quotient += power
    print(f"loopCount = {2*loopCount}")
    return quotient


def power_by_bits(a, b):
    result = 1
    while b:
        if b & 1:
            result *= a
        b >>= 1
        a *= a
    return result


def find_position_of_msb(n):
    high = 31
    low = 0
    while (high - low) > 1:
        mid = (high + low) // 2
        mask_high = (1 << high) - (1 << mid)
        if (mask_high & n) > 0:
            low = mid
        else:
            high = mid
    print(f"{n} : MSB at {low}. Between {pow(2, low)} and {pow(2, low + 1)}")


def swap_bits(x, i, j):
    x_old = bin(x)
    low = (x >> i) & 1
    high = (x >> j) & 1
    if low ^ high:
        x ^= (1 << i) | (1 << j)
    return f"{x_old} -> {bin(x)}"


# https://catonmat.net/low-level-bit-hacks
def int_to_bin(num, bits=8):
    r = ''
    while bits:
        r += ('1' if num & 1 else '0')
        bits -= 1
        num >>= 1
    print(r)


def check_even_or_odd(i):
    """
    Bit Hack #1. Check if the integer is even or odd.
    """
    return 'even' if i & 1 == 0 else 'odd'


def test_nth_bit_is_set(i, n):
    """
    Bit Hack #2. Test if the n-th bit is set
    """
    return 'is set' if i & (1 << n) else 'is not set'


def set_nth_bit(i, n):
    """
    Bit Hack #3. Set the n-th bit.
    """
    return i | (1 << n)


def unset_nth_bit(i, n):
    """
    Bit Hack #4. Unset the n-th bit
    """
    return i & ~(1 << n)


def toggle_nth_bit(i, n):
    """
    Bit Hack #5. Toggle the n-th bit
    """
    return i ^ (1 << n)


def turn_off_rightmost_bit(i):
    """
    Bit Hack #6. Turn off the rightmost 1-bit
    """
    return i & (i - 1)


def isolate_rightmost_bit(i):
    """
    Bit Hack #7. Isolate the rightmost 1-bit
    """
    return i & (-i)


def right_propagate_rightmost_bit(i):
    """
    Bit Hack #8. Right propagate the rightmost 1-bit
    """
    return i | (i - 1)


def isolate_rightmost_0_bit(i):
    """
    Bit Hack #9. Isolate the rightmost 0-bit
    """
    return ~i & (i + 1)


def turn_rightmost_0_bit(i):
    """
    Bit Hack #10. Turn on the rightmost 0-bit
    """
    return i | (i + 1)
