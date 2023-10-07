import streamlit as st
import os

static_folder_path = os.path.join(os.getcwd(), "static")
youtube_img_path = os.path.join(static_folder_path, 'Youtube.png')


def main():
    st.title("Welcome to Shion Maruko's Portfolio")
    st.divider()
    st.markdown("""
    Hello! I'm Shion Maruko, a specialist in mobile application development, backend engineering, and cloud infrastructure. This portfolio features the applications I've developed.
    """)
    # アプリの紹介をする
    # リストで以下を表示する
    # 左1/5にアイコン画像、残り右にタイトル、説明、リンク
    # リンクは各pagesのpage.pyに飛ばすようにする
    st.header("Applications")
    appList = [
        {
            "image": "https://is2-ssl.mzstatic.com/image/thumb/Purple116/v4/3a/e7/83/3ae78330-7751-ba7b-ce15-1c367adf3f7c/AppIcon-1x_U007emarketing-0-7-0-85-220.png/1024x1024bb.png",
            "title": "Connect Point",
            "description": "This service allows you to implement a loyalty card system solely using a smartphone. Once a card is purchased within the app, you can utilize your store's bespoke loyalty program right from your own smartphone.",
        },
        {
            "image": "https://is1-ssl.mzstatic.com/image/thumb/Purple116/v4/3e/d6/ec/3ed6ec65-f357-dd4e-95bc-83bab064fc51/AppIcon-1x_U007emarketing-0-7-0-85-220.png/1024x1024bb.png",
            "title": "Vision Speak",
            "description": "Vision Speak is an AI-based app that enables users to converse in English about objects they capture with their smartphone's camera. It offers a feature to search, save, and use chosen English phrases during the conversation, and receive feedback – designed based on the interaction hypothesis of language learning.",
        }
    ]
    for app in appList:
        createApp(app)

    st.markdown("""##### Other Applications""")
    _, _, daily_phrase, _, translation_history, _, english, _, _ = st.columns(
        9)
    daily_phrase.image(image="https://is1-ssl.mzstatic.com/image/thumb/Purple112/v4/a4/15/dd/a415dd11-2daa-e334-7db4-d87a03c5133d/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/460x0w.webp", use_column_width=True)
    daily_phrase.markdown(
        """
        [AppStore](https://apps.apple.com/us/app/daily-phrase/id6444667914)
        [GitHub](https://gitlab.com/marushi/daily-fraze)
        """)
    translation_history.image(
        image="https://is1-ssl.mzstatic.com/image/thumb/Purple126/v4/4b/78/61/4b7861cf-0c70-067d-2053-4399c480d900/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/460x0w.webp", use_column_width=True)
    translation_history.markdown(
        """
        [AppStore](https://apps.apple.com/us/app/%E7%BF%BB%E8%A8%B3%E5%B1%A5%E6%AD%B4/id1591420927)
        [GitHub](https://gitlab.com/marushi/translate-history)
        """)
    english.image(image="https://is1-ssl.mzstatic.com/image/thumb/Purple112/v4/b8/96/4d/b8964d5b-ad46-3a84-1c97-12089dc4f90a/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/460x0w.webp", use_column_width=True)
    english.markdown(
        """
        [AppStore](https://apps.apple.com/us/app/english-%E8%8B%B1%E8%AA%9E%E5%8A%9B-%E3%82%92%E9%AB%98%E3%82%81%E3%82%8B%E3%82%A2%E3%83%97%E3%83%AA/id1616308168)
        [GitHub](https://gitlab.com/marushi/english)
        """)

    st.divider()
    st.header("Other Activities")
    st.markdown("")
    appCol1, appCol2 = st.columns([1, 4])
    appCol1.image(image=youtube_img_path, use_column_width=True)
    appCol2.markdown(f"""
    ### YouTube: Omotenashi Japan - Nihon-Shoku ch
    'Omotenashi Japan - Nihon-Shoku ch'  As a **cameraman**, I've had the opportunity to work on a **YouTube channel** named 'Omotenashi Japan - Nihon-Shoku ch'. The channel offers a glimpse of foreign guests experiencing local Japanese restaurants.
    """)


def createApp(app):
    st.markdown("")
    appCol1, appCol2 = st.columns([1, 4])
    appCol1.image(image=app["image"], use_column_width=True)
    appCol2.markdown(f"""
    ### {app["title"]}
    {app["description"]}
    """)


if __name__ == "__main__":
    main()
