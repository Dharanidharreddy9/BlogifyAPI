from fastapi import FastAPI




app = FastAPI()




def create_app():
    
    from MasterBlog.blogOpenAPI.userRegistration import view
    app.include_router(view.router)

    from MasterBlog.blogOpenAPI.userLogin import view
    app.include_router(view.router)

    from MasterBlog.blogOpenAPI.blogPostsManage import view
    app.include_router(view.router)


    return app
