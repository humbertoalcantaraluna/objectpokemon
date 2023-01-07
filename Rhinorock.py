from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(10)
        self.spend_attack(40)
        self.spend_defence(50)
        self.add_move(Cuerno())
        self.add_move(Tornado_arena())
        self.add_move(Terremoto())
        self.add_move(Lava())
        self.set_type(Type.Earth)
        self.move = 0
        self.moves = ['Cuerno', "Tornado_arena", "Terremoto", "Lava"]


    def get_name(self):
        return "Rhinorock"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)

class Cuerno(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.Earth)

    def get_name(self):
        return "Cuerno"

class Tornado_arena(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.Earth)

    def get_name(self):
        return "Tornado_arena"


class Terremoto(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.Water)

    def get_name(self):
        return "Terremoto"


class Lava(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.Fire)

    def get_name(self):
        return "Lava"