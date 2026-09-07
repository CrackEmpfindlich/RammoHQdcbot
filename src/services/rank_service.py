from typing import List
from models.rank import Rank
from repositories.rank_repository import RankRepository

class RankService:
    def __init__(self, rank_repository: RankRepository):
        self.rank_repository = rank_repository

        async def get_all_ranks(self) -> List[Rank]:
            return await self.rank_repository.get_all_ranks()

            async def get_rank_by_level(self, level: int) -> Rank:
                return await self.rank_repository.get_rank_by_level(level)
