import time
import fluidsynth
from fractions import Fraction
from action import Action
from mingus.containers import Note
from chord import Chord, normalize_chord_durations

class NotePlayer:
    def __init__(self, sound_font_path = "", bpm=60, gain=0.8):
        self.player = fluidsynth.Synth(gain)
        self.player.start()
        self.sound_font = self.player.sfload(sound_font_path)
        self.player.program_select(0, self.sound_font, 0, 0)
        self.bpm = bpm
    
    def __enter__(self):
        return self

    def __exit__(self):
        self.player.delete()

    def play_note(self, note: str | int, velocity: int=30) -> bool:
        if type(note) == str:
            note = int(Note(note))
        return self.player.noteon(0, note, velocity)
    
    def play_notes(self, notes: list[str | int]) -> None:
        for note in notes:
            self.play_note(note)
    
    def stop_note(self, note: str | int) -> bool:
        if type(note) == str:
            note = int(Note(note))
        return self.player.noteoff(0, note)
    
    def stop_notes(self, notes: list[str | int]) -> None:
        for note in notes:
            self.stop_note(note)
    
    def do_action(self, action: Action) -> None:
        if action.is_start:
            self.play_notes(action.notes)
        else:
            self.stop_notes(action.notes)
    
    def play_song(self, chords: list[Chord]) -> None:
        # this represents what each note was scaled by. the notes originally represented beat values (value of 1 = 1 beat)
        # beats per minute = self.bpm, so beats per second = self.bpm / 60 => seconds per beat = 60 / self.bpm
        # for n beats it will take n * (60 / self.bpm) seconds
        # from one of these chord time values to seconds, we should do:
        # (time_value(int) / common_note_len_unit(the scale factor)) * (60 / self.bpm)
        # ^^^^ how many beats it actually is ^^^^                    ^^ seconds/beat ^^
        common_note_len_unit = normalize_chord_durations(chords)
        print(f"common_note_len_unit: {common_note_len_unit}")

        # construct the actions needed for this song
        actions: list[Action] = []
        for chord in chords:
            actions.append(Action(chord.notes, chord.start, True))
            actions.append(Action(chord.notes, chord.end, False))
        # sort the actions by their time. actions are in time units, not seconds or beats!
        actions.sort(key=lambda act: act.time)

        # now, we should loop through with each iteration being the length of 1 time value (so 1 / common_note_len_unit actual beats)
        # the seconds of each 1 unit is (1 / common_note_len_unit) * (60 / self.bpm) seconds
        loop_unit_seconds = 60 / (common_note_len_unit * self.bpm)
        end = actions[-1].time # end is at the last action
        cur_actions_index = 0
        for time_units in range(end + 1):
            while cur_actions_index < len(actions) and actions[cur_actions_index].time <= time_units:
                self.do_action(actions[cur_actions_index])
                cur_actions_index += 1
            time.sleep(loop_unit_seconds)
            



p = NotePlayer(sound_font_path="Yamaha_C3_Grand_Piano.sf2", bpm=50, gain=0.8)

chords = [
    Chord(0, 4, ['C#-3', 'C#-4']),
    Chord(0, Fraction(1, 3), ['G#-4']),
    Chord(Fraction(1, 3), Fraction(1, 3), ['C#-5']),
    Chord(Fraction(2, 3), Fraction(1, 3), ['E-5']),
    Chord(1, Fraction(1, 3), ['G#-4']),
    Chord(Fraction(4, 3), Fraction(1, 3), ['C#-5']),
    Chord(Fraction(5, 3), Fraction(1, 3), ['E-5']),
    Chord(2, Fraction(1, 3), ['G#-4']),
    Chord(Fraction(7, 3), Fraction(1, 3), ['C#-5']),
    Chord(Fraction(8, 3), Fraction(1, 3), ['E-5']),
    Chord(3, Fraction(1, 3), ['G#-4']),
    Chord(Fraction(10, 3), Fraction(1, 3), ['C#-5']),
    Chord(Fraction(11, 3), Fraction(1, 3), ['E-5']),
    Chord(4, 4, ['B-2', 'B-3']),
    Chord(4, Fraction(1, 3), ['G#-4']),
    Chord(Fraction(13, 3), Fraction(1, 3), ['C#-5']),
    Chord(Fraction(14, 3), Fraction(1, 3), ['E-5']),
    Chord(5, Fraction(1, 3), ['G#-4']),
    Chord(Fraction(16, 3), Fraction(1, 3), ['C#-5']),
    Chord(Fraction(17, 3), Fraction(1, 3), ['E-5']),
    Chord(6, Fraction(1, 3), ['G#-4']),
    Chord(Fraction(19, 3), Fraction(1, 3), ['C#-5']),
    Chord(Fraction(20, 3), Fraction(1, 3), ['E-5']),
    Chord(7, Fraction(1, 3), ['G#-4']),
    Chord(Fraction(22, 3), Fraction(1, 3), ['C#-5']),
    Chord(Fraction(23, 3), Fraction(1, 3), ['E-5']),
    Chord(8, 2, ['A-2', 'A-3']),
    Chord(8, Fraction(1, 3), ['A-4']),
    Chord(Fraction(25, 3), Fraction(1, 3), ['C#-5']),
    Chord(Fraction(26, 3), Fraction(1, 3), ['E-5']),
    Chord(9, Fraction(1, 3), ['A-4']),
    Chord(Fraction(28, 3), Fraction(1, 3), ['C#-5']),
    Chord(Fraction(29, 3), Fraction(1, 3), ['E-5']),
    Chord(10, 2, ['F#-2', 'F#-3']),
    Chord(10, Fraction(1, 3), ['A-4']),
    Chord(Fraction(31, 3), Fraction(1, 3), ['D-5']),
    Chord(Fraction(32, 3), Fraction(1, 3), ['F#-5']),
    Chord(11, Fraction(1, 3), ['A-4']),
    Chord(Fraction(34, 3), Fraction(1, 3), ['D-5']),
    Chord(Fraction(35, 3), Fraction(1, 3), ['F#-5']),
    Chord(12, 2, ['G#-2', 'G#-3']),
    Chord(12, Fraction(1, 3), ['G#-4']),
    Chord(Fraction(37, 3), Fraction(1, 3), ['C-5']),
    Chord(Fraction(38, 3), Fraction(1, 3), ['F#-5']),
    Chord(13, Fraction(1, 3), ['G#-4']),
    Chord(Fraction(40, 3), Fraction(1, 3), ['C#-5']),
    Chord(Fraction(41, 3), Fraction(1, 3), ['E-5']),
    Chord(14, 2, ['G#-2', 'G#-3']),
    Chord(14, Fraction(1, 3), ['G#-4']),
    Chord(Fraction(43, 3), Fraction(1, 3), ['C#-5']),
    Chord(Fraction(44, 3), Fraction(1, 3), ['D#-5']),
    Chord(15, Fraction(1, 3), ['F#-4']),
    Chord(Fraction(46, 3), Fraction(1, 3), ['C-5']),
    Chord(Fraction(47, 3), Fraction(1, 3), ['D#-5']),
]

p.play_song(chords)
