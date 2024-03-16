from openai import OpenAI


client = OpenAI(api_key='')


def get_answer(prompt):

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
                 "content": prompt},
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages

    )

    return response.choices[0].message.content


def get_history():
    return None


def delete_history():
    return None
