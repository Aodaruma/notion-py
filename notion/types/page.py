from typing import TypedDict, Dict
from datetime import datetime

from .user import User


class Page(TypedDict):
    id: str
    created_time: datetime
    created_by: User
    last_edited_time: datetime
    last_edited_by: User
    icon: File
    cover: File
    properties: Dict[str, Property]
    parent: Dict[str, str]
    url: str
