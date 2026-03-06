class pokemon:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def deal_damage(self, other):
        other.take_damage(self.attack)

def battle(pokemon1, pokemon2):
    while pokemon1.is_alive() and pokemon2.is_alive():
        pokemon1.deal_damage(pokemon2)
        if not pokemon2.is_alive():
            print(f"{pokemon1.name} wins!")
            break
        pokemon2.deal_damage(pokemon1)
        if not pokemon1.is_alive():
            print(f"{pokemon2.name} wins!")
            break