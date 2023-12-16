



def individual_serial(blog) -> dict:
    return {
        "id": str(blog["_id"]),
        "title": blog["title"],
        "content": blog["content"],
        "author": blog["author"],
        "creation_date": blog["creation_date"],
        "tags": blog["tags"]
    }

def list_serial(blogs) -> list:
    return [individual_serial(blog) for blog in blogs]
