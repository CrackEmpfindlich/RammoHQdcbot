import asyncio
import logging

import discord
from discord.ext import commands

from config import Config
from database import create_pool, init_db


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)


class RammoBot(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.guilds = True
        intents.members = True

        super().__init__(
            command_prefix="!",
            intents=intents,
        )

        self.db_pool = None

    async def setup_hook(self) -> None:
        self.db_pool = await create_pool()
        await init_db(self.db_pool)

        await self.load_extension("commands.setup")

        if Config.GUILD_ID:
            guild = discord.Object(id=Config.GUILD_ID)
            self.tree.copy_global_to(guild=guild)
            synced = await self.tree.sync(guild=guild)
            logging.info(
                "%s Slash Command(s) mit Guild %s synchronisiert.",
                len(synced),
                Config.GUILD_ID,
            )
        else:
            synced = await self.tree.sync()
            logging.info(
                "%s globale Slash Command(s) synchronisiert.",
                len(synced),
            )

    async def close(self) -> None:
        if self.db_pool is not None:
            await self.db_pool.close()

        await super().close()


bot = RammoBot()


@bot.event
async def on_ready() -> None:
    logging.info(
        "Logged in as %s (%s)",
        bot.user,
        bot.user.id if bot.user else "n/a",
    )


async def main() -> None:
    Config.validate()

    async with bot:
        await bot.start(Config.DISCORD_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
