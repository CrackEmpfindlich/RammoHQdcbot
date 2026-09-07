from models.guild import Guild
import asyncpg

class GuildRepository:
    def __init__(self, pool: asyncpg.Pool):
        self.pool = pool

        async def create_guild(self, guild: Guild) -> Guild:
            async with self.pool.acquire() as conn:
                query = """
                INSERT INTO guilds (id, name, owner_id, created_at)
                VALUES ($1, $2, $3, $4)
                RETURNING *
            """
                row = await conn.fetchrow(query, guild.id, guild.name, guild.owner_id, guild.created_at)
                return Guild(**row)

                async def get_guild(self, guild_id: str) -> Guild:
                    async with self.pool.acquire() as conn:
                        query = "SELECT * FROM guilds WHERE id = $1"
                        row = await conn.fetchrow(query, guild_id)
                        return Guild(**row) if row else None
