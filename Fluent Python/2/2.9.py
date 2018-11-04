from collections import namedtuple

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),   # <1>
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

field='name country population coordinates'.split()
City=namedtuple('City',field)
a=City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print (a.name)
print (a.country)
pass