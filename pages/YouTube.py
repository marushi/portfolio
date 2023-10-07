import streamlit as st
import os

static_folder_path = os.path.join(os.getcwd(), "static")
Youtube_img_path = os.path.join(static_folder_path, 'Youtube.png')


def main():
    st.title("YouTube")
    st.divider()
    st.markdown("""
    [YouTube: Omotenashi Japan - Nihon-Shoku ch](https://www.youtube.com/watch?v=DfSMAJwkNB8)
    """)
    st.divider()
    createYouTube()


def createYouTube():
    visionPro = st.container()
    _, col, _ = visionPro.columns(3)
    col.image(image=Youtube_img_path, use_column_width=True)
    visionPro.markdown(
        "'Omotenashi Japan - Nihon-Shoku ch'  As a **cameraman**, I've had the opportunity to work on a **YouTube channel** named 'Omotenashi Japan - Nihon-Shoku ch'. The channel offers a glimpse of foreign guests experiencing local Japanese restaurants.")
    imageCol1, imageCol2 = st.columns(2)
    imageCol1.image(
        image="http://img.youtube.com/vi/DfSMAJwkNB8/maxresdefault.jpg")
    imageCol2.image(
        image="http://img.youtube.com/vi/mb7VTOV5GjY/maxresdefault.jpg")

    st.divider()
    st.markdown("""
    ### Skills
    - **Communication**
    - **Facilitation**
    - **Project Management**
    """
                )


if __name__ == "__main__":
    main()
