from ABaseGato import ABaseGato, require_alive

class NormalGato(ABaseGato):
    """
        > A gato with 140 base HP.
    """

    IMAGE = "https://media.discordapp.net/attachments/435078369852260353/1192963553934704730/seelegato.png"
    ANIMATIONS = "4star"
    DISPLAY_NAME = "Berry Butterfly"
    RARITY = 4

    max_health: float = 140.0   # Create custom attributes for this gato class


    def simulate(self, team: list["ABaseGato"], seconds: int = 1):
        return super().simulate(team, seconds)