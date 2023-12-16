# This file is responsible for running the whole application.
import uvicorn
from MasterBlog.main import create_app



app = create_app()



if __name__ == "__main__":
    uvicorn.run("run:app", reload=True)
