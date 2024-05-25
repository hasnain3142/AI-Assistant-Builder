from pydantic import BaseModel, Field, ValidationError, root_validator
from typing import Any, Dict, Literal, Optional

class QueryRequestModel(BaseModel):
    chatbot_name: Literal['lawyer', 'medical']
    pre_filter: Optional[Dict[str, Any]] = Field(None, description='A JSON object with only one key "category" or None')
    query: str

    @root_validator(pre=True)
    def check_pre_filter(cls, values):
        pre_filter = values.get('pre_filter')
        if pre_filter is not None:
            if not isinstance(pre_filter, dict) or len(pre_filter) != 1 or 'category' not in pre_filter:
                raise ValueError('pre_filter must contain exactly one key: "category" or be None')
        return values