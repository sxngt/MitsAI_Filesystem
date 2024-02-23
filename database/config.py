from urllib.parse import quote_plus

host = "mits.iptime.org"
user = "mits"
password = "ehql"
URI = "mongodb://%s:%s@%s" % (
    quote_plus(user), quote_plus(password), host
)