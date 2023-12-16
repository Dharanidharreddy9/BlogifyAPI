
from fastapi import APIRouter, Query, Body, Depends
from .model import blogPost, PaginatedBlogResponse
from .blogSchema import list_serial
from .model import getBlogInfo, createBlog, updateBlog, deleteBlog
from typing import List
from Global.Responses import no_response
from Global.validate import decodeJWT


router = APIRouter(tags=['Blog Management'], prefix="/web/v1/blog")


# Get the blog Info
@router.get("/", response_model=PaginatedBlogResponse)
async def get_blogs(numOfData: int, pageNum:int, token: str = Depends(decodeJWT)):
    try:
        blogInfo = getBlogInfo(numOfData, pageNum)
        print(blogInfo, "blogInfo")
        return blogInfo
    except Exception as e:
        print(e, "error")
        return no_response


@router.post("/createBlog")
async def post_blog(blog: blogPost, token: str = Depends(decodeJWT)):
    try:
        return createBlog(dict(blog))
    except Exception as e:
        return no_response
    

@router.put("/updateBlogByTitle", response_model=dict)
async def update_blog_by_title(title: str = Query(..., title="The title of the blog to update"),
                               updated_data: dict = Body(..., description="Updated blog data"),
                               token: str = Depends(decodeJWT)):
    try:
        return updateBlog(title, updated_data)
    except Exception as e:
        return no_response


@router.delete("/deleteBlogByTitle", response_model=dict)
async def delete_blog_by_title(title: str = Query(..., title="The title of the blog to delete"), 
                               token: str = Depends(decodeJWT)):
    try:
        return deleteBlog(title)
    except Exception as e:
        return no_response