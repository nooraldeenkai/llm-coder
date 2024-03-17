from fastapi import FastAPI
from app import models
from app.services import get_answer, get_history, delete_history, submit_feedback
# from app.config import engine
from fastapi.staticfiles import StaticFiles
# models.Base.metadata.create_all(bind=engine)
from fastapi.middleware.cors import CORSMiddleware
from app.models import Feedback

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory="static"), name="index.html")



@app.post("/get_answer")
async def code_generation(prompt: str):
    """
    function to send the question to the LLM and get back the text response
    """
    answer = get_answer(prompt)

    return answer


@app.post("/feedback")
async def receive_feedback(feedback: Feedback):
    # Here you can process the received feedback
    # For now, we'll just print it
    reply = submit_feedback(feedback)
    print(f"Received feedback: {feedback}")
    return {"message": reply}


@app.get("/get_history")
async def history():
    """
    function to get the history of the user's generated code and the user's question.
    """
    return None


@app.get("/delete_history")
async def delete():
    """
    function to delete the history of the user's generated code and the user's question. 
    """
    return None
