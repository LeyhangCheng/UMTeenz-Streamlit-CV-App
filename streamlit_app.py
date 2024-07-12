import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# 1. Import streamlit option menu
from streamlit_option_menu import option_menu

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# 2. Add in menu bar
menu_bar_selected = option_menu(
    menu_title=None,
    options=["Home", "Education Background", "Curriculum Vitae"],
    icons=["house", "book", "trophy"], # icons can be found in https://icons.getbootstrap.com/?q=trope
    orientation="horizontal",
        styles={
        "container": {"padding": "0!important", "background-color": "#1b1f1b"}, # HEX code
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "center", "margin":"0px", "--hover-color": "#406340"},
        "nav-link-selected": {"background-color": "green"},
    },
)

# ---- LOADING ASSETS ---- Need to pip install streamlit-lottie, request
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/b32013b4-ac53-4acd-849e-1a15f8094390/eoMSE0cQjh.json")
img_trump = Image.open("images/trump2.jpeg")

# ---- HEADER SECTION ----
if menu_bar_selected == "Home":
    with st.container():
        st.write("---")
        st.title("Hi, I am Leyhang :wave:")
        st.subheader("A Software Developer From Kuala Lumpur")
        st.write(
            "This is my first python app website, hence feel free to navigate to other pages to know more about me!"
        )

# ---- WHAT I STUDIED ----
if menu_bar_selected == "Education Background":
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Education Summary")
            st.write("\n")
            st.write(
                """
                I'm a graduate from Universiti Malaya with the following credentials:
                - ✔️ Bachelor of Artificial Intelligence
                """
            )
            st.write("\n")
            st.write("[Link to UM Faculty of Computer Science >](https://portal.um.edu.my)")
        
        # Insert animation, can be obtained from https://lottiefiles.com
        with right_column:
            st_lottie(lottie_coding, height=300, width=500, key="coding", speed=1, loop=True)

# ---- PROJECTS ---- Need Pillow to display images, then create an images dir, upload picture
if menu_bar_selected == "Curriculum Vitae":
    with st.container():
        st.write("---")
        st.header("My CV")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_trump)
        with text_column:
            st.subheader("Cheng Ley Hang")
            st.write(
                """
                I've Strong interest in leveraging technology as a tool to assist entities in enabling digital transformation
                """
            )

            st.write('\n')
            st.subheader("Qulifications")
            st.write('\n')
            st.write(
                """
                - ✔️ 1 year in Ernst & Young as Project Management Trainee
                - ✔️ Strong hands on experience and knowledge in Azure technology
                - ✔️ 3 years in ExxonMobil as Tech Lead & Scrum Master
                - ✔️ Good understanding of statistical analytics in Oil & Gas manufacturing application
                - ✔️ Certified SAFe® 5 Advanced Scrum Master
                - ✔️ Professional Scrum Master I from Scrum Organisation
                """
                )
            st.write('\n')
            st.subheader("Hard Skills")
            st.write(
                """
            - 👩‍💻 Programming: Python, SQL, .NET, JS
            - 📊 Data Visulization: PowerBi, Tableau, Plotly
            - 📚 Cloud: Terraform Enterprise, Azure (RG, Blob, Function App, Service Bus), Openshift
            - 🗄️ Databases: MS SQL, Snowflake, HDFS
            """
            )
            st.write('\n')
            st.markdown("[Get my CV here in pdf format](https://www.canva.com/resumes/templates/)")