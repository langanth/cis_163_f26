
class Block:

    def __init__(self):
        self.renewable = False
        self.stackable = (True, 64)
        self.tool = "pick axe"
        self.blast_resistance = 0.0
        self.hardness = 0.0
        self.luminous = False
        self.transparent = False
        self.flamable = False
        self.lava = False
        self.xyz = (0, 0, 0)

    def break_block(self, tool):
        # CHECK WIKI
        pass        

    def detect_block_in_radius(self):
        """
        Finds all blocks in a blast radius and calculates
        damage done to them and generates a list of Tuples

        returns list[tuples[block, distance]]
        """
        pass


class Grass(Block):

    def __init__(self):
        super().__init__()
        self.renewable = True
        self.tool = "shovel"
        self.blast_resistance = 0.6
        self.hardness = 0.6

class Tuff(Block):

    def __init__(self):
        super().__init__()
        self.blast_resistance = 6
        self.hardness = 1.5      


class TNT(Block):

    def __init__(self):
        pass

    def explode(self):
        blocks = super().detect_block_in_radius()
        pass
