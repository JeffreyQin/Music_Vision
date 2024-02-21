from chord import Chord

class Action:
    def __init__(self, notes: list[str | int], time: int, is_start: bool):
        self.notes = notes
        self.time = time
        self.is_start = is_start
