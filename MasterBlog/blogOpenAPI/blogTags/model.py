from config import blog_posts_collection, tags_collection
from Global.Responses import success_created, no_response
from typing import List
from ..blogPostsManage.blogSchema import list_serial




def addTagsToPost(post_code: str, tags: List[str]):
    try:
        blog_post = tags_collection.find_one({"postCode": post_code})
        if not blog_post:
            tags_collection.insert_one({"postCode": post_code, "tags": tags})
            return success_created
        existing_tags = blog_post.get("tags", [])
        updated_tags = list(set(existing_tags + tags))

        tags_collection.update_one({"postCode": post_code},
                                    {"$set": {"tags": updated_tags}}
                                    )

        return success_created
    except Exception as e:
        return no_response
    


def getPostsByTag(tag: str):
    try:
        posts_with_tag = tags_collection.find({"tags": tag})
        post_codes = [post["postCode"] for post in posts_with_tag]

        blog_posts_cursor = blog_posts_collection.find({"postCode": {"$in": post_codes}})
        blogs = list_serial(blog_posts_cursor)
        return blogs
    except Exception as e:
        return no_response