from collections import namedtuple
field='name country population coordinates'.split()
City=namedtuple('City',field)
latlong=namedtuple('LatLong','lat long')
delhi_data=('Delhi NCR','IN',21.935,latlong(28.1,77.2))
delhi=City(*delhi_data)
pass

