from mingus.containers import Note
from fractions import Fraction
from math import lcm

# storage class
# start, duration, and stop are in beats, not sec or time
class Chord():
    def __init__(self, start: Fraction | int, duration: Fraction | int, notes: list[str | int]):
        self.start = start
        self.duration = duration
        self.end = start + duration
        self.notes = [int(Note(note)) for note in notes]

def is_integer(fraction: Fraction):
    return (fraction.numerator % fraction.denominator == 0)

# scales all chord lens to be integers such that they have the same relative lengths, then returns what everything was scaled by
def normalize_chord_durations(chords: list[Chord]) -> int:
    denominators = []
    for chord in chords:
        denominators.append(1 if type(chord.start) == int else chord.start.denominator)
        denominators.append(1 if type(chord.end) == int else chord.end.denominator)
    
    denom_lcm = lcm(*denominators)
    for i in range(len(chords)):
        chords[i].start *= denom_lcm
        assert(type(chords[i].start) == int or is_integer(chords[i].start))
        chords[i].start = int(chords[i].start)

        chords[i].duration *= denom_lcm
        assert(type(chords[i].start) == int or is_integer(chords[i].duration))
        chords[i].duration = int(chords[i].duration)

        chords[i].end *= denom_lcm
        assert(type(chords[i].start) == int or is_integer(chords[i].end))
        chords[i].end = int(chords[i].end)
    
    return denom_lcm
        

    