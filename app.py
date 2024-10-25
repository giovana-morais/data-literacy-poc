import streamlit as st

st.set_page_config(
    page_title="Home Page",
    page_icon=":home:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("# Welcome to the Data Remix prototype!")

st.markdown("""
There are two main functionalities we would like to test here:

* Evidence Selector: this tool helps the student discuss evidences with one agent and gather insights from it. The student *must* have a thesis to work on. Once the discussion is done, the student has the option to save it.

* Data Story Helper: this tool helps the student to build a coherent story from the discussed evidences.

To achieve that, we are restricting this proof-of-concept to discuss only evidences related to Social Media Usage by Teenagers.

The buttons below will direct you to the two tools.
""")

plot_helper = st.toggle(
        "I need help analyzing plots",
        help="Toggle this option if you would like help to read the plots")

argumentation_helper = st.toggle(
        "I need help elaborating arguments",
        help="Toggle this option if you would like help to elaborate your arguments and to connect the data you choose with your thesis")

st.session_state.plot_helper = plot_helper
st.session_state.argumentation_helper = argumentation_helper

if plot_helper:
    st.write("Feature activated!")

if argumentation_helper:
    st.write("Ok, we will provide help on building your arguments")


td = st.button("Assess thesis quality")
es = st.button("Evidence Selector")
dsh = st.button("Data Story Helper")

if td:
    st.switch_page("pages/thesis_definition.py")

if es:
    st.switch_page("pages/evidence_selector.py")

if dsh:
    st.switch_page("pages/data_story_helper.py")
