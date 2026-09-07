from typing import List
from models.sanction import Sanction
from repositories.sanction_repository import SanctionRepository

class SanctionService:
    def __init__(self, sanction_repository: SanctionRepository):
        self.sanction_repository = sanction_repository

        async def create_sanction(self, sanction: Sanction) -> Sanction:
            return await self.sanction_repository.create_sanction(sanction)

            async def get_active_sanctions(self, member_discord_id: str, guild_id: str) -> List[Sanction]:
                return await self.sanction_repository.get_active_sanctions(member_discord_id, guild_id)

                async def revoke_sanction(self, sanction_id: int, revoked_by: str, revoked_at: str) -> Sanction:
                    return await self.sanction_repository.revoke_sanction(sanction_id, revoked_by, revoked_at)
