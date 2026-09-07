import discord
from discord import app_commands

class ConfigCommand(app_commands.Command):
    def __init__(self, bot):
        super().__init__(name="config", description="Manage bot configuration")
        self.bot = bot

        async def callback(self, interaction: discord.Interaction):
            await interaction.response.send_message("Bot configuration", ephemeral=True)
