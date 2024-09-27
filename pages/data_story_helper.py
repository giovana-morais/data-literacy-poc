import streamlit as st

import base64
import glob
import os
from io import StringIO

import streamlit as st
from openai import OpenAI
from st_clickable_images import clickable_images

import base_prompts as bp

st.set_page_config(
    page_title="Chatbot",
    page_icon=":robot:",
    # initial_sidebar_state="collapsed",
    )

# load images
evidence_paths = glob.glob("evidence/*.png")
evidence_images = []
for file in evidence_paths:
    with open(file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
        evidence_images.append(f"data:image/jpeg;base64,{encoded}")

uploaded_files = st.file_uploader(
            "Choose your discussion files", accept_multiple_files=True
            )

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

for uploaded_file in uploaded_files:
    file_content = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write("filename:", uploaded_file.name)
    # st.write(file_content)
    st.chat_message("assistant").write(file_content)


# load img_index selected from previous page
# img_index = int(st.query_params.get("img_index", None))
# chosen_evidence = evidence_images[img_index]
# st.image(chosen_evidence)

# with st.sidebar:
#     st.markdown("[View the source code](https://github.com/mewtyunjay/data-literacy-poc)")
#     st.markdown("When you click on \"Save Evidence\", we create a summary of the conversation you had with the agent and then you can use this summary to create your data story")
#     # save_evidence = st.button("Save S")


# # send instructions to agent
# st.session_state["messages"] = [
#     {"role": "system", "content": bp.SYSTEM_INSTRUCTIONS}
# ]

# welcome_message = f'You need to build an argument about \
# "{main_topic}" \
# and your starting point of view is "{initial_argument}". How do you think the image \
# you chose related to your main thesis?'

# st.chat_message("assistant").write(welcome_message)

# # provide topic and thesis as context to the agent
# st.session_state.messages.append({
#     "role": "user",
#     "content": f"We're discussing {main_topic} and my main thesis is \"{initial_argument}\""})

# # provide selected image as context
# content = []
# content.append({
#     "type": "image_url",
#     "image_url": {
#         "url": f"{chosen_evidence}"
#         }
#     })

# # display message history, but
# # skip messages that were only providing context to the agent
# for idx, msg in enumerate(st.session_state.messages):
#     if idx < 2:
#         continue
#     st.chat_message(msg["role"]).write(msg["content"])

# if prompt := st.chat_input():
#     text_content = {"type": "text", "text": prompt}
#     content = [text_content]

#     st.session_state.messages.append({"role": "user", "content": content})
#     st.chat_message("user").write(prompt)
#     response = client.chat.completions.create(model="gpt-4o-mini", messages=st.session_state.messages)
#     msg = response.choices[0].message.content

#     st.session_state.messages.append({"role": "assistant", "content": msg})
#     st.chat_message("assistant").write(msg)
