from pydantic import BaseModel, EmailStr


class PostGuestSubscribeData(BaseModel):
    email: EmailStr
    topic: str