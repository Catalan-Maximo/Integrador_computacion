from constantes import Introduccion, Capitulos, Final

class Narrative:
    def __init__(self):
        self.introduction = Introduccion
        self.chapters = Capitulos
        self.current_chapter = 1

    def display_introduction(self):
        print(self.introduction)

    def advance_chapter(self):
        self.current_chapter += 1
        if self.current_chapter in self.chapters:
            print(self.chapters[self.current_chapter])
        else:
            print(Final)

    def display_current_chapter(self):
        if self.current_chapter in self.chapters:
            print(self.chapters[self.current_chapter])
        else:
            print(Final)
