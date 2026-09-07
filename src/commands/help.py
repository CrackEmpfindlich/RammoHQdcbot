import discord
from discord import app_commands

class HelpCommand(app_commands.Command):
    def __init__(self, bot):
        super().__init__(name="help", description="Show help information")
        self.bot = bot

        async def callback(self, interaction: discord.Interaction):
            await interaction.response.send_message("Help information", ephemeral=True)
