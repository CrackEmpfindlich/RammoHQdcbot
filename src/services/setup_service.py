from src.repositories.guild_repository import GuildRepository
from src.repositories.member_repository import MemberRepository
from src.repositories.rank_repository import RankRepository
from src.repositories.sanction_repository import SanctionRepository

class SetupService:
    def __init__(self, pool):
        self.guild_repo = GuildRepository(pool)
        self.member_repo = MemberRepository(pool)
        self.rank_repo = RankRepository(pool)
        self.sanction_repo = SanctionRepository(pool)

        async def setup_database(self):
            await self.guild_repo.create_table()
            await self.member_repo.create_table()
            await self.rank_repo.create_table()
            await self.sanction_repo.create_table()
