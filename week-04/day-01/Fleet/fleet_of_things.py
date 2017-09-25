from fleet import Fleet
from thing import Thing

fleet = Fleet()
# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch
milk = Thing("Get milk")
remove_obs = Thing("Remove the obstacles")
stand_up = Thing("Satnd up")
eat = Thing("Eat lunch")

stand_up.complete()
eat.complete()

fleet.add(milk)
fleet.add(remove_obs)
fleet.add(stand_up)
fleet.add(eat)

print(fleet)