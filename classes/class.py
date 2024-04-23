class Pokémon:
    def __init__(self, name : str, type : str, Atk : str, Def : str):
        self.name = name
        self.type = type
        self.Atk = Atk
        self.Def = Def

    def __str__(self):
        return f"{self.name} {self.type}"
    
    