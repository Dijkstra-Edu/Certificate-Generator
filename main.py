import uvicorn
import httpx
from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

#----------------------------------GET USERNAME(WITH TEST USERNAME)---------------------------------------------------
@app.get("/get-visitor-username")
async def get_visitor_username(request: Request):
    referer = request.headers.get("referer", "")
    if "github.com/" in referer:
        username = referer.split("github.com/")[-1].split("/")[0]
        return {"github_username": username}
    raise HTTPException(400, detail="Not visiting from GitHub")

@app.get("/test-github-username") # CALL THIS FOR TESTING 
async def test_endpoint():
    async with httpx.AsyncClient() as client:
        # Simulate a request coming from GitHub
        response = await client.get(
            "http://localhost:8000/get-visitor-username",
            headers={"Referer": "https://github.com/SJ-Cipher"} # NAME CAN BE CHANGED HERE FOR TESTING
        )
        return response.json()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)