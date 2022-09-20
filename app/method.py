from abc import ABC, abstractmethod
from pydantic import BaseModel, PrivateAttr, Field
from typing import Callable, Any, Union, List, Optional, Literal
import geopandas
from geopandas import GeoDataFrame
from functools import wraps


# decorators
def set_status_after_execution(process):
    """siple decorator that set the status of the process after the execution of the process"""
    @wraps(process)
    def set_status(*args, **kwargs):
        result = process(*args, **kwargs)
        process.is_executed = True
        return result
    return set_status



@set_status_after_execution
class Process(BaseModel, ABC):
    _is_executed: bool = PrivateAttr(default=False)
    """Abstrac factory for processes"""

    @property
    def is_executed(self) -> bool:
        return self._is_executed

    @is_executed.setter
    def is_executed(self, status: bool) -> None:
        self._is_executed = status

    @classmethod
    def __call__(self, *args, **kwargs):
        pass


@set_status_after_execution
class VectorRead(Process):
    """open the vector file. Supported formats correspond to the all formats that can be open by geopandas. Returns
    GeoDataFrame"""

    def __call__(self, path) -> GeoDataFrame:
        try:
            return geopandas.read_file(path)
        except Exception as e:
            print(e)


@set_status_after_execution
class VectorColumnsRename(Process):
    """Rename the input Geodataframe based on the mapping dictionary dict[str,str] where kyes are original names and
    values target names"""
    mapping: dict

    def __call__(self, geodata) -> GeoDataFrame:
        return geodata.rename(columns=self.mapping)



@set_status_after_execution
class VectorDropColumns(Process):
    """Class drop the from the input GeoDataFrame. Parmater colums list[str] or str specified the target columns. Based
    on the selected method columns are drop or keep in resulting GeoDataFrame """
    colums: List[str]
    how: Literal['keep', 'drop'] = Field(default='keep')

    def __call__(self, geodata) -> GeoDataFrame:
        if self.how == 'keep':
            return geodata[[key for key in self.colums]]
        elif self.how == 'drop':
            return geodata.drop(self.colums, axis=1)


