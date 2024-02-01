# Its_Fine_Its_Fine_Its_Fine

Converts image of piano sheet into encoded notes

## UPDATE UPDATE UPDATE

everything turned into one model now

## note localization from measure image


## note classification

Dataset
- path: './chord_data/'
- each chord will presumably have at most 5 notes (5 fingers lol)
- for now, all notes in the same chord will presumably have the same duration
- pitch-i in .csv represents the pitch of the i-th note in the chord (from lowest to highest)
- sfn-i in .csv represents sharp/flat/neural of the i-th note i the chord (from lowest to highest)

Data label for model
- tensor of (1 + 2k) dimensions where k is the # of distinct pitches on 5 staff line
- dimension 0 represents duration 
- dimension 1 to k represents if pitch i is being included in the chord (binary either 0 or 1)
- dimension k + 1 to 2k represents if pitch i has sharp/flat/neural

Task ^^^
- decide how many total distinct pitches are we classifying? for example 9 (within staff lines) + 5 (above staff lines) + 5 (below staff lines)
- decide what numbers to represent duration
- decide what numbers to represent sharp/flat/neural (e.g. 1 for shape, -1 for flat, 0 for neural)