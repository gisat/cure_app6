from abc import ABC, abstractmethod
from dataclasses import field, dataclass
from typing import Callable, Any, Union, List, Optional, Literal
import geopandas
from geopandas import GeoDataFrame
from functools import partial


class Process(ABC):

    @classmethod
    def __call__(self, *args, **kwargs):
        pass


@dataclass
class VectorRead(Process):

    def __call__(self, path):
        return geopandas.read_file(path)

@dataclass
class VectorColumsRename(Process):
    map: dict

    def __call__(self, geodata):
        return geodata.rename(columns=self.map)

@dataclass
class VectorDropColumns(Process):
    colums: List[str]
    how: Literal['keep', 'drop'] = field(default='keep')

    def __call__(self, geodata):
        if self.how == 'keep':
            return geodata[[key for key in self.colums]]
        elif self.how == 'drop':
            return geodata.drop(self.colums, axis=1)


# @dataclass
# class Process:
#     methods: List[Callable] = field(default_factory=list)
#
#     def add_method(self, func: Callable, params: Optional[Any] = None)-> None:
#         if params:
#             self.methods.append(partial(func, **params))
#         else:
#             self.methods.append(func)
#
#     def __call__(self, value) -> Any:
#         current = value
#         for method in self.methods:
#             current = method(current)
#         return current
