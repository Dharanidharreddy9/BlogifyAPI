
from fastapi import APIRouter, Query, Body, Depends
from .blogSchema import blogPost, PaginatedBlogResponse, updateBlogPost
from .model import getBlogInfo, searchBlogPosts, createBlog, updateBlog, deleteBlog
from typing import List
from Global.Responses import no_response, getBlogResp
from Global.validate import decodeJWT
from starlette import status


router = APIRouter(tags=['Blog Management'], prefix="/web/v1/blog")






# Get paginated blog information.
@router.get("/", responses=getBlogResp)
async def get_blogs(numOfData: int, pageNum:int):
    try:
        blogInfo = getBlogInfo(numOfData, pageNum)
        return blogInfo
    except Exception as e:
        return no_response


# Search for blog posts based on keywords.
@router.get("/searchPosts")
async def search_blog_posts(keywords: str = Query(..., title="Keywords", description="Comma-separated keywords for search")):
    try:
        keyword_list = keywords.split(',')
        blogs = searchBlogPosts(keyword_list)
        return blogs
    except Exception as e:
        print(e, "error")
        return no_response
    

# Create a new blog post.
@router.post("/createBlog", status_code=status.HTTP_201_CREATED)
async def post_blog(blog: blogPost, token: str = Depends(decodeJWT)):
    try:
        username = token['username']
        return createBlog(dict(blog), username)
    except Exception as e:
        return no_response
    

# Update an existing blog post.
@router.put("/updateBlog")
async def update_blog(updateBlogSchema: updateBlogPost,
                      post_code: str = Query(..., post_code="The post code of the blog to update"),
                    token: str = Depends(decodeJWT)):
    try:
        return updateBlog(post_code, updateBlogSchema)
    except Exception as e:
        print(e, "errro")
        return no_response


# Delete an existing blog post.
@router.delete("/deleteBlog", response_model=dict)
async def delete_blog(post_code: str = Query(..., post_code="The post code of the blog to delete"), 
                    token: str = Depends(decodeJWT)):
    try:
        return deleteBlog(post_code)
    except Exception as e:
        return no_response