import requests
from pathlib import Path
from skyfield.api import load

TLE_URL = "https://celestrak.org/NORAD/elements/stations.txt"
DATA_FILE = Path("data/stations.tle")


def download_tle():
    print("[INFO] Downloading TLE data...")

    response = requests.get(TLE_URL)

    if response.status_code == 200:
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        DATA_FILE.write_text(response.text)
        print("[OK] TLE data saved")
    else:
        print("[ERROR] Failed to download TLE")


def load_satellites():
    print("[INFO] Loading satellites...")

    satellites = load.tle_file(str(DATA_FILE))

    print(f"[OK] Loaded {len(satellites)} satellites")

    for sat in satellites:
        print(" -", sat.name)

    return satellites


if __name__ == "__main__":
    download_tle()
    load_satellites()
