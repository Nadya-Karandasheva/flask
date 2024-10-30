from datetime import datetime
import time
from pymongo import MongoClient
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redishost', port=6379)

client = MongoClient("mongodb://mongohost:27017/")
db = client.counter_db
counters = db.counters

def get_hit_count():
    retries = 5
    while True:
        try:
            # Увеличение значения в Redis
            count = cache.incr('hits')
            # Сохранение в Mongo
            counters.insert_one({"Count": count, "Visit time": datetime.now()})
            return count
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

@app.route('/database')
def show():
    data = counters.find({})

    result = []

    for element in data:
        result.append(str(element) + "</br>")
    
    return str(result)
