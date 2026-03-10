import json

DATABASE = "database.json"


def load_profiles():
    with open(DATABASE, "r") as f:
        return json.load(f)


def save_profiles(profiles):
    with open(DATABASE, "w") as f:
        json.dump(profiles, f, indent=4)


def add_profile(profile):
    profiles = load_profiles()
    profiles.append(profile)
    save_profiles(profiles)