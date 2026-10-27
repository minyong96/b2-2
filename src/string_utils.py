"""문자열 관련 유틸 함수 모음."""


def reverse_string(text: str) -> str:
    """문자열을 뒤집어 반환한다.

    >>> reverse_string("abc")
    'cba'
    """
    return text[::-1]
