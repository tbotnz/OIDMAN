lookup_table = [
    {
        "match_str": "Timeticks",
        "regexp": r'Timeticks: \((\d+)\)',
        "group": 1,
        "type": int
    },
    {
        "match_str": "Counter32",
        "regexp": r'Counter32: (\d+)',
        "group": 1,
        "type": int
    },
    {
        "match_str": "Counter64",
        "regexp": r'Counter64: (\d+)',
        "group": 1,
        "type": int
    },
    {
        "match_str": "INTEGER",
        "regexp": r'INTEGER: (\d+)',
        "group": 1,
        "type": int
    },
    {
        "match_str": "Gauge32",
        "regexp": r'Gauge32: (\d+)',
        "group": 1,
        "type": int
    },
    {
        "match_str": "Gauge64",
        "regexp": r'Gauge64: (\d+)',
        "group": 1,
        "type": int
    },
]
