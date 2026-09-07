import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "")
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://rammohq:change_me@127.0.0.1:5432/rammohq",
    )
    GUILD_ID = int(os.getenv("GUILD_ID", "0"))

    RANKS = {
        10: "Don",
        9: "Underboss",
        8: "Consigliere",
        7: "Caporegime",
        6: "Capo",
        5: "Instructor",
        4: "Made Man",
        3: "Soldier",
        2: "Associate",
        1: "Recruit",
    }

    FUNCTIONS = [
        "Vice",
        "Leader",
        "Instructor",
        "Recruiter",
        "War Leader",
        "Business",
        "Event Team",
        "Administration",
        "Media",
        "Moderation",
        "Sanktioniert",
    ]

    @classmethod
    def validate(cls) -> None:
        missing = []
        if not cls.DISCORD_TOKEN:
            missing.append("DISCORD_TOKEN")
        if not cls.GUILD_ID:
            missing.append("GUILD_ID")
        if not cls.DATABASE_URL:
            missing.append("DATABASE_URL")

        if missing:
            raise RuntimeError(
                "Fehlende Umgebungsvariablen: " + ", ".join(missing)
            )
