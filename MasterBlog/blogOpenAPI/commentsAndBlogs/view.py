# from fastapi import APIRouter, Depends
# from .model import Comment, add_comment_to_post
# from Global.validate import decodeJWT




# router = APIRouter(tags=['Comments'])




# @router.post("/add-comment/{post_id}")
# async def add_comment(post_id: str, comment: Comment, token: str = Depends(decodeJWT)):
#     add_comment_to_post(post_id, comment)
#     return {"message": "Comment added successfully"}
