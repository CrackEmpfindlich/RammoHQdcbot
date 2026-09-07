from dataclasses import dataclass
from typing import List

@dataclass
class Member:
    discord_id: str
    guild_id: str
    status: str
    functions: List[str]
    rank: str
    created_at: str
    updated_at: str
