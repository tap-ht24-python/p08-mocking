class Country:

    def __init__(self, name, pop, area=None):
        self.__name = name
        self.__population = pop
        self._area = area  # Sätter det inte som hemligt utan bara som info att detta har man inget att göra med
        self.languages = []


    def print_info(self):
        """
        Prints a summary
        """
        s = f" * I {self.__name} bor det {self.__population} miljoner invånare"

        if self._area:
            s += f" med en area på {self._area} tusen km2."

        print(s)

        s = ""
        if len(self.languages) < 1:
            s = f"    - Det finns inga språk inlagda"
        elif len(self.languages) == 1:
            s = f"    - Det officiella språket är {self.languages[0]}"
        #elif len(self.languages) == 2:
        #    s = f"    - De officiella språken är {self.languages[0]} och {self.languages[1]}"
        else:
            s = self.custom_join_languages()

        print(s)

    def custom_join_languages(self):
        languages = self.languages
        initial_text = " Man talar språken: "

        if len(languages) == 1:
            return initial_text + languages[0]

        all_except_last_language = ", ".join(languages[:-1])  # join with commas - last language excluded
        last_language = " och " + languages[-1]  # last language is prefixed with "och"
        return initial_text + all_except_last_language + last_language

    @property
    def languages(self):
        return self._language


    @languages.setter
    def languages(self, lang):
        self._language = lang

    def set_languages(self, languages):
        self.languages = languages



se = Country("Sverige", 10.5, 450)
no = Country("Norge", 5.5)
island = Country("Island", 0.4)
danmark = Country("Danmark", 5.9, 42)

danmark.print_info()

finland = Country("Finland", 45.6, 338)
# mha setter:
finland.languages = ["svenska, finska"]

# Alternativ metod:
finland.set_languages(["svenska", "finska"])

finland.print_info()

se.languages = ["svenska", "rövarspråket", "svengelska", "python"]
se.print_info()