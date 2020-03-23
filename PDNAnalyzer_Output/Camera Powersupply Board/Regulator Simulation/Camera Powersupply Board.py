designFile = "Y:/Altium Projects/Camera Powersupply/PDNAnalyzer_Output/Camera Powersupply Board/odb.tgz"

powerNets = ["VCC", "VCC_CLEAN", "VREGIN", "SW", "5V", "FBIN", "FB", "ISO_IN_IS1", "ISO_IN_IS2", "ISO_OUT_IS1", "ISO+_IS1", "ISO_OUT_IS2", "ISO+_IS2"]

groundNets = ["GND_P", "GND", "VOUT-", "ISO-_IS1", "ISO-_IS2"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("J1", "1") ],
"ground_pins": [ ("J1", "3"), ("J1", "2") ],
"voltage": 16.8,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("J2", "6") ],
"ground_pins": [ ("J2", "3"), ("J2", "2"), ("J2", "1") ],
"current": 1,
"Rpin": 0.15,
}
,
{
"id": "2",
"type": "load",
"power_pins": [ ("J2", "5") ],
"ground_pins": [ ("J2", "3"), ("J2", "2"), ("J2", "1") ],
"current": 1,
"Rpin": 0.15,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("R7", "2") ],
"ground_pins": [ ("R7", "1") ],
"resistance": 1E-09,
"Rpin": 550,
}
,
{
"id": "4",
"type": "load",
"power_pins": [ ("J3", "1") ],
"ground_pins": [ ("J3", "4") ],
"current": 0.5,
"Rpin": 0.2,
}
,
{
"id": "5",
"type": "load",
"power_pins": [ ("J2", "4") ],
"ground_pins": [ ("J2", "3"), ("J2", "2"), ("J2", "1") ],
"current": 5,
"Rpin": 0.03,
}
,
{
"id": "6",
"type": "load",
"power_pins": [ ("J4_IS1", "1") ],
"ground_pins": [ ("J4_IS1", "4") ],
"current": 0.3,
"Rpin": 0.333333333333333,
}
,
{
"id": "7",
"type": "load",
"power_pins": [ ("J4_IS2", "1") ],
"ground_pins": [ ("J4_IS2", "4") ],
"current": 0.3,
"Rpin": 0.333333333333333,
}
,
{
"id": "8",
"type": "source",
"power_pins": [ ("A1_IS1", "8") ],
"ground_pins": [ ("A1_IS1", "7") ],
"voltage": 5,
"Rpin": 0,
}
,
{
"id": "9",
"type": "load",
"power_pins": [ ("A1_IS1", "3") ],
"ground_pins": [ ("A1_IS1", "1") ],
"current": 0.0001,
"Rpin": 100000,
}
,
{
"id": "10",
"type": "source",
"power_pins": [ ("A1_IS2", "8") ],
"ground_pins": [ ("A1_IS2", "7") ],
"voltage": 5,
"Rpin": 0,
}
,
{
"id": "11",
"type": "load",
"power_pins": [ ("A1_IS2", "3") ],
"ground_pins": [ ("A1_IS2", "1") ],
"current": 0.0001,
"Rpin": 100000,
}
,
{
"id": "12",
"type": "source",
"power_pins": [ ("IC2", "14"), ("IC2", "13"), ("IC2", "12"), ("IC2", "11"), ("IC2", "10"), ("IC2", "9") ],
"ground_pins": [ ("IC2", "35"), ("IC2", "34"), ("IC2", "31"), ("IC2", "32"), ("IC2", "30"), ("IC2", "29"), ("IC2", "17"), ("IC2", "16"), ("IC2", "15"), ("IC2", "8"), ("IC2", "7"), ("IC2", "6") ],
"voltage": 5,
"Rpin": 0,
}
,
{
"id": "13",
"type": "load",
"power_pins": [ ("IC2", "19"), ("IC2", "18"), ("IC2", "5"), ("IC2", "4"), ("IC2", "3"), ("IC2", "2") ],
"ground_pins": [ ("IC2", "35"), ("IC2", "34"), ("IC2", "31"), ("IC2", "32"), ("IC2", "30"), ("IC2", "29"), ("IC2", "17"), ("IC2", "16"), ("IC2", "15"), ("IC2", "8"), ("IC2", "7"), ("IC2", "6") ],
"current": 0.0001,
"Rpin": 800000,
}
,
{
"id": "14",
"type": "load",
"power_pins": [ ("IC2", "23") ],
"ground_pins": [ ("IC2", "22") ],
"resistance": 1E-09,
"Rpin": 500000,
}
]


voltage_regulators = [
{
"id": "15",
"type": "linear",

"in": [ ("IC1", "8"), ("IC1", "7"), ("IC1", "6"), ("IC1", "5") ],
"out": [ ("IC1", "3"), ("IC1", "2"), ("IC1", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.0454285714285714,
}
,
{
"id": "16",
"type": "linear",

"in": [ ("L1", "1") ],
"out": [ ("L1", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 8.25E-05,
}
,
{
"id": "17",
"type": "linear",

"in": [ ("L4", "2") ],
"out": [ ("L4", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 8.25E-05,
}
,
{
"id": "18",
"type": "linear",

"in": [ ("L5", "1") ],
"out": [ ("L5", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.0006,
}
,
{
"id": "19",
"type": "linear",

"in": [ ("R4", "2") ],
"out": [ ("R4", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5,
}
,
{
"id": "20",
"type": "linear",

"in": [ ("R5", "2") ],
"out": [ ("R5", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5000,
}
,
{
"id": "21",
"type": "linear",

"in": [ ("R8", "2") ],
"out": [ ("R8", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "22",
"type": "linear",

"in": [ ("L3_IS1", "1") ],
"out": [ ("L3_IS1", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.085,
}
,
{
"id": "23",
"type": "linear",

"in": [ ("L3_IS2", "1") ],
"out": [ ("L3_IS2", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.085,
}
,
{
"id": "24",
"type": "linear",

"in": [ ("L2_IS1", "1") ],
"out": [ ("L2_IS1", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.166,
}
,
{
"id": "25",
"type": "linear",

"in": [ ("L2_IS2", "1") ],
"out": [ ("L2_IS2", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.166,
}
]


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.8, 'Thickness': 0.00155},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
