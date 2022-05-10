from fastapi import FastAPI
import uvicorn
from routs import facts_about,mails

app = FastAPI()

app.include_router(facts_about.router)
app.include_router(mails.router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=True,
        port=8081
    )
