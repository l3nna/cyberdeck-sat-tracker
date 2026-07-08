from skyfield.api import load, wgs84
from pathlib import Path


DATA_FILE = Path("data/stations.tle")


OBSERVER = wgs84.latlon(
    44.80,
    20.50,
    elevation_m=200
)


def get_iss():

    satellites = load.tle_file(str(DATA_FILE))

    for satellite in satellites:

        if "ISS" in satellite.name:
            return satellite

    return None



def track_from_observer():

    print("[INFO] Loading ISS...")

    iss = get_iss()

    if iss is None:
        print("[ERROR] ISS not found")
        return


    ts = load.timescale()

    now = ts.now()


    # Calculate ISS position at current time
    satellite_position = iss.at(now)


    # Calculate observer position at the same time
    observer_position = OBSERVER.at(now)


    # Vector from observer to satellite
    difference = satellite_position - observer_position


    # Get viewing information
    alt, az, distance = difference.altaz()


    print("==============================")
    print("       OBSERVER TRACKER")
    print("==============================")


    print("TARGET:")
    print(iss.name)

    print()

    print("YOUR LOCATION:")
    print("Zagreb / Croatia")

    print()

    print("DISTANCE:")
    print(round(distance.km, 2), "km")

    print()

    print("ELEVATION:")
    print(round(alt.degrees, 2), "degrees")

    print()

    print("AZIMUTH:")
    print(round(az.degrees, 2), "degrees")

    print("==============================")


if __name__ == "__main__":
    track_from_observer()
