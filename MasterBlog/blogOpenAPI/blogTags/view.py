from fastapi import APIRouter, Depends, Query
from .model import addTagsToPost, getPostsByTag
from Global.Responses import no_response
from Global.validate import decodeJWT
from typing import List

router = APIRouter(tags=['Blog tags'], prefix="/web/v1/tags")



# Add tags to a specific blog post.
@router.post("/addtags")
async def add_tags(tags: List[str],
                    post_code: str = Query(..., title="Post Code", description="Provide the post code for the blog post"),
                    token: str = Depends(decodeJWT)):
    try:            
        username = token['username']
        result = addTagsToPost(post_code, tags, username)
        return result
    except Exception as e:
        return no_response


# Filter blog posts by a specific tag.
@router.get("/filterByTag", response_model=list)
async def filter_posts_by_tag(tag: str = Query(..., title="Tag", description="Provide the tag to filter posts")):
    try:
        blog_posts = getPostsByTag(tag)
        return blog_posts

    except Exception as e:
        print(e, "error")
        return no_response