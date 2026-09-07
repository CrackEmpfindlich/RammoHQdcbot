from typing import List
import asyncpg

class AuditService:
    def __init__(self, pool: asyncpg.Pool):
        self.pool = pool

        async def log_action(self, actor_discord_id: str, action: str, target_discord_id: str, old_value: str, new_value: str, reason: str, timestamp: str) -> None:
            async with self.pool.acquire() as conn:
                query = """
                INSERT INTO audit_logs (actor_discord_id, action, target_discord_id, old_value, new_value, reason, timestamp)
                VALUES ($1, $2, $3, $4, $5, $6, $7)
            """
                await conn.execute(query, actor_discord_id, action, target_discord_id, old_value, new_value, reason, timestamp)

                async def get_audit_logs(self, target_discord_id: str) -> List[dict]:
                    async with self.pool.acquire() as conn:
                        query = "SELECT * FROM audit_logs WHERE target_discord_id = $1 ORDER BY timestamp DESC"
                        rows = await conn.fetch(query, target_discord_id)
                        return [dict(row) for row in rows]
