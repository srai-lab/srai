"""_summary_."""

import numpy as np

ACCEPTABLE_FEATURES = {
    "oneway": ["False", "True"],
    "lanes": list(map(str, range(1, 21))),
    "highway": [
        "motorway",
        "motorway_link",
        "trunk",
        "trunk_link",
        "primary",
        "primary_link",
        "secondary",
        "secondary_link",
        "tertiary",
        "tertiary_link",
        "residential",
        "unclassified",
        "living_street",
        "service",
        "pedestrian",
        "track",
        "bus_guideway",
        "escape",
        "raceway",
        "road",
        "busway",
        "footway",
        "bridleway",
        "steps",
        "corridor",
        "path",
    ],
    "maxspeed": [
        "5",
        "7",
        "10",
        "15",
        "20",
        "30",
        "40",
        "50",
        "60",
        "70",
        "80",
        "90",
        "100",
        "110",
        "120",
        "130",
        "140",
    ],
    "bridge": [
        "yes",
        "aqueduct",
        "boardwalk",
        "cantilever",
        "covered",
        "low_water_crossing",
        "movable",
        "trestle",
        "viaduct",
        "simple_brunnel",
    ],
    "access": [
        "yes",
        "no",
        "private",
        "public",
        "permissive",
        "permit",
        "destination",
        "delivery",
        "customers",
        "designated",
        "use_sidepath",
        "dismount",
        "agricultural",
        "forestry",
        "discouraged",
        "unknown",
        "restricted",
        "official",
        "students",
        "licence",
        "license",
        "exclusion_zone",
        "dismount",
    ],
    "junction": [
        "yes",
        "roundabout",
        "circular",
        "spui",
        "jughandle",
        "filter",
        "intersection",
        "crossing",
        "uncontrolled",
    ],
    "width": list(np.arange(0, 30.5, 0.5).astype("str")),
    "tunnel": ["building_passage", "yes", "avalanche_protector"],
    "surface": [
        "paved",
        "asphalt",
        "chipseal",
        "concrete",
        "concrete:lanes",
        "concrete:plates",
        "paving_stones",
        "sett",
        "unhewn_cobblestone",
        "cobblestone",
        "metal",
        "wood",
        "stepping_stones",
        "rubber",
        "unpaved",
        "compacted",
        "fine_gravel",
        "gravel",
        "rock",
        "pebblestone",
        "ground",
        "dirt",
        "earth",
        "grass",
        "grass_paver",
        "mud",
        "sand",
        "woodchips",
        "snow",
        "ice",
        "salt",
    ],
    "bicycle": [
        "yes",
        "no",
        "designated",
        "use_sidepath",
        "dismount",
        "permissive",
        "private",
        "customers",
        "destination",
        "official",
    ],
    "lit": ["yes", "no", "sunset-sunrise", "24/7", "automatic", "disused", "limited", "interval"],
}
