from constantes import introduccion, capitulos, final

class Narrative:
    def __init__(self):
        self.introduction = introduccion
        self.chapters = capitulos
        self.current_chapter = 1

    def display_introduction(self):
        print(self.introduction)

    def advance_chapter(self):
        self.current_chapter += 1
        if self.current_chapter in self.chapters:
            print(self.chapters[self.current_chapter])
        else:
            print(final)

    def display_current_chapter(self):
        if self.current_chapter in self.chapters:
            print(self.chapters[self.current_chapter])
        else:
            print(final)
