from config import blog_posts_collection, tags_collection
from Global.Responses import success_created, no_response
from typing import List
from ..blogPostsManage.blogSchema import list_serial




def addTagsToPost(post_code: str, tags: List[str], username):
    """
    Add tags to a blog post. If the post does not exist, create it with the provided tags.

    Args:
        post_code (str): The post code of the blog post.
        tags (List[str]): List of tags to add.

    Returns:
        dict: Response indicating success or failure.
    """
    try:
        blog_post = tags_collection.find_one({"postCode": post_code})
        if not blog_post:
            tags_collection.insert_one({"username": username, "postCode": post_code, "tags": tags})
            return success_created
        existing_tags = blog_post.get("tags", [])
        updated_tags = list(set(existing_tags + tags))

        tags_collection.update_one({"postCode": post_code},
                                    {"$set": {"username": username, "tags": updated_tags}}
                                    )

        return success_created
    except Exception as e:
        return no_response
    


def getPostsByTag(tag: str):
    """
    Retrieve blog posts with a specific tag.

    Args:
        tag (str): The tag to search for.

    Returns:
        list: List of blog posts with the specified tag.
    """
    try:
        posts_with_tag = tags_collection.find({"tags": tag})
        post_codes = [post["postCode"] for post in posts_with_tag]

        blog_posts_cursor = blog_posts_collection.find({"postCode": {"$in": post_codes}})
        blogs = list_serial(blog_posts_cursor)
        return blogs
    except Exception as e:
        return no_response