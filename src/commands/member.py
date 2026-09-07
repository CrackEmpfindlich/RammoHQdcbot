from discord import app_commands, Interaction, Embed
from discord.ext import commands
from services.member_service import MemberService
from services.audit_service import AuditService
from utils.embeds import create_embed

class MemberCommands(commands.Cog):
    def __init__(self, bot: commands.Bot, member_service: MemberService, audit_service: AuditService):
        self.bot = bot
        self.member_service = member_service
        self.audit_service = audit_service

        @app_commands.command(name="member", description="Manage members")
        async def member(self, interaction: Interaction):
            await interaction.response.send_message("Member command", ephemeral=True)

            @member.command(name="view", description="View member details")
            async def view(self, interaction: Interaction, member: discord.Member):
                member_data = await self.member_service.get_member(member.id, interaction.guild.id)
                embed = create_embed(title="Member Details", description=f"Details for {member.display_name}", color=discord.Color.red())
                embed.add_field(name="Status", value=member_data.status, inline=True)
                embed.add_field(name="Rank", value=member_data.rank, inline=True)
                await interaction.response.send_message(embed=embed, ephemeral=True)

                @member.command(name="register", description="Register a new member")
                async def register(self, interaction: Interaction, member: discord.Member):
                    member_data = Member(discord_id=member.id, guild_id=interaction.guild.id, status="ACTIVE", rank="Recruit", created_at=datetime.now().isoformat(), updated_at=datetime.now().isoformat())
                    await self.member_service.create_member(member_data)
                    await self.audit_service.log_action(interaction.user.id, "register", member.id, "", "ACTIVE", "New member registration", datetime.now().isoformat())
                    await interaction.response.send_message(f"Member {member.display_name} registered successfully", ephemeral=True)
