import streamlit as st
from openai import OpenAI

import base_prompts as bp

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
back = st.button("<< Go back")

if back:
    st.switch_page("app.py")

main_topic = "What responsibility should parents have in regulating their kids social media use?"

if "messages" not in st.session_state:
    st.session_state.messages = []

    # send instructions to agent
    st.session_state["messages"].append({
        "role": "system", "content": bp.THESIS_ASSESSMENT_SYSTEM_INSTRUCTIONS
    })

    welcome_message = f'We will construct your thesis together around the \
    {main_topic}. What do you think about the topic?'
    st.session_state.messages.append({"role": "assistant", "content": welcome_message})


for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = client.chat.completions.create(model="gpt-4o-mini", messages=st.session_state.messages)
    msg = response.choices[0].message.content

    st.chat_message("assistant").write(msg)
    st.session_state.messages.append({"role": "assistant", "content": msg})
