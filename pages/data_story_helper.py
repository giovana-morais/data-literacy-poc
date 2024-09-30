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
    initial_sidebar_state="collapsed",
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

# send instructions to agent
st.session_state["messages"] = [
    {"role": "system", "content": bp.DATA_STORY_SYSTEM_INSTRUCTIONS}
]


for uploaded_file in uploaded_files:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    file_content = stringio.read()
    st.chat_message("assistant").write(f"Processing file {uploaded_file.name}")
    st.session_state.messages.append({"role": "user", "content": file_content})

st.chat_message("assistant").write("Input files processed. How can I help you with your story?")

# # display message history, but
# # skip messages that were only providing context to the agent
for idx, msg in enumerate(st.session_state.messages):
    if idx < len(uploaded_files)+1:
        continue
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    text_content = {"type": "text", "text": prompt}
    content = [text_content]

    st.session_state.messages.append({"role": "user", "content": content})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-4o-mini", messages=st.session_state.messages)
    msg = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
