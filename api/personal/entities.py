import pydantic


class PostContactData(pydantic.BaseModel):
    sender_name: str
    sender_email: pydantic.EmailStr
    message: str