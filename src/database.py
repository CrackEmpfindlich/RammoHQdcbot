import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

async def init_db():
    conn = await asyncpg.connect(os.getenv("DATABASE_URL"))
    await conn.execute("""
        CREATE TABLE IF NOT EXISTS guilds (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            owner_id TEXT NOT NULL,
            created_at TIMESTAMPTZ NOT NULL
        )
    """)
    await conn.execute("""
        CREATE TABLE IF NOT EXISTS members (
            discord_id TEXT NOT NULL,
            guild_id TEXT NOT NULL,
            status TEXT NOT NULL,
            rank TEXT NOT NULL,
            created_at TIMESTAMPTZ NOT NULL,
            updated_at TIMESTAMPTZ NOT NULL,
            PRIMARY KEY (discord_id, guild_id),
            FOREIGN KEY (guild_id) REFERENCES guilds (id)
        )
    """)
    await conn.execute("""
        CREATE TABLE IF NOT EXISTS sanctions (
            id SERIAL PRIMARY KEY,
            member_discord_id TEXT NOT NULL,
            guild_id TEXT NOT NULL,
            type TEXT NOT NULL,
            reason TEXT NOT NULL,
            issued_by TEXT NOT NULL,
            issued_at TIMESTAMPTZ NOT NULL,
            expires_at TIMESTAMPTZ,
            revoked_by TEXT,
            revoked_at TIMESTAMPTZ,
            is_active BOOLEAN NOT NULL,
            FOREIGN KEY (member_discord_id, guild_id) REFERENCES members (discord_id, guild_id)
        )
    """)
    await conn.execute("""
        CREATE TABLE IF NOT EXISTS ranks (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            level INTEGER NOT NULL,
            description TEXT
        )
    """)
    await conn.execute("""
        INSERT INTO ranks (name, level, description) VALUES
        ('Don', 10, 'The highest rank in the family'),
        ('Underboss', 9, 'Second in command'),
        ('Consigliere', 8, 'Advisor to the Don'),
        ('Caporegime', 7, 'Commander of a crew'),
        ('Capo', 6, 'Leader of a crew'),
        ('Instructor', 5, 'Teaches new members'),
        ('Made Man', 4, 'Full member of the family'),
        ('Soldier', 3, 'Active member'),
        ('Associate', 2, 'Associate member'),
        ('Recruit', 1, 'New member')
        ON CONFLICT (name) DO NOTHING
    """)
    await conn.execute("""
        CREATE TABLE IF NOT EXISTS audit_logs (
            id SERIAL PRIMARY KEY,
            actor_discord_id TEXT NOT NULL,
            action TEXT NOT NULL,
            target_discord_id TEXT NOT NULL,
            old_value TEXT,
            new_value TEXT,
            reason TEXT,
            timestamp TIMESTAMPTZ NOT NULL
        )
    """)
    await conn.close()

    if __name__ == "__main__":
        import asyncio
        asyncio.run(init_db())
