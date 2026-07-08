from skyfield.api import load
from pathlib import Path
import time


DATA_FILE = Path("data/stations.tle")


def get_iss():

    satellites = load.tle_file(str(DATA_FILE))

    for satellite in satellites:

        if "ISS" in satellite.name:
            return satellite

    return None



def track_live():

    print("[INFO] Loading ISS...")

    iss = get_iss()

    if iss is None:
        print("[ERROR] ISS not found")
        return


    ts = load.timescale()


    print("[OK] Tracking started")
    print("-----------------------------")


    while True:

        now = ts.now()

        position = iss.at(now)

        subpoint = position.subpoint()


        latitude = subpoint.latitude.degrees
        longitude = subpoint.longitude.degrees
        altitude = subpoint.elevation.km


        # Clear terminal
        print("\033c", end="")


        print("==============================")
        print("       SATELLITE TRACKER")
        print("==============================")

        print("TARGET:")
        print(iss.name)

        print()

        print("LATITUDE:")
        print(round(latitude, 4), "degrees")

        print()

        print("LONGITUDE:")
        print(round(longitude, 4), "degrees")

        print()

        print("ALTITUDE:")
        print(round(altitude, 2), "km")

        print()

        print("STATUS:")
        print("TRACKING")

        print("==============================")


        time.sleep(1)



if __name__ == "__main__":
    track_live()
