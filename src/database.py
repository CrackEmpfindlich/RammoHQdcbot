import asyncpg
from config import Config


async def create_pool() -> asyncpg.Pool:
    return await asyncpg.create_pool(
        dsn=Config.DATABASE_URL,
        min_size=1,
        max_size=10,
        command_timeout=60,
    )


async def init_db(pool: asyncpg.Pool) -> None:
    async with pool.acquire() as conn:
        await conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS members (
                id SERIAL PRIMARY KEY,
                discord_id BIGINT UNIQUE NOT NULL,
                discord_name TEXT,
                discord_nickname TEXT,
                rp_name TEXT,
                rp_id TEXT,
                rp_rank INTEGER,
                status TEXT,
                join_date TIMESTAMPTZ DEFAULT NOW(),
                leave_date TIMESTAMPTZ,
                recruiter TEXT
            );

            CREATE TABLE IF NOT EXISTS sanctions (
                id SERIAL PRIMARY KEY,
                member_id INTEGER REFERENCES members(id) ON DELETE CASCADE,
                type TEXT NOT NULL,
                reason TEXT NOT NULL,
                issuer TEXT NOT NULL,
                date TIMESTAMPTZ DEFAULT NOW(),
                duration INTERVAL,
                end_date TIMESTAMPTZ,
                evidence TEXT,
                notes TEXT,
                status TEXT NOT NULL DEFAULT 'ACTIVE'
            );

            CREATE TABLE IF NOT EXISTS rules (
                id SERIAL PRIMARY KEY,
                category TEXT NOT NULL,
                content TEXT NOT NULL,
                version INTEGER NOT NULL DEFAULT 1,
                published BOOLEAN NOT NULL DEFAULT FALSE
            );
            '''
        )
