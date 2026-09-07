from discord import app_commands, Interaction, Embed
from discord.ext import commands
from services.sanction_service import SanctionService
from services.audit_service import AuditService
from utils.embeds import create_embed

class SanctionCommands(commands.Cog):
    def __init__(self, bot: commands.Bot, sanction_service: SanctionService, audit_service: AuditService):
        self.bot = bot
        self.sanction_service = sanction_service
        self.audit_service = audit_service

        @app_commands.command(name="sanction", description="Manage sanctions")
        async def sanction(self, interaction: Interaction):
            await interaction.response.send_message("Sanction command", ephemeral=True)

            @sanction.command(name="create", description="Create a new sanction")
            async def create(self, interaction: Interaction, member: discord.Member, reason: str, duration: int):
                sanction = Sanction(
                id=0,
                member_discord_id=member.id,
                guild_id=interaction.guild.id,
                type="TEMPORARY",
                reason=reason,
                issued_by=interaction.user.id,
                issued_at=datetime.now().isoformat(),
                expires_at=(datetime.now() + timedelta(days=duration)).isoformat(),
                revoked_by="",
                revoked_at="",
                is_active=True
            )
            await self.sanction_service.create_sanction(sanction)
            await self.audit_service.log_action(interaction.user.id, "create_sanction", member.id, "", reason, "Sanction created", datetime.now().isoformat())
            await interaction.response.send_message(f"Sanction created for {member.display_name}", ephemeral=True)
