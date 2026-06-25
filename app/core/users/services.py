from dataclasses import dataclass
from typing import Optional

from sqlalchemy import select
from app.core.users.models import User
from app.core.users.constants import RolesEnum
from app.core.users.repositories import UserRepository


@dataclass
class UserService:
    repository: UserRepository

    async def register_visitor(self, user_id: int) -> None:
        await self.repository.create_user_if_not_exist(user_id)

    async def is_waiter(self, user_id: int) -> bool:
        """Проверяет, помечен ли пользователь как официант (is_waiter=True)"""
        async with self.repository.database.session() as session:
            query = select(User.is_waiter).where(User.id == user_id)
            result = await session.scalar(query)
            return result is True

    async def get_user_ids_for_role(self, role: RolesEnum) -> list[int]:
        match role:
            case RolesEnum.waiter:
                return await self.repository.get_waiter_user_ids()
            case _:
                raise ValueError("Unable to fetch user ids for role", role)
