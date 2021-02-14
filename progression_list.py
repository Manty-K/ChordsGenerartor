from progression_chord import PChord
from chord_type import ChordType

common_major_progression = [
    [
        PChord(index=1, type=ChordType.maj),
        PChord(index=5, type=ChordType.maj),
        PChord(index=6, type=ChordType.min),
        PChord(index=4, type=ChordType.maj),
    ],
    [
        PChord(index=1, type=ChordType.maj),
        PChord(index=6, type=ChordType.min),
        PChord(index=4, type=ChordType.maj),
        PChord(index=5, type=ChordType.maj),
    ],
    [
        PChord(index=1, type=ChordType.maj),
        PChord(index=6, type=ChordType.min),
        PChord(index=2, type=ChordType.min),
        PChord(index=5, type=ChordType.maj),
    ],
    [
        PChord(index=1, type=ChordType.maj),
        PChord(index=4, type=ChordType.maj),
        PChord(index=6, type=ChordType.min),
        PChord(index=5, type=ChordType.maj),
    ],
    [
        PChord(index=1, type=ChordType.maj),
        PChord(index=3, type=ChordType.min),
        PChord(index=4, type=ChordType.maj),
        PChord(index=5, type=ChordType.maj),
    ],
    [
        PChord(index=1, type=ChordType.maj),
        PChord(index=4, type=ChordType.maj),
        PChord(index=1, type=ChordType.maj),
        PChord(index=5, type=ChordType.maj),
    ],
    [
        PChord(index=1, type=ChordType.maj),
        PChord(index=4 , type=ChordType.maj),
        PChord(index=2,type=ChordType.min),
        PChord(index=5, type=ChordType.maj),
    ],
    [
        PChord(index=2, type=ChordType.min7),
        PChord(index=5, type=ChordType.maj),
        PChord(index=1,type=ChordType.maj7),
    ],
    [
        PChord(index=1, type=ChordType.maj),
        PChord(index=4, type=ChordType.maj),
        PChord(index=5, type=ChordType.maj),
    ],

]

common_minor_progression = [

    [
        PChord(index=1, type=ChordType.min),
        PChord(index=6, type=ChordType.maj),
        PChord(index=7, type=ChordType.maj),
    ],
    [
        PChord(index=1, type=ChordType.min),
        PChord(index=4, type=ChordType.min),
        PChord(index=7, type=ChordType.maj),
    ],
    [
        PChord(index=1, type=ChordType.min),
        PChord(index=4, type=ChordType.min),
        PChord(index=5, type=ChordType.min),
    ],
    [
        PChord(index=1, type=ChordType.min),
        PChord(index=6, type=ChordType.maj),
        PChord(index=3, type=ChordType.maj),
        PChord(index=7, type=ChordType.maj),
    ],
    [
        PChord(index=2, type=ChordType.min),
        PChord(index=5, type=ChordType.min),
        PChord(index=1, type=ChordType.min),
    ],
    [
        PChord(index=1, type=ChordType.min),
        PChord(index=4, type=ChordType.min),
        PChord(index=5, type=ChordType.min),
        PChord(index=1, type=ChordType.min),
    ],
    [
        PChord(index=6, type=ChordType.maj),
        PChord(index=7, type=ChordType.maj),
        PChord(index=1, type=ChordType.min),
        PChord(index=1, type=ChordType.min),
    ],
    [
        PChord(index=1, type=ChordType.min),
        PChord(index=7, type=ChordType.maj),
        PChord(index=6, type=ChordType.maj),
        PChord(index=7, type=ChordType.maj),
    ],
    [
        PChord(index=1, type=ChordType.min),
        PChord(index=4, type=ChordType.min),
        PChord(index=1, type=ChordType.min),
    ],
]
