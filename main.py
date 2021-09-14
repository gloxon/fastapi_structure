from application.factory import create_app 
import uvicorn

# create an instance of the Fastapi app 
app = create_app()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
