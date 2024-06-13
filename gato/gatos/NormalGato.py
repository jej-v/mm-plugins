from ABaseGato import ABaseGato, require_alive

class NormalGato(ABaseGato):
    """
        > A gato with 140 base HP.
    """

    IMAGE = "https://cdn.discordapp.com/emojis/1173895764087414855.webp"
    ANIMATIONS = "mooncakegato"
    DISPLAY_NAME = "Mooncake"
    RARITY = 3

    max_health: float = 140.0   # Create custom attributes for this gato class


    def simulate(self, team: list["ABaseGato"], seconds: int = 1):
        super().simulate(team, seconds)