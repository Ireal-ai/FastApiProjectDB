import timestamp as timestamp
from pydantic import BaseModel, PositiveInt


class DocumentsSchema(BaseModel):
    id: PositiveInt
    name: str
    text: str
    inserted_at: timestamp
    updated_at: timestamp


class RightsSchema(BaseModel):
    id: PositiveInt
    document_id: PositiveInt
    name: str
    text: str
    rights_from: timestamp
    rights_to: timestamp
    inserted_at: timestamp
    updated_at: timestamp
