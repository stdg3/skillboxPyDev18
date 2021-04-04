# -*- codding: utf-8 -*-

sities = {
    "moscow": (500, 370),
    "london": (510,510),
    "paris": (480,480)
}

ml = (sities["moscow"][0] - sities["london"][0]) **2 + (sities["moscow"][1] - sities["london"][1]) ** 2
mp = (sities["moscow"][0] - sities["paris"][0]) **2 + (sities["moscow"][1] - sities["paris"][1]) ** 2
lp = (sities["london"][0] - sities["paris"][0]) **2 + (sities["london"][1] - sities["paris"][1]) ** 2

distance = {
    "mos-lon": ml,
    "mos-par": mp,
    "lon-par": lp
}

#print(sities["moscow"][1])
print("Distances:\nMoscow-London:", distance["mos-lon"], "\nMoscow-Paris:", distance["mos-par"], "\nParis-London:", distance["lon-par"])

# Distances:
# Moscow-London: 19700
# Moscow-Paris: 12500
# Paris-London: 1800
