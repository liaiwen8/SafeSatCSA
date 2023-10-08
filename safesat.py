from numpy import number
from skyfield.api import load, wgs84
from numpy.linalg import norm
from skyfield.api import EarthSatellite

# Function to input TLE data from the user
def get_user_tle_input():
    tle_line1 = input("Enter TLE Line 1: ")
    tle_line2 = input("Enter TLE Line 2: ")
    return tle_line1, tle_line2

activeURL = 'https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle'
analystURL = 'https://celestrak.org/NORAD/elements/gp.php?GROUP=analyst&FORMAT=tle'
satellites = load.tle_file(activeURL, filename='sat.php')
analyst = load.tle_file(analystURL, filename='ana.php')
print('Loaded', len(satellites), 'satellites')
print('Loaded', len(analyst), 'A')

inA = int(input("serialA (Enter 0 to input your own TLE data): "))
inB = int(input("serialB (Enter 0 to input your own TLE data): "))

num = {sat.model.satnum: sat for sat in satellites}

if inA == 0:
  line1, line2 = get_user_tle_input()
  ts = load.timescale()
  satellite = EarthSatellite(line1, line2, "SATELLITE A", ts)
  print(satellite)
else:
    satellite = num[inA]

if inB == 0:
  line1, line2 = get_user_tle_input()
  ts = load.timescale()
  debris = EarthSatellite(line1, line2, "SATELLITE B", ts)
  print(debris)
else:
  debris = num[inB]

print(satellite)
print(debris)

t = load.timescale(delta_t=0).now()

for i in range(0, 1000, 10):
    t = load.timescale(delta_t=i).now()
    geoS = satellite.at(t)
    geoD = debris.at(t)
    print(geoS.position.km)
    print(geoD.position.km)

    # Calculate the position vectors and their difference
    position_S = geoS.position.km
    position_D = geoD.position.km
    position_difference = position_S - position_D

    # Calculate the distance between the objects
    distance_km = norm(position_difference)

    if distance_km < 5:
        print("COLLISION")
