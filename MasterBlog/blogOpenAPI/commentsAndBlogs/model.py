from pydantic import BaseModel
from typing import List
from datetime import datetime
from config import comments_collection





class Comment(BaseModel):
    user: str
    text: str
    creation_date: datetime = datetime.utcnow()




def add_comment_to_post(post_id: str, comment: Comment):
    # Implement the logic to add a comment to a blog post
    pass
