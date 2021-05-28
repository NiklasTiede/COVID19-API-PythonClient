"""List of API endpoints `covid19pyclient` knows about."""

BASE_URL = "https://api.corona-zahlen.org/"

# epidemiological metrics served by the API (frozen-incidents have been left out to simplify the Wrapper):
TYPES = [
    'cases',      # number of infected people
    'incidence',  # number of newly infected people (per 100.000; avg per week)
    'deaths',     # number of deceased patients
    'recovered',  # number of recovered patients
]

STATES = [  # two-letter codes for the federal states of germany
    'BW',  # Baden-Württemberg
    'BY',  # Bayern
    'BE',  # Berlin
    'BB',  # Brandenburg
    'HB',  # Bremen
    'HH',  # Hamburg
    'HE',  # Hessen
    'MV',  # Mecklenburg-Vorpommern
    'NI',  # Niedersachsen
    'NW',  # Nordrhein-Westfalen
    'RP',  # Rheinland-Pfalz
    'SL',  # Saarland
    'SN',  # Sachsen
    'ST',  # Sachsen-Anhalt
    'SH',  # Schleswig-Holstein
    'TH',  # Thüringen
]

API_PATH = {  # API endpoints (full path: https://api.corona-zahlen.org/germany/history/deaths )
    "germany_accumulated":           "germany",
    "germany_age_groups":            "germany/age-groups",
    "germany_history":               "germany/history/{types}",
    "germany_history_paginated":     "germany/history/{types}/{days}",

    "states_accumulated":            "states/",
    "states_history":                "states/{state}",
    "states_by_agegroups":           "states/age-groups",
    "states_all_by_agegroups":       "states/{state}/age-groups",

    "districts_accumulated":         "districts",
    "districts_history":             "districts/history/{types}",
    "districts_history_paginated":   "districts/history/{types}/{days}",

    "vaccination_accumulated":       "vaccinations",
    "vaccination_history":           "vaccinations/history",
    "vaccination_history_paginated": "vaccinations/history/{days}",

    "testing_history":               "testing/history",
    "testing_history_paginated":     "testing/history/{weeks}",
}