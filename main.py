import streamlit as st
from rembg import remove
from PIL import Image
import io
import base64 
button_css = """
<style>
.button-85 {
  padding: 0.6em 2em;
  border: none;
  outline: none;
  color: rgb(255, 255, 255);
  background: #111;
  cursor: pointer;
  position: relative;
  z-index: 0;
  border-radius: 10px;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  text-decoration: none;
  display: inline-block;
}

.button-85:before {
  content: "";
  background: linear-gradient(
    45deg,
    #bb1ccc,
    #5c1abb
  );
  position: absolute;
  top: -2px;
  left: -2px;
  background-size: 400%;
  z-index: -1;
  filter: blur(5px);
  -webkit-filter: blur(5px);
  width: calc(100% + 4px);
  height: calc(100% + 4px);
  animation: glowing-button-85 20s linear infinite;
  transition: opacity 0.3s ease-in-out;
  border-radius: 10px;
}

@keyframes glowing-button-85 {
  0% {
    background-position: 0 0;
  }
  50% {
    background-position: 400% 0;
  }
  100% {
    background-position: 0 0;
  }
}

.button-85:after {
  z-index: -1;
  content: "";
  position: absolute;
  width: 100%;
  height: 100%;
  background: #222;
  left: 0;
  top: 0;
  border-radius: 10px;
}

.centered {
  text-align: center;
  margin-top: 20px;
}
</style>
"""

gradient_text_css = """
    <style>
    .gradient-text {
        font-weight: bold;
        background: -webkit-linear-gradient(left, #bb1ccc, #5c1abb);
        background: linear-gradient(to right, #bb1ccc, #5c1abb);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline-block;
        font-size: 3em;
        position: relative;
        overflow: hidden;
    }
    .gradient-text:hover::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 200%;
        height: 100%;
        background: linear-gradient(to right, rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0));
        animation: shine 0.5s forwards linear;
    }

    @keyframes shine {
        to {
            left: 100%;
        }
    }
    </style>
"""

st.markdown(gradient_text_css, unsafe_allow_html=True)

with open("ui/sidebar.md", "r") as sidebar_file:
    sidebar_content = sidebar_file.read()

with open("ui/styles.md", "r") as styles_file:
    styles_content = styles_file.read()


st.sidebar.markdown(sidebar_content)
href = f'<a href="https://www.linkedin.com/in/aryanbhan/" style="text-decoration: none;color: white;">Connect with me</a>'    

styled_button_html2 = f"<div style='text-align: center;padding: 5px 10px; font-size: 12px'><button class='button-62' role='button'><span class='text'>{href}</span></button></div>"
st.sidebar.markdown(styled_button_html2, unsafe_allow_html=True)

st.write(styles_content, unsafe_allow_html=True)


st.title("MyBgRemover.io")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.markdown(button_css, unsafe_allow_html=True)
    # Create two columns
    col1, col2 = st.columns(2)

    with col1:
        st.image(image, caption='Uploaded Image', use_column_width=True)

    # Remove background
    result = remove(image)

    with col2:
        st.image(result, caption='Image with Background Removed', use_column_width=True)

    # Convert result image to byte array for download
    buf = io.BytesIO()
    result.save(buf, format='PNG')
    byte_im = buf.getvalue()
    # Creating Styled Button
    download_link = f'<div class="centered" style="margin:20px"><a href="data:file/png;base64,{base64.b64encode(byte_im).decode()}" download="background_removed.png" class="button-85" style="text-decoration: none;color:white">Download Image</a></div>'
    st.markdown(download_link, unsafe_allow_html=True)


# Credits 
st.write(
    """
    <div style="text-align:center; font-size: 14px; font-weight: bold; color: black;
                text-shadow: 0px 0px 10px rgba(255, 255, 255, 0.7);">
        Made with ❤️ by Aryan Bhan
    </div>
    """,
    unsafe_allow_html=True
)