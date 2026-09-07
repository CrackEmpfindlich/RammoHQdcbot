from typing import List
from models.member import Member
import asyncpg

class MemberRepository:
    def __init__(self, pool: asyncpg.Pool):
        self.pool = pool

        async def create_member(self, member: Member) -> Member:
            async with self.pool.acquire() as conn:
                query = """
                INSERT INTO members (discord_id, guild_id, status, rank, created_at, updated_at)
                VALUES ($1, $2, $3, $4, $5, $6)
                RETURNING *
            """
                row = await conn.fetchrow(query, member.discord_id, member.guild_id, member.status, member.rank, member.created_at, member.updated_at)
                return Member(**row)

                async def get_member(self, discord_id: str, guild_id: str) -> Member:
                    async with self.pool.acquire() as conn:
                        query = """
                SELECT * FROM members WHERE discord_id = $1 AND guild_id = $2
            """
                        row = await conn.fetchrow(query, discord_id, guild_id)
                        return Member(**row) if row else None

                        async def update_member(self, member: Member) -> Member:
                            async with self.pool.acquire() as conn:
                                query = """
                UPDATE members SET status = $1, rank = $2, updated_at = $3
                WHERE discord_id = $4 AND guild_id = $5
                RETURNING *
            """
                                row = await conn.fetchrow(query, member.status, member.rank, member.updated_at, member.discord_id, member.guild_id)
                                return Member(**row) if row else None
