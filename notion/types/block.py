from typing import TypedDict, Dict, Literal, Union
from datetime import datetime

from .user import User

BlockType = Literal["paragraph", "heading_1", "heading_2", "heading_3", "bulleted_list_item", "numbered_list_item", "to_do", "toggle", "child_page", "unsupported"]

class Block(TypedDict):
    id: str
    parent: Dict[str, str]
    type: BlockType
    created_time: datetime
    created_by: User
    last_edited_time: datetime
    last_edited_by: User
    archived: bool
    has_children: bool
    data: Dict[str, Union[str, int, bool, dict]]