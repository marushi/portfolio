import streamlit as st
import os

static_folder_path = os.path.join(os.getcwd(), "static")
VisionSpeak_img_path = os.path.join(static_folder_path, 'VisionSpeak.png')
AppStore_img_path = os.path.join(static_folder_path, 'AppStore.png')
Github_img_path = os.path.join(static_folder_path, 'GitHub.png')


def main():
    st.title("Vision Speak")
    st.divider()
    app_store, git_hub, _ = st.columns([1, 2, 2])
    app_store.image(image=AppStore_img_path, width=100)

    link_text = '[TestFlight](https://testflight.apple.com/join/rv4CwKEQ)'
    app_store.markdown(link_text, unsafe_allow_html=True)

    # _, col, _ = image.columns([1, 2, 1])
    git_hub.image(image=Github_img_path, width=100)
    mobile, backend = git_hub.columns([1, 1])
    mobile_link = '[GitHub: iOS](https://github.com/Smart-Connections/vision-speak-ios)'
    backend_link = '[GitHub: Backend](https://github.com/Smart-Connections/visison-speak-backinfra)'
    mobile.markdown(mobile_link, unsafe_allow_html=True)
    backend.markdown(backend_link, unsafe_allow_html=True)

    st.divider()
    createVisionPro()


def createVisionPro():
    visionPro = st.container()
    _, col, _ = visionPro.columns(3)
    col.image(
        image="https://is1-ssl.mzstatic.com/image/thumb/Purple116/v4/3e/d6/ec/3ed6ec65-f357-dd4e-95bc-83bab064fc51/AppIcon-1x_U007emarketing-0-7-0-85-220.png/1024x1024bb.png", use_column_width=True)
    visionPro.markdown(
        "Vision Speak is an AI-based app that enables users to converse in English about objects they capture with their smartphone's camera. It offers a feature to search, save, and use chosen English phrases during the conversation, and receive feedback – designed based on the interaction hypothesis of language learning.")
    imageCol1, imageCol2 = st.columns(2)
    imageCol1.image(image="https://is1-ssl.mzstatic.com/image/thumb/PurpleSource116/v4/d9/ec/fd/d9ecfde6-dd98-2211-563e-2d1b67c0a83b/6c056eaa-e387-48a5-956e-78b5fb8b9dad_6.5_1__U2013_1.png/800x400bb.png")
    imageCol1.image(image="https://is1-ssl.mzstatic.com/image/thumb/PurpleSource126/v4/8f/0f/ab/8f0faba8-8f6c-6228-f12d-97d00c70b424/91999eee-22c1-4a77-b690-a3f13140ccd4_6.5_1__U2013_2.png/800x400bb.png")
    imageCol2.image(image="https://is1-ssl.mzstatic.com/image/thumb/PurpleSource116/v4/2b/fd/2c/2bfd2cce-2d01-0287-9387-09a9452f0a51/624a7ff2-63d1-4bed-806c-ec01c43909b3_6.5_1__U2013_3.png/800x400bb.png")
    imageCol2.image(image="https://is1-ssl.mzstatic.com/image/thumb/PurpleSource116/v4/76/10/38/761038d2-0e6d-936d-aa75-e53f473ec45a/ca72434c-2646-425b-b537-00d1f3646ff2_6.5_1__U2013_4.png/800x400bb.png")

    st.divider()
    st.markdown("""
    ### Architecture
    I built the system, as shown in the following diagram. I utilized Terraform, AWS to create the entire system, excluding the TLS Certificate.

    In addition, I am utilizing the following external APIs:
    - [Whisper API](https://openai.com/blog/introducing-chatgpt-and-whisper-apis): for transcribing the user's voice to text
    - [Chat completions API](https://platform.openai.com/docs/guides/gpt/chat-completions-api): for conversing with the AI assistant
    - [Azure Computer Vision API](https://learn.microsoft.com/ja-jp/azure/ai-services/computer-vision/overview): for recognizing photographed images.
    """)
    st.image(VisionSpeak_img_path, caption="Vision Speak Architecture")

    st.markdown("""
    ### Technology Stack
    - **Mobile App**: Swift, SwiftUI
    - **Backend**: Python, AWS, Terraform, Terraform Cloud
    """
                )


if __name__ == "__main__":
    main()
