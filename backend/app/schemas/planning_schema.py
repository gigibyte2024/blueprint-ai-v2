from pydantic import BaseModel
from typing import List


class PlanningSchema(BaseModel):
    product_summary: str

    features: List[str]

    user_stories: List[str]

    functional_requirements: List[str]

    non_functional_requirements: List[str]

    success_metrics: List[str]