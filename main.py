
from app.config import config
from app.method import vector_read, vector_rename_colums, vector_drop_except, Process



def main():

    path = "C:\\michal\\gisat\\projects\\Cure\\app\\app06\\EL004L1_IRAKLEIO_UA2018_v013.gpkg"

    process = Process()
    process.add_method(vector_read)
    process.add_method(vector_rename_colums, {'map': config.input.urbanAtlas.columnNames.reverse})
    process.add_method(vector_drop_except, {'keep': config.input.urbanAtlas.columnNames.keys})
    res = process(path)




    pass

if __name__ == '__main__':
    main()
