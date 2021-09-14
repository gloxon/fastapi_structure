from fastapi import FastAPI
from .config import settings 


def create_app():
    app = FastAPI()

    from .blog import routes as blog_routes 
    from .session import routes as session_routes 

    app.include_router(blog_routes.router)
    app.include_router(session_routes.router)
    
    return app 
