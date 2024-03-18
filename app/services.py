from openai import OpenAI
from app.models import History
from app.config import OPENAI_API_KEY


client = OpenAI()
client.api_key = OPENAI_API_KEY


def get_answer(prompt, conv_history: dict,):
    # get history
    if conv_history:
        messages = [
            {
                "role": "system",
                        "content": "you're a smart coding assistant bot designed to generate code that adhere to the user's specifications.\
                                    You should only generate code that adheres to the user's specifications. \
                                    You should only generate the code and do not respond with any other messages. \
                                    You're given the previous conversation history and the user's question along with the user feedback. \
                                    make sure your next answer improves from the previous answer.\
                                    "
            },
            {"role": "user",
             "content": conv_history.question},
            {"role": "system",
             "content": conv_history.answer},
            {"role": "user",
             "content": conv_history.feedback},
            {"role": "user",
             "content": prompt}
        ]
    else:
        messages = [
            {
                "role": "system",
                        "content": "you're a smart coding assistant bot designed to generate code that adhere to the user's specifications.\
                                    You should only generate code that adheres to the user's specifications. \
                                    You should only generate the code and do not respond with any other messages. \
                                    "
            },
            {"role": "user",
             "content": prompt}
        ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages

    )

    return response.choices[0].message.content
