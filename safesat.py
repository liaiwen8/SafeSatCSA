from skyfield.api import load, EarthSatellite
from numpy.linalg import norm

# Function to input TLE data from the user
def get_user_tle_input():
    tle_line1 = input("Enter TLE Line 1: ")
    tle_line2 = input("Enter TLE Line 2: ")
    return tle_line1, tle_line2

def compute_collisions():  
  activeURL = 'https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle'
  satellites = load.tle_file(activeURL, filename='sat.php')
  print('Loaded', len(satellites), 'satellites')

  inA = int(input("Serial number of satellite to track (Enter 0 to input your own TLE data): "))

  if inA == 0:
      line1, line2 = get_user_tle_input()
      ts = load.timescale()
      satellite = EarthSatellite(line1, line2, "Custom Satellite", ts)
      print(satellite)
  else:
      num = {sat.model.satnum: sat for sat in satellites}
      satellite = num.get(inA)

  if satellite is None:
      print("Invalid satellite serial number or TLE data.")
  else:
      t = load.timescale(delta_t=0).now()

      for i in range(10):
          t = load.timescale(delta_t=i).now()
          geoS = satellite.at(t)
          print(f"Position of Satellite at {t.utc_datetime()}: {geoS.position.km}")

          for debris in satellites:
              geoD = debris.at(t)
              position_S = geoS.position.km
              position_D = geoD.position.km
              position_difference = position_S - position_D

              distance_km = norm(position_difference)

              if distance_km < 5:
                  print("COLLISION with", debris.name)
