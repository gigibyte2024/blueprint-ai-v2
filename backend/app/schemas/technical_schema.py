from pydantic import BaseModel
from typing import List, Dict


class TechnicalSchema(BaseModel):
    tech_stack: Dict[str, str]

    database_tables: Dict[str, List[str]]

    api_endpoints: List[str]

    folder_structure: str