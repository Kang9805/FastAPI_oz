
my_int: int = 1
my_str: str = "abc"

my_list: list[str] = ["abc", "def"]

my_tuple: tuple[str, str] = ("abc", "def")

my_dict: dict[str, int] = {"a": 1, "b": 2}


def add(a: int, b: int) -> int:
    return a + b

print(1 + add(a=1, b=1))