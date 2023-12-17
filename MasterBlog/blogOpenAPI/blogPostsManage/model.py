from pydantic import BaseModel
from typing import List
from datetime import datetime
from config import blog_posts_collection, comments_collection
from Global.Responses import no_response, no_data, success_created, success_ok,  \
                                code_exists
from .blogSchema import list_serial
from ..userRegistration.model import generateCode







def getBlogInfo(numOfData: int = 10, pageNum: int = 1):
    try:
        skip = (pageNum - 1) * numOfData
        blogs_cursor = blog_posts_collection.find().skip(skip).limit(numOfData)
        print(blogs_cursor, "blogs_cursor")
        blogs = list_serial(blogs_cursor)
        total_count = blog_posts_collection.count_documents({})

        response = {'blogs': blogs,
                    'total_count': total_count,
                    'page': pageNum}
        return response
    except Exception as e:
        return no_response
    

def getMostCommentedPosts(limit: int = 5):
    try:
        most_commented_posts_cursor = blog_posts_collection.find().sort("comments_count", -1).limit(limit)
        most_commented_posts = list_serial(most_commented_posts_cursor)
        return most_commented_posts
    except Exception as e:
        return no_response


# def searchBlogPosts(keywords: List[str]):
#     try:
#         print(keywords, "keywords")
#         query = {"$text": {"$search": " ".join(keywords)}}
#         print(query, "query")
#         blogs_cursor = blog_posts_collection.find(query)
#         blogs = list_serial(blogs_cursor)
#         print(blogs, "blogs")
#         return blogs
#     except Exception as e:
#         print(e, "error")
#         return no_response


def createBlog(blogData):
    try:
        if blogData:
            if 'postCode' not in blogData or blogData['postCode'] is None or blogData['postCode'] == "":
                blogData['postCode']= generateCode(range_=6, prefix='pt')

            if 'postCode' in blogData:
                if not blogData['postCode'].lower().startswith('pt_'):
                    blogData['postCode'] = 'pt_' + blogData['postCode']

            is_post_code = blog_posts_collection.find_one({"postCode": blogData['postCode']})
            if is_post_code:
                return code_exists

            blogData['createdByDate'] = datetime.utcnow()
            blog_posts_collection.insert_one(blogData)        
            return success_created
        else:
            return no_data
    except Exception as e:
        return no_response


def updateBlog(post_code, updated_data):
    try:
        updated_data_dict = updated_data.dict()
        updated_data_dict['updatedByDate'] = datetime.utcnow()

        result = blog_posts_collection.update_one({"postCode": post_code},
                                                    {"$set": {"title": updated_data_dict['title'],
                                                            "content": updated_data_dict['content'],
                                                            "author": updated_data_dict['author'],
                                                            "updatedByDate": updated_data_dict['updatedByDate']}}
                                                    )
        if result.modified_count > 0:
            return success_ok
        else:
            return no_data
    except Exception as e:
        return no_response


def deleteBlog(post_code):
    try:
        result = blog_posts_collection.delete_one({"postCode": post_code})
        if result.deleted_count > 0:
            return success_ok
        else:
            return no_data
    except Exception as e:
        return no_response