from pydantic import BaseModel
from typing import List


class UISchema(BaseModel):
    screens: List[str]
    user_flow: List[str]
    ui_prompt: str
    design_system: List[str]