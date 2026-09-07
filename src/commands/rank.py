from discord import app_commands, Interaction, Embed
from discord.ext import commands
from services.rank_service import RankService
from services.audit_service import AuditService
from utils.embeds import create_embed

class RankCommands(commands.Cog):
    def __init__(self, bot: commands.Bot, rank_service: RankService, audit_service: AuditService):
        self.bot = bot
        self.rank_service = rank_service
        self.audit_service = audit_service

        @app_commands.command(name="rank", description="Manage ranks")
        async def rank(self, interaction: Interaction):
            await interaction.response.send_message("Rank command", ephemeral=True)

            @rank.command(name="set", description="Set a member's rank")
            async def set(self, interaction: Interaction, member: discord.Member, rank_level: int):
                rank = await self.rank_service.get_rank_by_level(rank_level)
                if not rank:
                    await interaction.response.send_message("Invalid rank level", ephemeral=True)
                    return
                    # Update member rank logic here
                    await self.audit_service.log_action(interaction.user.id, "set_rank", member.id, "", rank.name, "Rank update", datetime.now().isoformat())
                    await interaction.response.send_message(f"Rank for {member.display_name} set to {rank.name}", ephemeral=True)
