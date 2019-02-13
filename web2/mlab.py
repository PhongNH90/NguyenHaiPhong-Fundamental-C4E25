import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds147420.mlab.com:47420/c4e25-web2

host = "ds147420.mlab.com"
port = 47420
db_name = "c4e25-web2"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())