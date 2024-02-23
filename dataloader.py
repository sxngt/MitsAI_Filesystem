from database.conn import mongo
from database.config import URI

mongo.init_app(uri=URI, port=27017)

#싱글턴처럼 사용합시다...

mongo.connect("chest_image")

#with open('local_data/ID00426637202313170790466_91.jpg', 'rb') as f:
#    res = mongo.gfs_upload(f, filename="chest1.jpg")
#print(res)

mongo.gfs_download(output_file_path="/Users/ysh/Dev/Python/mitsAI/download/chest1.jpg", filename="chest1.jpg")
mongo.close()

