from typing import TypedDict, Dict, List, Optional, Literal, Union

from datetime import datetime


class Property(TypedDict):
    id: str
    type: str
    name: str
    description: str
    format: Optional[dict]
    options: Optional[dict]


class File(TypedDict):
