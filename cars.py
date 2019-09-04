showroom = set()

showroom.update(["Mustang", "Impala", "Charger", "Thunderbird"])
showroom.add("Mustang")
showroom.update(["Accord", "Altima"])
showroom.discard("Accord")

print(len(showroom))
print(showroom)

junkyard = {"Prius", "Pilot", "Camry", "Altima", "Charger", "Impala"}

same_cars = showroom.intersection(junkyard)
print(same_cars)

new_showroom = showroom.union(junkyard)
print(new_showroom)

new_showroom.discard("Camry")
new_showroom.discard("Prius")
print(new_showroom)