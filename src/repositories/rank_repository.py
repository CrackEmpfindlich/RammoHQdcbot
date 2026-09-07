from typing import List
from models.rank import Rank
import asyncpg

class RankRepository:
    def __init__(self, pool: asyncpg.Pool):
        self.pool = pool

        async def get_all_ranks(self) -> List[Rank]:
            async with self.pool.acquire() as conn:
                query = "SELECT * FROM ranks ORDER BY level DESC"
                rows = await conn.fetch(query)
                return [Rank(**row) for row in rows]

                async def get_rank_by_level(self, level: int) -> Rank:
                    async with self.pool.acquire() as conn:
                        query = "SELECT * FROM ranks WHERE level = $1"
                        row = await conn.fetchrow(query, level)
                        return Rank(**row) if row else None
