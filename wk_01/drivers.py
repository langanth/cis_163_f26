drivers = {
    "Kimi Antonelli": 12,
    "Lewis Hamilton": 44,
    "Max Verstappen": 3,
    "Lando Norris": 4
}

print(drivers)
drivers["Lando Norris"] = 1
# print(drivers)
drivers["Valtteri Bottas"] = 77
print('='*25)
for k in drivers.keys():
    drivers[k] = {"Number": drivers[k], "Podiums": [0, 0, 0]}

print(drivers)

for k in drivers:
    print(drivers[k]["Number"])