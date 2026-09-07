from dataclasses import dataclass

@dataclass
class AuditLog:
    log_id: int
    actor_discord_id: int
    action: str
    target_discord_id: int
    old_value: str
    new_value: str
    reason: str
    timestamp: str
