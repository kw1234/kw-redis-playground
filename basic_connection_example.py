"""Basic connection example.
"""

import redis

r = redis.Redis(
    host='redis-15201.c15.us-east-1-2.ec2.redns.redis-cloud.com',
    port=15201,
    decode_responses=True,
    username="default",
    password="SCvjOApt6Ll9PW17XLSk0SFVodZhIZ8O",
)

success = r.set('foo', 'bar')
# True

result = r.get('foo')
print(result)
# >>> bar

