import yaml

configDefaults = {
    "sizes": [
        "1024x768",
        "1920x1280",
        "1280x720"
    ],
    "border": {
        "size": 20,
        "color": "000"
    },
    "grid": {
        "1024x768": [3, 4],
        "": [5, 4]
    },
    "inclusions": 5
}


def load(configPath):
    """
    Load configuration
    """

    with open(configPath) as configFile:
        raw = configFile.read()
        return yaml.safe_load(raw)
