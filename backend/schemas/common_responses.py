from pydantic import BaseModel


class MessageResponseSchemaOut(BaseModel):
    message: str
