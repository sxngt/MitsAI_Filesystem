import os

from database.conn import mongo
from database.config import URI

if __name__ == "__main__":
    mongo.init_app(uri=URI, port=27017)

    # 싱글턴처럼 사용합시다...

    mongo.connect("Finger_motion_data")
    mongo.gfs_download(output_file_path="/Users/ysh/Dev/Python/mitsAI/download/15FRU_9 - 9of20.mp4", filename="15FRU_9 - 9of20.mp4")
    mongo.close()


def data_name_to_list(folder_path: str) -> list:
    file_and_dirs = os.listdir(folder_path)
    return file_and_dirs