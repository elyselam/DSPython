import datetime
last_id = 0
class Note:
    '''represent each note in a notebook.
    Match against a string in searches and store tags for each note'''
    def __init__(self, memo, tags=""):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        '''True if this note matches the filter text'''
        return filter in self.memo or filter in self.tags


n1 = Note("hi")
n2 = Note("butt")
print(n1.id)
print(n2.id)
print(n2.match("butt"))


class Notebook:
    '''represent a collection of notes that can be tagged, modified, and searched'''
    def __init__(self):
        '''initialize with an empty list'''
        self.notes = []

    def new_note(self, memo, tags=""):
        '''append new note to notes list'''
        self.notes.append(Note(memo, tags))


    def _find_note(self, note_id):
        '''locate note with given id
        underscore means internal use only '''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self, note_id, memo):
        '''find note with given id and change its memo to given value'''
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):
        '''find note with given id and change its memo to given value'''
        self._find_note(note_id).tags = tags


    def search(self, filter):
        '''find all notes that match a given filter str'''
        return [note for note in self.notes if note.match(filter)]


n = Notebook()
n.new_note("butt")
n.new_note("face")
print(n.notes)

print(n.notes[0].id)
print(n.notes[0].memo)
print(n.notes[1].memo)








