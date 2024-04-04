import redis
import json
import time

r = redis.StrictRedis(host='0.0.0.0', port=8400, db=0)


with open('20mb.json', 'r') as f:
    data = json.load(f)

start_time = time.time()
r.set('set_key', json.dumps(data))
end_time = time.time()
set_time = end_time - start_time
print("Set Time: ", set_time)


start_time = time.time()
retrieved_data = r.get('set_key')
end_time = time.time()
get_time = end_time - start_time
print("Get Time:", get_time)



start_time = time.time()
for i in range(109000):
    r.hset(f'hset_key{i}',mapping=data[i])
end_time = time.time()
set_time = end_time - start_time
print("Hset Time: ", set_time)


start_time = time.time()
for i in range(109000):
    r.hget(f'hset_key{i}', key= 'name')
end_time = time.time()
get_time = end_time - start_time
print("Hget Time:", get_time)

start_time = time.time()
for i in range(109000):
    r.zadd('zset_key', {json.dumps(data[i]):i})
end_time = time.time()
set_time = end_time - start_time
print("Zset Time: ", set_time)


start_time = time.time()
retrieved_data = r.zrange('zset_key', 0, -1, withscores=True)
end_time = time.time()
get_time = end_time - start_time
print("Retrieved Data[1777]:", retrieved_data[1777])
print("ZRange Time:", get_time)

start_time = time.time()
for i,d in enumerate(data):
    if i%2 ==1:
        r.rpush('list_key',json.dumps(d))
    else:
        r.lpush('list_key',json.dumps(d))
end_time = time.time()
set_time = end_time - start_time
print("List Set Time: ", set_time)


start_time = time.time()
retrieved_data = r.lrange('list_key', 0, -1)
end_time = time.time()
get_time = end_time - start_time
print("Retrieved Data[1777]:", retrieved_data[1777])
print("List Get Time:", get_time)


