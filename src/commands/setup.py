import discord
from discord import app_commands
from discord.ext import commands

from config import Config


class Setup(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="setup",
        description="Erstellt die Grundstruktur für RammoHQ.",
    )
    @app_commands.guild_only()
    @app_commands.default_permissions(administrator=True)
    async def setup_command(self, interaction: discord.Interaction) -> None:
        guild = interaction.guild

        if guild is None:
            await interaction.response.send_message(
                "❌ Dieser Befehl kann nur auf einem Server verwendet werden.",
                ephemeral=True,
            )
            return

        if Config.GUILD_ID and guild.id != Config.GUILD_ID:
            await interaction.response.send_message(
                "❌ Dieser Server ist nicht als RammoHQ-Guild konfiguriert.",
                ephemeral=True,
            )
            return

        await interaction.response.defer(ephemeral=True, thinking=True)

        created_roles = 0
        created_categories = 0
        created_channels = 0

        for _, name in reversed(list(Config.RANKS.items())):
            role = discord.utils.get(guild.roles, name=name)

            if role is None:
                await guild.create_role(
                    name=name,
                    reason=f"RammoHQ Setup durch {interaction.user}",
                )
                created_roles += 1

        categories = {
            "00 • START": [
                "willkommen",
                "regeln",
                "ankündigungen",
                "faq",
            ],
            "01 • FAMILY": [
                "family-chat",
                "media",
                "vorschläge",
                "abwesenheit",
                "hilfe",
            ],
        }

        for category_name, channel_names in categories.items():
            category = discord.utils.get(
                guild.categories,
                name=category_name,
            )

            if category is None:
                category = await guild.create_category(
                    category_name,
                    reason=f"RammoHQ Setup durch {interaction.user}",
                )
                created_categories += 1

            for channel_name in channel_names:
                channel = discord.utils.get(
                    category.text_channels,
                    name=channel_name,
                )

                if channel is None:
                    await guild.create_text_channel(
                        channel_name,
                        category=category,
                        reason=f"RammoHQ Setup durch {interaction.user}",
                    )
                    created_channels += 1

        await interaction.followup.send(
            "✅ **RammoHQ Setup abgeschlossen.**\n"
            f"• Rollen erstellt: `{created_roles}`\n"
            f"• Kategorien erstellt: `{created_categories}`\n"
            f"• Textkanäle erstellt: `{created_channels}`",
            ephemeral=True,
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Setup(bot))
