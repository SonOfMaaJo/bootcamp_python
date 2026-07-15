class GotCharacter():
    def __init__(self, first_name: str = '', is_alive: bool = True) -> None:
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    """A class \\underline{representing} the Stark family. Or When bad things
    happen to good people
    """
    def __init__(self, first_name=None, is_alive=True) -> None:
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self) -> None:
        print(self.house_words)

    def die(self) -> None:
        self.is_alive = False
