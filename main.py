import time
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))


input = open("input.txt", "r")
output = open("output.txt", "w")
input_info = open("input_info.txt", "r")

print("Generating Response")
start = time.time()
completion = client.chat.completions.create(
    model = "gpt-4",
    n = 1,
    temperature = 1,
    messages = [
        {"role": "system", "content": input_info.read()},
        {"role": "user", "content": input.read()}
    ]
)
end = time.time()
output.write(completion.choices[0].message.content)
print("Finished!")
print("Response generated to " + output.name + " in " + str(round(end - start), 2) + " seconds")
