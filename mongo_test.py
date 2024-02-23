import pymongo
from urllib.parse import quote_plus

host = "mits.iptime.org"
user = "mits"
password = "ehql"
URI = "mongodb://%s:%s@%s" % (
    quote_plus(user), quote_plus(password), host
)

conn = pymongo.MongoClient(
    host=URI,
    port=27017,
    document_class=dict,
    tz_aware=False,
    connect=True
)

chest_ct = conn.get_database(name="chest_ct")
metadata = chest_ct.get_collection(name="metadata")

metadata.insert_one(document={
    "name": "ysh",
    "test": "test"
})

print(metadata)
