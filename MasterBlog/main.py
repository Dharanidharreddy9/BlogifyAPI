from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from typing import List, Optional

# Import your models, dependencies, and routes here

app = FastAPI(
    title="BlogifyAPI",
    description="API for managing blog users, posts, comments, and tags.",
    version="1.0.0",
    openapi_tags=[{"name": "Users", "description": "APIs related to user management"}],
    redoc_url=None,
)



# Custom exception handler for validation errors
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


# Register the exception handler
app.add_exception_handler(RequestValidationError, validation_exception_handler)


# Custom OpenAPI schema
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Your Blog API",
        version="1.0.0",
        description="API for managing blog users, posts, comments, and tags.",
        routes=app.routes,
    )
    # Customize your OpenAPI schema here
    openapi_schema["info"]["x-logo"] = {"url": "your_logo_url"}

    return openapi_schema


app.openapi = custom_openapi


def create_app():
    """
    Factory function to create and configure the FastAPI application.

    Returns:
        FastAPI: Configured FastAPI application.
    """

    from MasterBlog.blogOpenAPI.userRegistration import view as user_registration_view
    app.include_router(user_registration_view.router, tags=["Users"])

    from MasterBlog.blogOpenAPI.userLogin import view as user_login_view
    app.include_router(user_login_view.router, tags=["Users"])

    from MasterBlog.blogOpenAPI.blogPostsManage import view as blog_posts_manage_view
    app.include_router(blog_posts_manage_view.router, tags=["Posts"])

    from MasterBlog.blogOpenAPI.blogComments import view as blog_comments_view
    app.include_router(blog_comments_view.router, tags=["Comments"])

    from MasterBlog.blogOpenAPI.blogTags import view as blog_tags_view
    app.include_router(blog_tags_view.router, tags=["Tags"])

    return app


# Integerating Redoc documentation with custom favicon
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Your Blog API",
        swagger_favicon_url="your_swagger_favicon_url",
    )


# Integerating Redoc documentation with custom favicon
@app.get("/", include_in_schema=False)
async def custom_redoc_html():
    return get_redoc_html(
        openapi_url="/openapi.json",
        title="Your Blog API",
        redoc_favicon_url="your_redoc_favicon_url",
    )
