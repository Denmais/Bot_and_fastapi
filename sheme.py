from pydantic import BaseModel


class Base(BaseModel):
    message: str
