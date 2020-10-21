import json

with open('data/darks.txt', 'r') as colour_file:
   darks = [x.strip() for x in colour_file.readlines()]

with open('data/lights.txt', 'r') as colour_file:
   lights = [x.strip() for x in colour_file.readlines()]

print(json.dumps({
    "size": ["1","2","3","4","5","6","7","8","9"],
    "origin":["[this_dark:#dark#]  [this_light:#light#] [this_size:#size#] #this_dark# and #this_light# 2x#this_size# threads per colour {img https://mitzi-del-bra.glitch.me/houndstooth.png?c1=#this_dark#&c2=#this_light#&size=#this_size#}"],
    "dark": darks,
    "light": lights
    }, indent=2))
