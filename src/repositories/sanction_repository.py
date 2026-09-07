from typing import List
from models.sanction import Sanction
import asyncpg

class SanctionRepository:
    def __init__(self, pool: asyncpg.Pool):
        self.pool = pool

        async def create_sanction(self, sanction: Sanction) -> Sanction:
            async with self.pool.acquire() as conn:
                query = """
                INSERT INTO sanctions (member_discord_id, guild_id, type, reason, issued_by, issued_at, expires_at, is_active)
                VALUES ($1, $2, $3, $4, $5, $6, $7, $8)
                RETURNING *
            """
                row = await conn.fetchrow(query, sanction.member_discord_id, sanction.guild_id, sanction.type, sanction.reason, sanction.issued_by, sanction.issued_at, sanction.expires_at, sanction.is_active)
                return Sanction(**row)

                async def get_active_sanctions(self, member_discord_id: str, guild_id: str) -> List[Sanction]:
                    async with self.pool.acquire() as conn:
                        query = """
                SELECT * FROM sanctions WHERE member_discord_id = $1 AND guild_id = $2 AND is_active = TRUE
            """
                        rows = await conn.fetch(query, member_discord_id, guild_id)
                        return [Sanction(**row) for row in rows]

                        async def revoke_sanction(self, sanction_id: int, revoked_by: str, revoked_at: str) -> Sanction:
                            async with self.pool.acquire() as conn:
                                query = """
                UPDATE sanctions SET is_active = FALSE, revoked_by = $1, revoked_at = $2
                WHERE id = $3
                RETURNING *
            """
                                row = await conn.fetchrow(query, revoked_by, revoked_at, sanction_id)
                                return Sanction(**row) if row else None
