from pydantic import BaseModel




class Comment(BaseModel):
    commentText: str
