# This example is to show how to use the Mistral-7B-Instruct-v0.1 model to generate code.
# we use the same prompt used , but we need to add [/INST] to the user input to leverage instrution tuning
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda"  # the device to load the model onto

model = AutoModelForCausalLM.from_pretrained(
    "mistralai/Mistral-7B-Instruct-v0.1")
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")


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
         "content": f"<s>[INST] {prompt} [/INST]"},
    ]
    encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt")

    model_inputs = encodeds.to(device)
    model.to(device)

    generated_ids = model.generate(
        model_inputs, max_new_tokens=1000, do_sample=True)
    decoded = tokenizer.batch_decode(generated_ids)
    return decoded[0]
