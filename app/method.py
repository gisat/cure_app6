from abc import ABC, abstractmethod
from dataclasses import field, dataclass
from typing import Callable, Any, Union, List, Optional
import geopandas
from geopandas import GeoDataFrame
from functools import partial


def vector_read(path: str) -> GeoDataFrame:
    return geopandas.read_file(path)


def vector_rename_colums(geodata: GeoDataFrame, map: dict) -> GeoDataFrame:
    return geodata.rename(columns=map)


def vector_drop_except(geodata: GeoDataFrame, keep: list) -> GeoDataFrame:
    return geodata[[key for key in keep]]


@dataclass
class Process:
    methods: List[Callable] = field(default_factory=list)

    def add_method(self, func: Callable, params: Optional[Any] = None)-> None:
        if params:
            self.methods.append(partial(func, **params))
        else:
            self.methods.append(func)

    def __call__(self, value) -> Any:
        current = value
        for method in self.methods:
            current = method(current)
        return current
