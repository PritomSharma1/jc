import pymongo
from bson import ObjectId
from pymongo.collection import Collection
teleclient = pymongo.MongoClient('')

teledb = teleclient["mozikhjcbot"]
bot = teledb['bot']
user = teledb['user']
hch = teledb['hch']
ggh = teledb['ggh']
fyb = teledb['fyb']
gzpd = teledb['gzpd']
xgmz = teledb['xgmz']
xgjj = teledb['xgjj']
cji = teledb['cji']
fxi = teledb['fxi']
yhmfx = teledb['yhmfx']


def fanyibao(projectname, text, fanyi):
    fyb.insert_one({
        'projectname':projectname,
        'text': text,
        'fanyi': fanyi
    })
    
def jiancehao(projectname, uid, phone):
    hch.insert_one({
        'projectname': projectname,
        'uid': uid,
        'phone': phone
    })



def user_data(key_id, user_id, username, fullname, lastname, state, creation_time, last_contact_time):
    user.insert_one({
        'count_id': key_id,
        'user_id': user_id,
        'username': username,
        'fullname': fullname,
        'lastname': lastname,
        'state': state,
        'creation_time': creation_time,
        'last_contact_time': last_contact_time,
        'sign': 0,
        'USDT': 0

    })



if __name__ == '__main__':

    pass