__all__ = (
    'seconds_to_str',
)

def to_str(number: int) -> str:
    if number < 10:
        return '0' + str(number)
    return str(number)

def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    s = seconds % 60
    m = seconds // (60) % 60
    h = seconds // (60*60) % 24
    d = seconds // (60*60*24)
    st = ''
    if d > 0:
        st += to_str(d) + 'd'
        st += to_str(h) + 'h'
        st += to_str(m) + 'm'
        st += to_str(s) + 's'
    elif h > 0:
        st += to_str(h) + 'h'
        st += to_str(m) + 'm'
        st += to_str(s) + 's'
    elif m > 0:
        st += to_str(m) + 'm'
        st += to_str(s) + 's'
    else:
        st += to_str(s) + 's'
    return st
