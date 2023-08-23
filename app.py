import streamlit as st
from streamlit_lottie import st_lottie
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb
# import datetime
import requests
from PIL import Image

# '''
# # Klarna Credit Default Model
# GitHub repository [Klarna](https://github.com/Emilio1030/klarna)
# '''
# SETTING PAGE IMAGE & NAME
im = Image.open("image/klarna_icon_1.png")
st.set_page_config(
    page_title="Klarna Project",
    page_icon=im,
)

# Define function to display icon links
def display_icon_link(icon_svg, link):
    icon_html = f'<a href="{link}" style="width: 100px;height: 16px; color: white; margin-right: 10px;">{icon_svg}</a>'
    st.write(icon_html, unsafe_allow_html=True)

# Load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/cfb13562-6706-40b8-9a0a-aeb38009c6a9/ME6FQpO8hx.json")

# Apply custom CSS from the external stylesheet
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# ICON
github_icon_svg = '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 496 512" style="width: 1.28em; height: 2em; color: white;">
<path d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"/></svg>
'''
linkedin_icon_svg = '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" style="width: 1.2em; height: 2em; color: white;">
<path d="M416 32H31.9C14.3 32 0 46.5 0 64.3v383.4C0 465.5 14.3 480 31.9 480H416c17.6 0 32-14.5 32-32.3V64.3c0-17.8-14.4-32.3-32-32.3zM135.4 416H69V202.2h66.5V416zm-33.2-243c-21.3 0-38.5-17.3-38.5-38.5S80.9 96 102.2 96c21.2 0 38.5 17.3 38.5 38.5 0 21.3-17.2 38.5-38.5 38.5zm282.1 243h-66.4V312c0-24.8-.5-56.7-34.5-56.7-34.6 0-39.9 27-39.9 54.9V416h-66.4V202.2h63.7v29.2h.9c8.9-16.8 30.6-34.5 62.9-34.5 67.2 0 79.7 44.3 79.7 101.9V416z"/></svg>
'''
email_icon_svg = '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" style="width: 1.55em; height: 2em; color: white;">
<path d="M48 64C21.5 64 0 85.5 0 112c0 15.1 7.1 29.3 19.2 38.4L236.8 313.6c11.4 8.5 27 8.5 38.4 0L492.8 150.4c12.1-9.1 19.2-23.3 19.2-38.4c0-26.5-21.5-48-48-48H48zM0 176V384c0 35.3 28.7 64 64 64H448c35.3 0 64-28.7 64-64V176L294.4 339.2c-22.8 17.1-54 17.1-76.8 0L0 176z"/></svg>
'''
klarna_image = '''
<svg id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 238.63 53.26"><title>Brand_assets_master</title><path d="M42,0H30.25A30,30,0,0,1,18.11,24.23l-4.65,3.48,18,24.57H46.29L29.71,29.67A41.56,41.56,0,0,0,42,0Z"/><polygon points="0 52.28 12.03 52.28 12.03 0 0 0 0 52.28 0 52.28"/><polygon points="49.79 52.26 61.12 52.26 61.12 0.01 49.79 0.01 49.79 52.26 49.79 52.26"/><path d="M160.49,15.15c-4.32,0-8.41,1.34-11.14,5V16.12H138.57V52.26h10.91v-19c0-5.5,3.68-8.19,8.12-8.19,4.76,0,7.49,2.84,7.49,8.11V52.26H175.9v-23c0-8.41-6.69-14.13-15.41-14.13Z"/><path d="M85.51,43.49a9.56,9.56,0,0,1-9.8-9.3,9.82,9.82,0,0,1,19.61,0,9.56,9.56,0,0,1-9.81,9.3Zm9.84-27.37v2.31A19.07,19.07,0,1,0,84.63,53.26,18.89,18.89,0,0,0,95.35,50v2.31h10.83V16.12Z"/><path d="M122.92,20.83V16.12H111.84V52.26h11.1V35.39c0-5.7,6.17-8.76,10.46-8.76h.12V16.12c-4.39,0-8.43,1.88-10.6,4.71Z"/><path d="M199.68,43.49a9.56,9.56,0,0,1-9.8-9.3,9.82,9.82,0,0,1,19.61,0,9.56,9.56,0,0,1-9.81,9.3Zm9.85-27.37v2.31a19.07,19.07,0,1,0,0,31.52v2.31h10.82V16.12Z"/><path d="M231.84,39.44a6.8,6.8,0,1,0,6.79,6.8,6.79,6.79,0,0,0-6.79-6.8Z"/></svg>
'''

github_link = 'https://github.com/Emilio1030'
linkedin_link = 'https://www.linkedin.com/in/emilioaguiar/'
email_link = 'mailto:junioraguiar_83@hotmail.com'
#############

# GIPHY IMAGE
giphy_url = "https://media.giphy.com/media/N013zOWpvY7O9T2XYP/giphy.gif"
html_code = f"""
            <a href="{giphy_url}" target="_blank">
                <img src="{giphy_url}" width="300" alt="Giphy GIF" />
            </a>
            """
###############

# Load external CSS file
st.markdown('<link rel="stylesheet" href="custom.css">', unsafe_allow_html=True)

# Streamlit layout structure
with st.container():
    st.write("##") # this part will set where the image/cotainer starts
    image_column = st.columns(1)
    with image_column[0]:

        st.image(klarna_image, width=200)
        st_lottie(lottie_coding, height=350, key="coding")

    with st.form(key='params_for_api'):
        customer_id_input = st.text_input('Customer ID', value="e25e41f6-c314-4f76-ac8a-a8d0185706c7")

        if st.form_submit_button(label='Make prediction'):
            payload = {
                'customer_ID': customer_id_input,
                'output': 'Payer!',
                'probability': 0.009
            }

            wagon_cab_api_url = 'https://emilio-klarna-v9-zsm6vqiqwq-ew.a.run.app/predict'
            response = requests.get(wagon_cab_api_url, params=payload)

            if response.status_code == 200:
                st.success("Prediction successful!")
                prediction_data = response.json()

                st.write("Prediction Result:")
                st.write(f"Customer ID: {prediction_data['customer_ID']}")
                st.write(f"Probability: {prediction_data['probability']}")
                if prediction_data['probability'] <= 0.20:
                   # st.write("![Your Awsome GIF](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWFwbHpvaWh2N3p1MWxydzBpNjdneXNzMWRqYnB5OXRvMTZqeDYxdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/N013zOWpvY7O9T2XYP/giphy.gif)")
                    st.write(html_code, unsafe_allow_html=True)
                else:
                    st.write("![Not approved](https://media.giphy.com/media/9B5bcqtSnJq44vtsvn/giphy.gif")
                # st.write(f"Output: {prediction_data['output']}")
            else:
                st.error(f"Error: {response.status_code}")


# below - source: https://discuss.streamlit.io/t/st-footer/6447

def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))

def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)

def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 80px; }
    </style>
    """
    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="black",
        text_align="center",
        height="auto",
        opacity=1,
        font_family="'Mulish', sans-serif",  # Add this line
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        # border_style="inset",
        # border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)

def footer():
    myargs = [
        "Made in ",
        image('https://avatars3.githubusercontent.com/u/45109972?s=400&v=4',
              width=px(20), height=px(20)),
        " by ", #"with ❤️ by ",
        link("mailto:junioraguiar_83@hotmail.com", "@EmilioAguiar"),
        br(),
       "Further details on",
        github_icon_svg,
        a(href=github_link, target="_blank", style=styles(color="black")),
        linkedin_icon_svg,
        a(href=linkedin_link, target="_blank", style=styles(color="black")),
        email_icon_svg,
        a(href=email_link, target="_blank", style=styles(color="black")),
    ]
    layout(*myargs)

if __name__ == "__main__":
    footer()

# note: every time I change the code and want to put in porduction
# I have to go to this website: https://share.streamlit.io/ with my login
