# Saturn is missing from the planetList
# Insert it into the correct position

planetList = ["Mercury","Venus","Earth","Mars","Jupiter","Uranus","Neptune"]
planet = planetList[:5] + ["Saturnus"] + planetList[5:]

print(planet)