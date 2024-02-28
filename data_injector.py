from data_loader import data_name_to_list
from database.config import URI
from database.conn import mongo
from argparse import ArgumentParser, BooleanOptionalAction

project_home_path = "/Users/ysh/Dev/Python/mitsAI"

if __name__ == "__main__":
    mongo.init_app(uri=URI, port=27017)

    parser = ArgumentParser(description="this is mongoDB GridFS Based large-image-data injector")
    parser.add_argument('--path', "-p", type=str, default="/data", help="You must enter a relative path based on the "
                                                                        "project home directory.")
    parser.add_argument("--database", "-d", type=str, help="Database in MongoDB to store data")
    parser.add_argument("--subdirectory", '-s', action=BooleanOptionalAction, help="If you're going to inject a data "
                                                                                   "folder that has a lot of "
                                                                                   "subdirectories, you can use that "
                                                                                   "option to move all the data in the "
                                                                                   "subdirectories in batches.")

    args = parser.parse_args()
    if args.subdirectory:
        #TODO: 대용량 파일 처리 로직 만들기
    else:
        filename_list = data_name_to_list(project_home_path + args.path)

        mongo.connect(args.database)

        for filename in filename_list:
            with open(project_home_path + args.path + "/" + filename, 'rb') as f:
                res = mongo.gfs_upload(f, filename=filename)
                print("upload" + filename + "succeed")

        mongo.close()
