from dataclasses import dataclass, field


class SequenceMeta(type):

    def __new__(cls, clsname: str, superclasses: tuple, clsdict: dict):
        # stac = [clsdict.get(attr) for attr in clsdict if callable(clsdict[attr]) and not attr.startswith("__")]
        stac = [clsdict.get(attr) for attr in clsdict if not callable(clsdict[attr]) and not attr.startswith("__")]
        clsdict.update(stack=stac)
        return super().__new__(cls, clsname, superclasses, clsdict)


class Sequence(metaclass=SequenceMeta):
    a = 1
    b = 2
    c = 'hej'

    def run(self):
        for item in self.stack:
            print(item)

pass