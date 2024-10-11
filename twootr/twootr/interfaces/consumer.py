from typing import TypeVar, Callable


T = TypeVar('T')
Consumer = Callable[[T], None]
