import timestamp as timestamp
from pydantic import BaseModel, PositiveInt


class DocumentsSchema(BaseModel):
    id: PositiveInt
    name: str
    text: str
    inserted_at: timestamp
    updated_at: timestamp


