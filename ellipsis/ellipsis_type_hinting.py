from typing import Callable


def inject(func: Callable[..., int]) -> None:
  return func() + 5


print(inject(lambda: 4))


def foo(x: ...) -> None:
  return x + x


print(foo(2))
print(foo("e"))