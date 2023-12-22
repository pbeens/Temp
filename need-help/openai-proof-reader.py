'''
This program isn't working. It sends the request but then hangs.

Can anyone help me with it? 

This code was adapted from https://codecurrents.blog/article/2023-07-16. 

Issue has been created here: https://github.com/pbeens/Temp/issues/1

https://mstdn.ca/@pbeens
https://twitter.com/pbeens 
'''

'''
UPDATE 2023-12-19
This latest update works with a significantly shortened input file. For now I'm assuming the program works okay, within filesize limitations.
'''

import os
from openai import OpenAI

# Get the path of the directory where the script is located
dir_path = os.path.dirname(
    os.path.abspath(__file__)
)  # ensures it reads from the same directory

# Read the contents of the file
with open(os.path.join(dir_path, "file.txt"), "r") as f:
    text = f.read()

# Initialize the OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Define the system role and the request
system_role = "You are a proofreader for my personal blog posts."
model = "gpt-3.5-turbo-16k"
request = f"""Review and look for grammatical errors in the
following blog post. Clearly highlight the errors in your response:\n\n
{text}"""

# Define the messages to be sent to the OpenAI API
messages = [
    {
        "role": "system",
        "content": system_role,
    },
    {
        "role": "user",
        "content": request,
    },
]

# Send the request to the OpenAI API
print('sending request...')
response = client.chat.completions.create(
    messages=messages,
    model=model,
)

# Print the response from the OpenAI API
print(f"{response}")