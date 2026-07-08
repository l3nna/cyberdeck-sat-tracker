from skyfield.api import load, wgs84
from pathlib import Path
import time


DATA_FILE = Path("data/stations.tle")


# Zagreb, Croatia
OBSERVER = wgs84.latlon(
    45.8150,
    15.9819,
    elevation_m=150
)


def get_iss():

    satellites = load.tle_file(str(DATA_FILE))

    for satellite in satellites:

        if "ISS" in satellite.name:
            return satellite

    return None



def live_track():

    print("[INFO] Loading ISS...")

    iss = get_iss()

    if iss is None:
        print("[ERROR] ISS not found")
        return


    ts = load.timescale()


    print("[OK] Live observer tracking started")


    while True:

        now = ts.now()


        # Satellite position
        satellite_position = iss.at(now)


        # Observer position
        observer_position = OBSERVER.at(now)


        # Difference between them
        difference = satellite_position - observer_position


        # Look angles
        alt, az, distance = difference.altaz()


        # Clear terminal
        print("\033c", end="")


        print("==============================")
        print("   LIVE SATELLITE TRACKER")
        print("==============================")


        print("TARGET:")
        print(iss.name)

        print()

        print("LOCATION:")
        print("Zagreb, Croatia")

        print()

        print("DISTANCE:")
        print(round(distance.km, 2), "km")

        print()

        print("ELEVATION:")
        print(round(alt.degrees, 2), "degrees")

        print()

        print("AZIMUTH:")
        print(round(az.degrees, 2), "degrees")

        print()

        if alt.degrees > 0:
            print("STATUS:")
            print("VISIBLE ABOVE HORIZON")
        else:
            print("STATUS:")
            print("BELOW HORIZON")


        print("==============================")


        time.sleep(1)



if __name__ == "__main__":
    live_track()
