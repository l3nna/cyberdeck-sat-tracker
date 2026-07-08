from skyfield.api import load, EarthSatellite
from pathlib import Path
from datetime import datetime


DATA_FILE = Path("data/stations.tle")


def get_iss():

    satellites = load.tle_file(str(DATA_FILE))

    for satellite in satellites:
        if "ISS" in satellite.name:
            return satellite

    return None


def track_satellite():

    print("[INFO] Loading ISS...")

    iss = get_iss()

    if iss is None:
        print("[ERROR] ISS not found")
        return


    ts = load.timescale()

    now = ts.now()

    position = iss.at(now)

    subpoint = position.subpoint()


    print("==============================")
    print(" SATELLITE TRACKING")
    print("==============================")

    print("TARGET:", iss.name)

    print("Latitude:",
          round(subpoint.latitude.degrees, 3))

    print("Longitude:",
          round(subpoint.longitude.degrees, 3))

    print("Altitude:",
          round(subpoint.elevation.km, 2),
          "km")


if __name__ == "__main__":
    track_satellite()
