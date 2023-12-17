# This file is responsible for running the whole application.
import uvicorn
from MasterBlog.main import create_app




# Create the FastAPI application using the `create_app` factory function.
app = create_app()




# Check if this script is the main entry point.
if __name__ == "__main__":
    uvicorn.run("run:app", reload=True)
