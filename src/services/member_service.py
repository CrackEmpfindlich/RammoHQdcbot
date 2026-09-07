from typing import List
from models.member import Member
from repositories.member_repository import MemberRepository

class MemberService:
    def __init__(self, member_repository: MemberRepository):
        self.member_repository = member_repository

        async def create_member(self, member: Member) -> Member:
            return await self.member_repository.create_member(member)

            async def get_member(self, discord_id: str, guild_id: str) -> Member:
                return await self.member_repository.get_member(discord_id, guild_id)

                async def update_member(self, member: Member) -> Member:
                    return await self.member_repository.update_member(member)
