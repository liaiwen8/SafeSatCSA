from skyfield.api import load, wgs84

url = 'https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle'
satellites = load.tle_file(url)
print('Loaded', len(satellites), 'satellites')

inS = int(input("serial: "))

by_number = {sat.model.satnum: sat for sat in satellites}
satellite = by_number[inS]
print(satellite)
ts = load.timescale()
t = ts.now()
geocentric = satellite.at(t)
print(geocentric.position.km)
