from fastapi import FastAPI
from app.services import get_answer, get_history, delete_history

app = FastAPI()


@app.post("/get_answer")
async def code_generation(prompt: str):
    """
    function to send the question to the LLM and get back the text response
    """
    answer = get_answer(prompt)

    return answer


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
