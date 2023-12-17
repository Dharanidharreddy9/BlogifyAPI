from config import blog_posts_collection, comments_collection
from Global.Responses import no_response, success_created
from datetime import datetime
from pydantic import BaseModel
from .schema import Comment





# Adds a comment to a blog post identified by the given post_code.
def addCommentToPost(post_code: str, comment_data: Comment):
    """
    Adds a comment to a blog post.

    Args:
        post_code (str): The post code of the blog post to which the comment is added.
        comment_data (Comment): Data for the comment.

    Returns:
        dict: Response indicating success or failure.
    """
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
        return True

    except Exception as e:
        print(e, "error")
        return no_response