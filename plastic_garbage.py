from garbage import Garbage


class PlasticGarbage(Garbage):

        def __init__(self, name, clean):
            Garbage.__init__(self, name)
            self.is_clean = clean

        def clean(self):
            self.is_clean = True
