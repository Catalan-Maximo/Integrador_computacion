class Narrative:
    def __init__(self):
        self.introduction = """
        En un reino olvidado, las fuerzas del mal han despertado. 
        Eres parte de un grupo de héroes que ha sido convocado para detener a 
        las criaturas que están aterrorizando la tierra. Cada paso que des te acercará más 
        a la verdad detrás de esta oscuridad. ¡Prepárate para la aventura de tu vida!
        """
        self.current_chapter = 1
        self.chapters = {
            1: "Capítulo 1: La llamada a la aventura\n\n" 
               "Tu viaje comienza en la aldea de los aventureros. Aquí, te reunirás con "
               "otros héroes para planear tu travesía hacia la Cueva de las Brujas.",
            2: "Capítulo 2: Enfrentando a los muertos\n\n"
               "Después de superar la Cueva de las Brujas te encuentras una aldea"
               "donde un habitante se ofrece como ayuda. Luego te diriges a la Tumba de tus Sueños, "
               "donde los no-muertos te desafiarán en cada esquina.",
            3: "Capítulo 3: La batalla final\n\n"
               "Finalmente, has llegado al corazón de la oscuridad,"
               "ayudado por el habitante de la aldea y un "
               "explorador de la Cueva de las Brujas. Los Orcos y sus demonios te esperan "
               "en una batalla que decidirá el destino del mundo."
        }

    def display_introduction(self):
        print(self.introduction)

    def advance_chapter(self):
        self.current_chapter += 1
        if self.current_chapter in self.chapters:
            print(self.chapters[self.current_chapter])
        else:
            print("Has completado la historia. ¡Felicitaciones, héroe!")

    def display_current_chapter(self):
        if self.current_chapter in self.chapters:
            print(self.chapters[self.current_chapter])
        else:
            print("Has completado la historia. ¡Felicitaciones, héroe!")
