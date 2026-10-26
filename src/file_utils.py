"""파일 관련 유틸 함수 모음."""


def read_lines(path: str) -> list[str]:
    """파일을 줄 단위로 읽어 줄바꿈을 뺀 문자열 리스트로 반환한다.

    >>> import os, tempfile
    >>> with tempfile.TemporaryDirectory() as d:
    ...     p = os.path.join(d, "sample.txt")
    ...     with open(p, "w", encoding="utf-8") as f:
    ...         _ = f.write("a\\nb\\n")
    ...     read_lines(p)
    ['a', 'b']
    """
    with open(path, encoding="utf-8") as f:
        return f.read().splitlines()
