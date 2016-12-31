from garbage import Garbage
from paper_garbage import PaperGarbage
from plastic_garbage import PlasticGarbage
from dustbin_content_error import DustbinContentError


class Dustbin:

    def __init__(self, color):
        self.color = color
        self.paper_content = []
        self.plastic_content = []
        self.house_waste_content = []

    def throw_out_garbage(self, garbage):
        if isinstance(garbage, PlasticGarbage):
            if garbage.is_clean is True:
                self.plastic_content.append(garbage)
            else:
                raise DustbinContentError("Plastic garbage isn't clean")
        elif isinstance(garbage, PaperGarbage):
            if garbage.is_squeezed is True:
                self.paper_content.append(garbage)
            else:
                raise DustbinContentError("Paper garbage isn't squeezed.")
        elif isinstance(garbage, Garbage) and \
            isinstance(garbage, PlasticGarbage) == False and \
                isinstance(garbage, PaperGarbage) == False:
            self.house_waste_content.append(garbage)
        else:
            raise DustbinContentError("This is not a garbage.")

    def empty_contents(self):
        self.paper_content = []
        self.plastic_content = []
        self.house_waste_content = []
