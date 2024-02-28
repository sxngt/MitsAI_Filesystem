import os

from database.conn import mongo
from database.config import URI

if __name__ == "__main__":
    mongo.init_app(uri=URI, port=27017)

    # 싱글턴처럼 사용합시다...

    mongo.connect("chest_image")

    # with open('local_data/ID00426637202313170790466_91.jpg', 'rb') as f:
    #    res = mongo.gfs_upload(f, filename="chest1.jpg")


def data_name_to_list(folder_path: str) -> list:
    file_and_dirs = os.listdir(folder_path)
    return file_and_dirs