from discord import app_commands, Interaction, Embed
from discord.ext import commands
from services.setup_service import SetupService
from utils.embeds import create_embed

class SetupCommands(commands.Cog):
    def __init__(self, bot: commands.Bot, setup_service: SetupService):
        self.bot = bot
        self.setup_service = setup_service

        @app_commands.command(name="setup", description="Setup the bot for the guild")
        async def setup(self, interaction: Interaction):
            await interaction.response.send_message("Setup command", ephemeral=True)

            @setup.command(name="preview", description="Preview the setup changes")
            async def preview(self, interaction: Interaction):
                changes = await self.setup_service.preview_changes(interaction.guild)
                embed = create_embed(title="Setup Preview", description="\n".join(changes), color=discord.Color.gold())
                await interaction.response.send_message(embed=embed, ephemeral=True)

                @setup.command(name="apply", description="Apply the setup changes")
                async def apply(self, interaction: Interaction):
                    await self.setup_service.apply_changes(interaction.guild)
                    await interaction.response.send_message("Setup changes applied", ephemeral=True)
