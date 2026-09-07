from dataclasses import dataclass

@dataclass
class Sanction:
    id: int
    member_discord_id: str
    guild_id: str
    type: str
    reason: str
    issued_by: str
    issued_at: str
    expires_at: str
    revoked_by: str
    revoked_at: str
    is_active: bool
