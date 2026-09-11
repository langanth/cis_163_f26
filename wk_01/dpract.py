

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
# print(drivers)
print(drivers["Valtteri Bottas"])
try:
    print(drivers['Alex Albon'])
except:
    print('driver not found')

# number = drivers.get('Alex Albon')
number = drivers.get('Alex Albon', -1)
print(number)

print()
for k in drivers:
    print(k)

print()
for k in drivers.keys():
    print(k)

print()
for v in drivers.values():
    print(v)

print()
for k, v in drivers.items():
    print(k, v)

print()
for i in drivers.items():
    print(i)

