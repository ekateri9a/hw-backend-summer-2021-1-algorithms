from posixpath import split
import re
from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    min_w, max_w = None, None
    p = re.compile(r'\w+')
    res = p.findall(text)
    if len(res)>0:
        min_w = min(res, key=len)
        max_w = max(res, key=len)
    return min_w, max_w
