"""
Notebook.
"""

import doctest
import datetime
import sys


class Note:
    """
    Class for Note.
    """

    def __init__(self, memo, tags):
        """
        Init.

        >>> note = Note('Some note.', ['first'])
        """

        date = datetime.datetime.now()

        self.memo = memo
        self.creation_date = date.strftime("%d.%m.%Y")
        self.tags = tags

    def match(self, search_filter: str) -> bool:
        """
        Check tags.
        """

        if search_filter in self.tags:
            return True

        return False


class Notebook:
    """
    Class for Notebook.
    """

    def __init__(self):
        """
        Init.
        """

        self.notes = []

    def search(self, filter_s: str) -> list:
        """
        Search notes by filter.
        """

        result = []

        for note in self.notes:
            if note.match(filter_s):
                result.append(note)

        return result

    def new_note(self, memo, tags):
        """
        Create note.
        """

        tags_list = tags.split()
        note = Note(memo, tags_list)
        self.notes.append(note)

    def modify_memo(self, note_id, memo):
        """
        Modify name.
        """

        if note_id < len(self.notes):
            self.notes[note_id].memo = memo

    def modify_tags(self, note_id, tags):
        """
        Modify tags.
        """

        tags_list = tags.split()
        if note_id < len(self.notes):
            self.notes[note_id].tags = tags_list


class Menu:
    """
    Class for Menu.
    """

    def __init__(self):
        """
        Init.
        """

        self.instruction()
        self.notebook = Notebook()

    def interact(self):
        """
        Main loop of menu.
        """

        while True:
            command = self.wait_command()

            if command == "notes":
                self.notes(self.notebook.notes)
            elif command == "create":
                self.create()
            elif command == "edit":
                self.edit()
            elif command == "search":
                self.search()
            elif command == "exit":
                sys.exit()
            else:
                print("Sorry, this command doesn't exist.")

            self.instruction()

    def instruction(self):
        """
        Print instructions.
        """

        print(
            "\nAvailable commands:\n  - notes\n  - create\n  - search\n  - edit\n  - exit\n")

    def wait_command(self):
        """
        Read user's input.
        """

        print(">>> ", end="")
        command = input()

        return command

    def notes(self, notes):
        """
        Printing notes.
        """

        for note in notes:
            print(note.creation_date)
            print(note.memo)

            tags = "#" + "#".join(note.tags)
            print(tags)

            print()

    def search(self):
        """
        Search menu.
        """

        print("Enter a filter for search.")
        filter_ = self.wait_command()

        notes = self.notebook.search(filter_)

        if notes:
            self.notes(notes)
        else:
            print("Nothing was found.")

    def create(self):
        """
        Create a note.
        """

        print("Enter a text of note.")
        text = self.wait_command()
        print("Enter tags for the note.")
        tags = self.wait_command()

        self.notebook.new_note(text, tags)

        print("Created successfully.")

    def edit(self):
        """
        Edit note.
        """

        print("Enter id of the note for range [0, {}]".format(
            len(self.notebook.notes) - 1))
        id_note = self.wait_command()

        print("Choose the type of editing.\n0 - edit text\n1 - edit tags")
        command = self.wait_command()

        if command == '0':
            print("Enter a text of note.")
            text = self.wait_command()

            self.notebook.modify_memo(int(id_note), text)

        elif command == '1':
            print("Enter tags of note.")
            tags = self.wait_command()

            self.notebook.modify_tags(int(id_note), tags)

        else:
            print("Command is invalid!")


def main():
    """
    Main function.
    """

    menu = Menu()
    menu.interact()


if __name__ == "__main__":
    main()

doctest.testmod()
