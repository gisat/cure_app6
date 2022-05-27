import pytest
from app.base import  SequenceMeta
from app.method import sum


def test_sequnece():
    class MySequnece(metaclass=SequenceMeta):
        a = sum(1, 2)
        b = sum(2, 4)

    print('baf')
    s = MySequnece()
    assert s.run()
    pass
    print('baf')
