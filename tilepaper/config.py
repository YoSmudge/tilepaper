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


def mergedict(a, b, path=None):
    """
    Dictionary merge
    http://stackoverflow.com/a/7205107/744180
    """

    path = [] if path is None else path
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                mergedict(a[key], b[key], path + [str(key)])
        else:
            a[key] = b[key]
    return a


def load(configPath):
    """
    Load configuration
    """

    with open(configPath) as configFile:
        raw = configFile.read()
        loadedConfig = yaml.safe_load(raw)
        return mergedict(loadedConfig, configDefaults)
