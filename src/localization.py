# Built-in
import json
from pathlib import Path
# Local
import envvars

# White-Rabbit/src/localization.py
WHITE_RABBIT_DIR = Path(__file__).parent.parent

# Localization
DEFAULT_LOCALIZATION = envvars.DEFAULTS["LANGUAGE"]
LOCALIZATION_DIR = WHITE_RABBIT_DIR / "localization"

LOCALIZATIONS = {
    "en": "english.json",
    "fr": "french.json",
}

LANGUAGE_KEY = envvars.get_env_var("LANGUAGE")

localization_file = LOCALIZATION_DIR / LOCALIZATIONS[LANGUAGE_KEY]

print(f"Loading localization data ({LANGUAGE_KEY})... ", end="")

LOCALIZATION_DATA = None
with open(localization_file, encoding='utf-8') as f:
    LOCALIZATION_DATA = json.load(f)

print("Done!")
