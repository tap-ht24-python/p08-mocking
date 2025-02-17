class Country:

    def __init__(self, name, pop, area=None):
        self.__name = name
        self.__population = pop
        self._area = area  # Sätter det inte som hemligt utan bara som info att detta har man inget att göra med
        self.language = []


    def print_info(self):
        """
        Prints a summary
        """
        s = f" * I {self.__name} bor det {self.__population} miljoner invånare"
        #print(f" * I {self.__name} bor det {self.__population} miljoner invånare",
        #      end="")

        if self._area:
            s += f" med en area på {self._area} tusen km2."
        #    print(f" med en area på {self._area} tusen km2.", end="")

        print(s)

        if self.language:
            print("    - Officiella språk i", end=" ")
            print(self.__name, "är:", end=" ")
            print(*self.language, sep=",")


    @property
    def language(self):
        return self._language


    @language.setter
    def language(self, lang):
        self._language = lang

    def set_languages(self, languages):
        self.language = languages



se = Country("Sverige", 10.5, 450)
no = Country("Norge", 5.5)
island = Country("Island", 0.4)
danmark = Country("Danmark", 5.9, 42)

danmark.print_info()

finland = Country("Finland", 45.6, 338)
# mha setter:
finland.language = ["svenska, finska"]

# Alternativ metod:
finland.set_languages(["svenska", "finska"])

finland.print_info()

se.language = ["svenska"]
se.print_info()