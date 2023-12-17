from config import blog_posts_collection, comments_collection
from Global.Responses import no_response, success_created
from datetime import datetime
from pydantic import BaseModel
from .schema import Comment






def addCommentToPost(post_code: str, comment_data: Comment):
    try:
        blog_post = blog_posts_collection.find_one({"postCode": post_code})
        if not blog_post:
            return {"error": "Blog post not found", "status_code": 404}

        comments_collection.insert_one({"postCode": post_code,
                                        "text": comment_data.commentText,
                                        "created_at": datetime.utcnow()
                                    })

        return success_created
    except Exception as e:
        print(e, "error")
        return no_response
