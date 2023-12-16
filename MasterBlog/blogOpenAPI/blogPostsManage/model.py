from pydantic import BaseModel
from typing import List
from datetime import datetime
from config import blog_posts_collection
from Global.Responses import no_response, no_data, success_created, success_ok
from .blogSchema import list_serial


class blogPost(BaseModel):
    title: str
    content: str
    author: str
    creation_date : datetime
    tags: List[str] = []


class PaginatedBlogResponse(BaseModel):
    blogs: List[blogPost]
    total_count: int
    page: int
    num_of_data: int


def getBlogInfo(pageNum: int = 1, numOfData: int = 10):
    try:
        skip = (pageNum - 1) * numOfData
        blogs_cursor = blog_posts_collection.find().skip(skip).limit(numOfData)
        blogs = list_serial(blogs_cursor)
        total_count = blog_posts_collection.count_documents({})

        response = {'blogs': blogs,
                    'total_count': total_count,
                    'page': pageNum}
        return response
    except Exception as e:
        return no_response
    

def createBlog(blogData):
    try:
        if blogData:            
            blog_posts_collection.insert_one(blogData)        
            return success_created
        else:
            return no_data
    except Exception as e:
        return no_response


def updateBlog(title, updated_data):
    try:
        result = blog_posts_collection.update_one({"title": title}, {"$set": updated_data})
        if result.modified_count > 0:
            return success_ok
        else:
            return no_data 
    except Exception as e:
        return no_response


def deleteBlog(title):
    try:
        result = blog_posts_collection.delete_one({"title": title})
        if result.deleted_count > 0:
            return success_ok
        else:
            return no_data
    except Exception as e:
        return no_response