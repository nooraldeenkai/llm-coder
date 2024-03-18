from openai import OpenAI
from app.models import Feedback
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)


def get_answer(prompt):

    messages = [
        {
            "role": "system",
                    "content": "you're a smart coding assistant bot designed to generate code that adhere to the user's specifications.\
                                You should only generate code that adheres to the user's specifications. \
                                You should only generate the code and do not respond with any other messages. \
                                "
        },
        {"role": "user",
                 "content": prompt},
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages

    )

    return response.choices[0].message.content


def submit_feedback(feedback: Feedback):
    messages = [
        {
            "role": "system",
                    "content": "you're a smart coding assistant bot designed to generate code that adhere to the user's specifications.\
                                You should only generate code that adheres to the user's specifications. \
                                You should not generate code that is not related to the user's specifications. \
                                You should not generate code that is not related to the user's specifications. \
                                You should only generate the code and do not respond with any other messages. \
                                "
        },
        {"role": "user",
                 "content": feedback.question},
        {"role": "system",
                 "content": feedback.answer},
        {"role": "user",
                 "content": feedback.feedback},
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages

    )

    return response.choices[0].message.content
