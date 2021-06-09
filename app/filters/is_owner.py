from dataclasses import dataclass

from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message
from app.config import OWNER_ID


@dataclass
class IsOwner(BoundFilter):
    """
    Filtered message should be advertising
    """

    key = "is_owner"

    is_owner: bool

    async def check(self, message: Message) -> bool:
        if message.from_user.id == int(OWNER_ID):
            return self.is_owner and True
        else:
            return False
