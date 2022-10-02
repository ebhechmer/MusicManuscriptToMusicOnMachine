from rectangle import Rectangle

note_step = 0.0625

note_defs = {
     -4 : ("g", 79),
     -3 : ("f", 77),
     -2 : ("e", 76),
     -1 : ("d", 74),
      0 : ("c", 72),
      1 : ("b", 71),
      2 : ("a", 69),
      3 : ("g", 67),
      4 : ("f", 65),
      5 : ("e", 64),
      6 : ("d", 62),
      7 : ("c", 60),
      8 : ("b", 59),
      9 : ("a", 57),
     10 : ("g", 55),
     11 : ("f", 53),
     12 : ("e", 52),
     13 : ("d", 50),
     14 : ("c", 48),
     15 : ("b", 47),
     16 : ("a", 45),
     17 : ("f", 53),
}

class Note(object):
    def __init__(self, rec, sym, staff_rec, sharp_notes = [], flat_notes = []):
        self.rec = rec
        self.sym = sym

        middle = rec.y + (rec.h / 2.0)
        height = (middle - staff_rec.y) / staff_rec.h
        note_def = note_defs[int(height/note_step + 0.5)]
        self.note = note_def[0]
        self.pitch = note_def[1]
        if any(n for n in sharp_notes if n.note[0] == self.note[0]):
            self.note += "#"
            self.pitch += 1
        if any(n for n in flat_notes if n.note[0] == self.note[0]):
            self.note += "b"
            self.pitch -= 1


