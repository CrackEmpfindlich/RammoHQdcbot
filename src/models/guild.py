from dataclasses import dataclass

@dataclass
class Guild:
    id: str
    name: str
    owner_id: str
    created_at: str
