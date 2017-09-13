
queue = [
	{ 'name': 'Amanda', 'alcohol': 10, 'guns': 1 },
	{ 'name': 'Tibi', 'alcohol': 0, 'guns': 0 },
	{ 'name': 'Dolores', 'alcohol': 0, 'guns': 1 },
	{ 'name': 'Wade', 'alcohol': 1, 'guns': 1 },
	{ 'name': 'Anna', 'alcohol': 10, 'guns': 0 },
	{ 'name': 'Rob', 'alcohol': 2, 'guns': 0 },
	{ 'name': 'Joerg', 'alcohol': 20, 'guns': 0 }
]

# Queue of festivalgoers at entry
# no. of alcohol units 
# no. of guns

# Create a security_check function that returns a list of festivalgoers who can enter the festival

# If guns are found, remove them and put them on the watchlist (only the names)
# If alcohol is found confiscate it (set it to zero and add it to security_alchol_loot) and let them enter the festival




def unitsCounter():
    security_alcohol_loot = 0
    guns_units = 0
    for n in range(len(queue)):
        security_alcohol_loot += queue[n]['alcohol']
        guns_units += queue[n]['guns']
    print("Alkohol units: ", security_alcohol_loot)
    print("Guns units: ", guns_units)

def security_check():
    watchlist = []
    for n in range(len(queue)):
        if queue[n]['guns'] == 0:
            queue[n]['alcohol'] = 0
            watchlist+=[queue[n]['name'],queue[n]['alcohol']]
            
    print(watchlist)
unitsCounter()
security_check()