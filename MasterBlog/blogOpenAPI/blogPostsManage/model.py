from pydantic import BaseModel
from typing import List
from datetime import datetime
from config import blog_posts_collection, comments_collection
from Global.Responses import no_response, no_data, success_created, success_ok,  \
                                code_exists
from .blogSchema import list_serial
from ..userRegistration.model import generateCode






# Function to retrieve blog information with pagination.
def getBlogInfo(numOfData: int = 10, pageNum: int = 1):
    """
    Retrieve information about blog posts with pagination.

    Args:
        numOfData (int): Number of blog posts to retrieve per page.
        pageNum (int): Page number.

    Returns:
        dict: Response containing paginated blog information.
    """
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


# Function to search for blog posts based on keywords in title, content, and author.
def searchBlogPosts(keywords: List[str]):
    """
    Search for blog posts based on keywords in title, content, and author.

    Args:
        keywords (List[str]): List of keywords to search for.

    Returns:
        list: List of blog posts matching the search criteria.
    """
    try:
        query_conditions = []

        for keyword in keywords:
            condition = {"$or": [{"title": {"$regex": keyword, "$options": "i"}},
                                {"content": {"$regex": keyword, "$options": "i"}},
                                {"author": {"$regex": keyword, "$options": "i"}}
                                ]}
            query_conditions.append(condition)

        query = {"$and": query_conditions}
        blogs_cursor = blog_posts_collection.find(query)
        blogs = list_serial(blogs_cursor)
        return blogs

    except Exception as e:
        return no_response


# Function to create a new blog post.
def createBlog(blogData, userCode):
    """
    Create a new blog post.

    Args:
        blogData (dict): Data for the new blog post.

    Returns:
        dict: Response indicating success or failure.
    """
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
            
            blogData['userCode'] = userCode
            blogData['creation_date'] = datetime.utcnow()
            blog_posts_collection.insert_one(blogData)        
            return success_created
        else:
            return no_data
    except Exception as e:
        return no_response


# Function to update a blog post by post_code.
def updateBlog(post_code, updated_data):
    """
    Update a blog post by post_code.

    Args:
        post_code (str): The post code of the blog post to update.
        updated_data (updateBlogPost): Data to update in the blog post.

    Returns:
        dict: Response indicating success or failure.
    """
    try:
        updated_data_dict = updated_data.dict()
        updated_data_dict['updated_Date'] = datetime.utcnow()

        result = blog_posts_collection.update_one({"postCode": post_code},
                                                    {"$set": {"title": updated_data_dict['title'],
                                                            "content": updated_data_dict['content'],
                                                            "author": updated_data_dict['author'],
                                                            "updated_Date": updated_data_dict['updated_Date']}}
                                                    )
        if result.modified_count > 0:
            return success_ok
        else:
            return no_data
    except Exception as e:
        return no_response


# Function to delete a blog post by post_code.
def deleteBlog(post_code):
    """
    Delete a blog post by post_code.

    Args:
        post_code (str): The post code of the blog post to delete.

    Returns:
        dict: Response indicating success or failure.
    """
    try:
        result = blog_posts_collection.delete_one({"postCode": post_code})
        if result.deleted_count > 0:
            return success_ok
        else:
            return no_data
    except Exception as e:
        return no_response