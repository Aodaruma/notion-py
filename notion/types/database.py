from typing import TypedDict
from datetime import datetime

from .user import User

class Database(TypedDict):
    id: str
    created_time: datetime
    created_by: User
    last_edited_time: datetime
    last_edited_by: User
    title: RichText
    description: RichText
    icon: File
    cover: File
    properties: Dict[str, Property]
    parent: Dict[str, str]
    url: str
    archived: bool
    is_inline: bool
