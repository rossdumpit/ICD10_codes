import csv
import os
import sys

DATASETS = {}

def resource_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.abspath("."), filename)


FILES = {
    "act_engaged": resource_path("act_engaged.csv"),
    "existing_cause": resource_path("existing_cause.csv"),
    "place_of_injury": resource_path("place_of_injury.csv")
}


def load_data():
    for name, path in FILES.items():
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            DATASETS[name] = list(reader)