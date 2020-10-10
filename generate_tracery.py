import json

with open('data/darks.txt', 'r') as colour_file:
   darks = [x.strip() for x in colour_file.readlines()]

with open('data/lights.txt', 'r') as colour_file:
   lights = [x.strip() for x in colour_file.readlines()]

print(json.dumps({
    "origin":["[this_dark:#dark#]  [this_light:#light#] #this_dark# and #this_light# {img https://mitzi-del-bra.glitch.me/houndstooth.png?c1=#this_dark#&c2=#this_light#}"],
    "dark": darks,
    "light": lights
    }, indent=2))
