from fastapi import APIRouter, Depends, Query
from .model import addCommentToPost, getMostCommentedPosts
from .schema import Comment
from Global.Responses import no_response
from Global.validate import decodeJWT




router = APIRouter(tags=['Blog Comments'], prefix="/web/v1/comments")


# Route to add a comment to a blog post identified by the given post_code.
@router.post("/addComment")
async def add_comment(comment: Comment,
                    post_code: str = Query(..., title="Post Code", description="Provide the post code for the blog post"),    
                    token: str = Depends(decodeJWT)):
    try:            
        result = addCommentToPost(post_code, comment)
        return result
    except Exception as e:
        return no_response


# Route to retrieve the most commented blog posts with comments count greater than or equal to the specified limit.
@router.get("/mostCommentedPosts", response_model=list)
async def most_commented_posts(limit: int = 5):
    try:
        return getMostCommentedPosts(limit)
    except Exception as e:
        print(e, "error")
        return no_response