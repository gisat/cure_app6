from dataclasses import dataclass, field
from functools import partial
from typing import Callable, Optional, Any
from functools import wraps

from app.method import Process


class SequenceMeta(type):
    def __new__(cls, clsname: str, superclasses: tuple, clsdict: dict):
        stac = [value for attr, value in clsdict.items() if isinstance(value, Process)]
        clsdict.update(stac=stac)
        return super().__new__(cls, clsname, superclasses, clsdict)


class Sequence(metaclass=SequenceMeta):

    def __call__(self, value) -> Any:
        current = value
        for method in self.stac:
            current = method(current)
        return current