import redis
import json
import time
from redis.cluster import RedisCluster as Redis

cluster_redis = Redis(host='0.0.0.0', port=8401)

with open('20mb.json', 'r') as f:
    data = json.load(f)

start_time = time.time()
cluster_redis.set('set_key', json.dumps(data))
end_time = time.time()
set_time = end_time - start_time
print("Set Time: ", set_time)


start_time = time.time()
retrieved_data = cluster_redis.get('set_key')
end_time = time.time()
get_time = end_time - start_time
print("Get Time:", get_time)



start_time = time.time()
for i in range(109000):
    cluster_redis.hset(f'hset_key{i}',mapping=data[i])
end_time = time.time()
set_time = end_time - start_time
print("Hset Time: ", set_time)


start_time = time.time()
for i in range(109000):
    cluster_redis.hget(f'hset_key{i}', key= 'name')
end_time = time.time()
get_time = end_time - start_time
print("Hget Time:", get_time)

start_time = time.time()
for i in range(109000):
    cluster_redis.zadd('zset_key', {json.dumps(data[i]):i})
end_time = time.time()
set_time = end_time - start_time
print("Zset Time: ", set_time)


start_time = time.time()
retrieved_data = cluster_redis.zrange('zset_key', 0, -1, withscores=True)
end_time = time.time()
get_time = end_time - start_time
print("Retrieved Data[1777]:", retrieved_data[1777])
print("ZRange Time:", get_time)

start_time = time.time()
for i,d in enumerate(data):
    if i%2 ==1:
        cluster_redis.rpush('list_key',json.dumps(d))
    else:
        cluster_redis.lpush('list_key',json.dumps(d))
end_time = time.time()
set_time = end_time - start_time
print("List Set Time: ", set_time)


start_time = time.time()
retrieved_data = cluster_redis.lrange('list_key', 0, -1)
end_time = time.time()
get_time = end_time - start_time
print("Retrieved Data[1777]:", retrieved_data[1777])
print("List Get Time:", get_time)


