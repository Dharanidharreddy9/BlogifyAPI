from config import blog_posts_collection, comments_collection
from Global.Responses import no_response, success_created
from datetime import datetime
from pydantic import BaseModel
from .schema import Comment
from typing import List
from ..blogPostsManage.blogSchema import list_serial
from fastapi.responses import JSONResponse





# Adds a comment to a blog post identified by the given post_code.
def addCommentToPost(post_code: str, comment_data: Comment, username):
    """
    Adds a comment to a blog post.

    Args:
        post_code (str): The post code of the blog post to which the comment is added.
        comment_data (Comment): Data for the comment.

    Returns:
        dict: Response indicating success or failure.
    """
    try:
        blog_post = comments_collection.find_one({"postCode": post_code})
        
        if blog_post:
            comments_collection.update_one({"postCode": post_code},
                                            {"$push": {"comments": {
                                                "comment": comment_data.commentText,
                                                "created_at": datetime.utcnow()
                                            }}})
        else:
            comments_collection.insert_one({"postCode": post_code,
                                            "username": username,
                                            "comments": [{                    
                                                "comment": comment_data.commentText,
                                                "created_at": datetime.utcnow()
                                            }]})

        return success_created
    except Exception as e:
        return no_response


# Retrieves the most commented blog posts with comments count greater than or equal to the specified limit.
def getMostCommentedPosts(limit: int = 5):
    """
    Retrieves the most commented blog posts.

    Args:
        limit (int): The minimum number of comments a blog post should have to be considered.

    Returns:
    """
    try:
        # pipeline = [{"$unwind": "$comments"},
        #             {"$group": {
        #                 "_id": "$postCode",
        #                 "comments_count": {"$sum": 1},
        #             }},
        #             {"$match": {"comments_count": {"$gte": limit}}},
        #             {"$sort": {"comments_count": -1}},
        #             {"$limit": limit},]
        # most_commented_post_codes = [result["_id"] for result in comments_collection.aggregate(pipeline)]
        # most_commented_posts = list_serial(blog_posts_collection.find({"postCode": {"$in": most_commented_post_codes}}))
        # return most_commented_posts
        return JSONResponse(content={"message": "work in progess"}, status_code=400)
    except Exception as e:
        print(e, "error")
        return no_response