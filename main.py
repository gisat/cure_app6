
from app.config import config
from app.method import VectorRead, VectorColumnsRename, VectorDropColumns
from app.base import Sequence



def main():

    class UrbanAtlasPreprocess(Sequence):
        process1 = VectorRead()
        process2 = VectorColumnsRename(mapping=config.input.urbanAtlas.columnNames.reverse)
        process3 = VectorDropColumns(colums=config.input.urbanAtlas.columnNames.keys, how='keep')

    path = "C:\\michal\\gisat\\projects\\Cure\\app\\app06\\EL004L1_IRAKLEIO_UA2018_v013.gpkg"
    preproces = UrbanAtlasPreprocess()
    preproces(path)

if __name__ == '__main__':
    main()
