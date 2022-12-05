from typing import TypedDict, List, Optional, Literal, Union

UserType = Literal["person", "bot"]

class User(TypedDict):
    id: str
    type: Union[List[UserType], None]
    name: Optional[str]
    avatar_url: str
    person: Optional[dict]
    bot: Optional[dict]
