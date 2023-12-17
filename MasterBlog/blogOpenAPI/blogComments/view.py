from fastapi import APIRouter, Depends, Query
from .model import addCommentToPost
from .schema import Comment
from Global.Responses import no_response
from Global.validate import decodeJWT




router = APIRouter(tags=['Blog Comments'], prefix="/web/v1/comments")



@router.post("/addComment")
async def add_comment(comment: Comment,
                    post_code: str = Query(..., title="Post Code", description="Provide the post code for the blog post"),    
                    token: str = Depends(decodeJWT)):
    try:            
        result = addCommentToPost(post_code, comment)
        return result
    except Exception as e:
        return no_response