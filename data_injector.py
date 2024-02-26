import data_loader
from database.config import URI
from database.conn import mongo

local_data_path = "/Users/ysh/Dev/Python/mitsAI/local_data/"
filename_list = dataloader.data_name_to_list(local_data_path)

mongo.init_app(uri=URI, port=27017)

mongo.connect("chest_image")

for filename in filename_list:
    with open(local_data_path + filename, 'rb') as f:
        res = mongo.gfs_upload(f, filename=filename)

mongo.close()

print(filename_list)
