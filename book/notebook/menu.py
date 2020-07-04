import sys
from notebook import Notebook

#interface
class Menu:
    '''display menue and respond to choices'''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit,
        }

    def display_menu(self):
        print(
            '''
            Notebook menue
            1. show all notes
            2. search notes
            3. add note
            4. modify note
            5. quit '''
        )

    def run(self):
        '''display menue and respond to choices'''
        while True:
            self.display_menu()
            choice = input("choose an option")
            action = self.choices.get(choice)
            # action variable refers to a specific method, and is called by appending empty brackets (since none of the methods require parameters) to the variable
            if action: #if input is 1 to 5
                action()
            else:
                print("{0} is not valid".format(choice))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(note.id, note.tags, note.memo))

    def search_notes(self):
        filter = input("search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("enter a memo")
        self.notebook.new_note(memo)
        print("new note has been added")

    def modify_note(self):
        id = input("enter a note id")
        memo = input("enter a memo")
        tags = input("enter a tag")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print("byeeee")
        sys.exit()

    if __name__ == "__main__":
        Menu().run()


















