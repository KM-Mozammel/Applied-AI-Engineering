# Formula: 
#     new_x = x*cos(θ) - y*sin(θ)
#     new_y = x*sin(θ) + y*cos(θ)

import math

x = 1
y = 0

angle = math.radians(90)

new_x = x*math.cos(angle) - y*math.sin(angle)
new_y = x*math.sin(angle) + y*math.cos(angle)

print(round(new_x))
print(round(new_y))