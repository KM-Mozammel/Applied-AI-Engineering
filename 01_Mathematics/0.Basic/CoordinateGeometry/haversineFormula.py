# For Earth coordinates, we use the Haversine formula instead of Euclidean distance, because Earth is spherical.
from math import radians, sin, cos, sqrt, atan2

def haversine(coord1, coord2):
    R = 6371  # Earth radius in km
    lat1, lon1 = map(radians, coord1)
    lat2, lon2 = map(radians, coord2)
    dlat, dlon = lat2-lat1, lon2-lon1
    a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
    c = 2*atan2(sqrt(a), sqrt(1-a))
    return R*c

dhaka = (23.8103, 90.4125)
chittagong = (22.3569, 91.7832)
print("Distance Dhaka-Chittagong:", haversine(dhaka, chittagong), "km")
