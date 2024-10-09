import base64
import glob
import os

import streamlit as st
from st_clickable_images import clickable_images

st.set_page_config(
    page_title="Evidence Selector",
    page_icon=":bookmark_tabs:",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.sidebar.header("Evidence Selector")

st.markdown("# Evidence Selector")

st.markdown("### What is your thesis?")
thesis = st.text_input(label="Thesis", placeholder="Example: I believe that parents should not allow teenagers to use social media because it is hurtful to their studies.")

if thesis != "":
    st.markdown("## Click on an image miniatures to see if bigger")
    st.markdown("### Once you're happy with your choice, click on the \"Discuss Image\" button to open a new tab with the AI agent")

    # define our two columns and make sure image_list is 2x the size of
    # image_selection
    image_list, image_selection = st.columns((2,2), gap="large")

    with image_list:
        img_container = image_list.container(height=1000)
        with img_container:
            evidence_paths = glob.glob("evidence/*.png")
            evidence_images = []
            for file in evidence_paths:
                with open(file, "rb") as image:
                    encoded = base64.b64encode(image.read()).decode()
                    evidence_images.append(f"data:image/jpeg;base64,{encoded}")

            clicked = clickable_images(
                evidence_images,
                titles=[f"{os.path.basename(i)}" for i in evidence_paths],
                div_style={"display": "flex", "flex-wrap": "wrap"},
                # img_style={"width": "300px"},
                img_style={"width": "300px"},
            )

    with image_selection:
        if clicked > -1:
            st.link_button(
                url=f"./chatbot?img_index={clicked}&thesis={thesis}",
                label="Discuss this image",
                use_container_width=True
            )
            st.image(evidence_images[clicked],
                    caption=f"{os.path.basename(evidence_paths[clicked])}",
                    use_column_width="never",
                    width=600
            )
