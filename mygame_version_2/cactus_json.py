import json

cactus_1 = {'type': 'short', 'number': 1, 'x': 622, 'y': 275}
cactus_2 = {'type': 'short', 'number': 2, 'x': 1458, 'y': 228}
cactus_3 = {'type': 'short', 'number': 3, 'x': 2740, 'y': 276}
cactus_4 = {'type': 'small', 'number': 4, 'x': 220, 'y': 504}
cactus_5 = {'type': 'small', 'number': 5, 'x': 2340, 'y': 510}
cactus_6 = {'type': 'big', 'number': 6, 'x': 994, 'y': 726}
cactus_7 = {'type': 'big', 'number': 7, 'x': 1827, 'y': 685}
cactus_8 = {'type': 'long', 'number': 8, 'x': 435, 'y': 884}
cactus_9 = {'type': 'long', 'number': 9, 'x': 2548, 'y': 884}
cactus_10 = {'type': 'short', 'number': 10, 'x': 600, 'y': 1248}
cactus_11 = {'type': 'short', 'number': 11, 'x': 1460, 'y': 1248}
cactus_12 = {'type': 'short', 'number': 12, 'x': 2740, 'y': 1248}
cactus_13 = {'type': 'small', 'number': 13, 'x': 200, 'y': 1484}
cactus_14 = {'type': 'small', 'number': 14, 'x': 1060, 'y': 1484}
cactus_15 = {'type': 'small', 'number': 15, 'x': 2340, 'y': 1484}
cactus_16 = {'type': 'big', 'number': 16, 'x': 1824, 'y': 1706}
cactus_17 = {'type': 'long', 'number': 17, 'x': 408, 'y': 1862}
cactus_18 = {'type': 'long', 'number': 18, 'x': 1268, 'y': 1862}
cactus_19 = {'type': 'long', 'number': 19, 'x': 2546, 'y': 1862}

cactuses = [cactus_1, cactus_2, cactus_3, cactus_4, cactus_5,
            cactus_6, cactus_7, cactus_8, cactus_9, cactus_10,
            cactus_11, cactus_12, cactus_13, cactus_14, cactus_15,
            cactus_16, cactus_17, cactus_18, cactus_19]

with open('cactus.json', 'w') as f:
    json.dump(cactuses, f)
