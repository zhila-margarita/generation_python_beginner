"""You are given some string where you need to find its middle character(s). The string may contain one word, a few symbols or a whole sentence. If the length of the string is even, then you should return two middle characters, but if the length is odd, return just one. For more details look at the Example.

If you want to practice more with the similar case, try Median mission.

Input: A string (str).

https://py.checkio.org/en/mission/middle-characters/"""


def middle(text: str) -> str:
    length = len(text)

    return (text[length // 2] if length % 2 == 1 else text[length // 2 - 1 : length // 2 + 1])


print(middle("корова"))
