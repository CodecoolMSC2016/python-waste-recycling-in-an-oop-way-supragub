from garbage import Garbage


class PaperGarbage(Garbage):

    def __init__(self, name, squeezed):
        Garbage.__init__(self, name)
        self.is_squeezed = squeezed

    def squeeze(self):
        self.is_squeezed = True
