from pydantic import BaseModel, Field, StrictStr
from datetime import datetime
from typing import List, Optional





class blogPost(BaseModel):
    postCode: Optional[StrictStr] = Field(title="Post Code",description="provide post code,this is not a mandatory field")
    title: str = Field(title="Title", description="Provide the title for the blog post, this is a mandatory field")
    content: str = Field(title="Content", description="Provide the content for the blog post, this is a mandatory field")
    author: str = Field(title="Author", description="Provide the author of the blog post, this is a mandatory field")
    # creation_date: datetime = Field(title="Creation Date", description="Provide the creation date of the blog post, this is a mandatory field")
    # tags: List[str] = Field(title="Tags", description="Provide a list of tags for the blog post, this is an optional field")



class PaginatedBlogResponse(BaseModel):
    blogs: List[blogPost]
    total_count: int = Field(title="Total Count", description="Total number of blog posts")
    page: int = Field(title="Page", description="Current page number")


class updateBlogPost(BaseModel):
    title: str = Field(title="Title", description="Provide the title for the blog post, this is a mandatory field")
    content: str = Field(title="Content", description="Provide the content for the blog post, this is a mandatory field")
    author: str = Field(title="Author", description="Provide the author of the blog post, this is a mandatory field")
    # update_date: datetime = Field(title="Creation Date", description="Provide the creation date of the blog post, this is a mandatory field")



def individual_serial(blog) -> dict:
    return {
        "id": str(blog["_id"]),
        "postCode": blog["postCode"],
        "title": blog["title"],
        "content": blog["content"],
        "author": blog["author"],
        "creation_date": blog["creation_date"]
        # "tags": blog["tags"]
    }

def list_serial(blogs) -> list:
    return [individual_serial(blog) for blog in blogs]
