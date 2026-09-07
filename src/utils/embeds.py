from discord import Embed, Color

def create_embed(title: str, description: str, color: Color) -> Embed:
    embed = Embed(title=title, description=description, color=color)
    embed.set_footer(text="Famiglia. Onore. Lealtà.")
    return embed
