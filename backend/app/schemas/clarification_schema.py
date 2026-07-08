from pydantic import BaseModel
from typing import List


class ClarificationQuestions(BaseModel):
    questions: List[str]