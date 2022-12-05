from typing import TypedDict

class Comment(TypedDict):
    id: str
    parent: dict
    properties: dict
    url: str