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

pikachu = pokemon("Pikachu", 100, 20)
charmander = pokemon("Charmander", 80, 25)
squirtle = pokemon("Squirtle", 120, 15)
bulbasur = pokemon("Bulbasur", 110, 18)
ponyta = pokemon("Ponyta", 90, 22)
caterpie = pokemon("Caterpie", 70, 10)
weedle = pokemon("Weedle", 60, 12)
pidgey = pokemon("Pidgey", 75, 14)
rattata = pokemon("Rattata", 65, 16)
spearow = pokemon("Spearow", 70, 18)
ekans = pokemon("Ekans", 80, 17)
sandshrew = pokemon("Sandshrew", 95, 19)
nidoran = pokemon("Nidoran", 85, 18)
vulpix = pokemon("Vulpix", 80, 20)
jigglypuff = pokemon("Jigglypuff", 115, 12)
zubat = pokemon("Zubat", 70, 15)
oddish = pokemon("Oddish", 90, 14)
paras = pokemon("Paras", 85, 17)
venonat = pokemon("Venonat", 90, 16)
diglett = pokemon("Diglett", 60, 21)
meowth = pokemon("Meowth", 75, 18)
psyduck = pokemon("Psyduck", 95, 17)
mankey = pokemon("Mankey", 80, 22)
growlithe = pokemon("Growlithe", 100, 21)
poliwag = pokemon("Poliwag", 85, 16)
abra = pokemon("Abra", 60, 25)
machop = pokemon("Machop", 110, 23)

pokemons = [pikachu, charmander, squirtle, bulbasur, ponyta, caterpie, weedle, pidgey, rattata, spearow, ekans, sandshrew, nidoran, vulpix, jigglypuff, zubat, oddish, paras, venonat, diglett, meowth, psyduck, mankey, growlithe, poliwag, abra, machop]