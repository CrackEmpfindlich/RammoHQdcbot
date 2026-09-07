import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncpg
from services.member_service import MemberService
from services.sanction_service import SanctionService
from services.rank_service import RankService
from services.audit_service import AuditService
from services.setup_service import SetupService
from repositories.member_repository import MemberRepository
from repositories.sanction_repository import SanctionRepository
from repositories.rank_repository import RankRepository
from repositories.guild_repository import GuildRepository
from commands.member import MemberCommands
from commands.rank import RankCommands
from commands.sanction import SanctionCommands
from commands.setup import SetupCommands

load_dotenv()

class RammoHQBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())

        async def setup_hook(self):
            self.pool = await asyncpg.create_pool(os.getenv("DATABASE_URL"))
            member_repository = MemberRepository(self.pool)
            sanction_repository = SanctionRepository(self.pool)
            rank_repository = RankRepository(self.pool)
            guild_repository = GuildRepository(self.pool)

            member_service = MemberService(member_repository)
            sanction_service = SanctionService(sanction_repository)
            rank_service = RankService(rank_repository)
            audit_service = AuditService(self.pool)
            setup_service = SetupService(self.pool)

            await self.add_cog(MemberCommands(self, member_service, audit_service))
            await self.add_cog(RankCommands(self, rank_service, audit_service))
            await self.add_cog(SanctionCommands(self, sanction_service, audit_service))
            await self.add_cog(SetupCommands(self, setup_service))

            bot = RammoHQBot()

            @bot.event
            async def on_ready():
                print(f"Logged in as {bot.user}")
                try:
                    synced = await bot.tree.sync()
                    print(f"Synced {len(synced)} commands")
                    except Exception as e:
                        print(e)

                        @bot.tree.error
                        async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
                            if isinstance(error, app_commands.MissingPermissions):
                                await interaction.response.send_message("❌ You do not have the required permissions to use this command.", ephemeral=True)
                                else:
                                    await interaction.response.send_message("❌ An error occurred while executing the command.", ephemeral=True)
                                    print(error)

                                    if __name__ == "__main__":
                                        bot.run(os.getenv("DISCORD_TOKEN"))
