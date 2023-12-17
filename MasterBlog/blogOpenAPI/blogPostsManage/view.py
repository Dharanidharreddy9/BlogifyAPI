
from fastapi import APIRouter, Query, Body, Depends
from .blogSchema import blogPost, PaginatedBlogResponse
from .model import getBlogInfo, getMostCommentedPosts, createBlog, updateBlog, deleteBlog
from typing import List
from Global.Responses import no_response
from Global.validate import decodeJWT
from starlette import status


router = APIRouter(tags=['Blog Management'], prefix="/web/v1/blog")


# Get the blog Info
@router.get("/", response_model=PaginatedBlogResponse)
async def get_blogs(numOfData: int, pageNum:int):
    try:
        blogInfo = getBlogInfo(numOfData, pageNum)
        print(blogInfo, "blogInfo")
        return blogInfo
    except Exception as e:
        print(e, "error")
        return no_response


@router.get("/mostCommentedPosts", response_model=List[blogPost])
async def most_commented_posts(limit: int = Query(5, ge=1, le=10)):
    try:
        return getMostCommentedPosts(limit)
    except Exception as e:
        print(e, "error")
        return no_response


# @router.get("/searchBlogPosts/{keywords}")
# async def search_blog_posts(keywords: str):
#     try:
#         keyword_list = keywords.split(',')
#         blogs = searchBlogPosts(keyword_list)
#         return blogs
#     except Exception as e:
#         print(e, "error")
#         return no_response
    

@router.post("/createBlog", status_code=status.HTTP_201_CREATED)
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