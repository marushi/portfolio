import streamlit as st
import os

static_folder_path = os.path.join(os.getcwd(), "static")
ConnectPoint_img_path = os.path.join(static_folder_path, 'ConnectPoint.png')
AppStore_img_path = os.path.join(static_folder_path, 'AppStore.png')
Github_img_path = os.path.join(static_folder_path, 'GitHub.png')


def main():
    st.title("Connect Point")
    st.divider()
    app_store, git_hub, _ = st.columns([1, 3, 1])
    app_store.image(image=AppStore_img_path, width=100)

    link_text = '[AppStore](https://apps.apple.com/us/app/connect-point/id1672584184)'
    app_store.markdown(link_text, unsafe_allow_html=True)

    # _, col, _ = image.columns([1, 2, 1])
    git_hub.image(image=Github_img_path, width=100)
    mobile, backend, proxy = git_hub.columns([1, 1, 1])
    mobile_link = '[GitLab: Mobile](https://gitlab.com/marushi/connectpoint)'
    backend_link = '[GitLab: Backend](https://gitlab.com/marushi/recipe-app-api-devops)'
    proxy_link = '[GitLab: Proxy](https://gitlab.com/marushi/recipe-app-api-proxy)'
    mobile.markdown(mobile_link, unsafe_allow_html=True)
    backend.markdown(backend_link, unsafe_allow_html=True)
    proxy.markdown(proxy_link, unsafe_allow_html=True)

    st.divider()
    createConnectPoins()


def createConnectPoins():
    connectPoint = st.container()
    _, col, _ = connectPoint.columns(3)
    col.image(
        image="https://is2-ssl.mzstatic.com/image/thumb/Purple116/v4/3a/e7/83/3ae78330-7751-ba7b-ce15-1c367adf3f7c/AppIcon-1x_U007emarketing-0-7-0-85-220.png/1024x1024bb.png", use_column_width=True)
    connectPoint.markdown(
        "This service allows you to implement a loyalty card system solely using a smartphone. Once a card is purchased within the app, you can utilize your store's bespoke loyalty program right from your own smartphone.")
    imageCol1, imageCol2 = st.columns(2)
    imageCol1.image(image="https://is2-ssl.mzstatic.com/image/thumb/PurpleSource116/v4/86/b3/4e/86b34ea2-20d8-9924-6553-e5bdc735fc05/ae53c4d0-f04b-4385-823e-d08fc6ba5d7e_6.5_1__U2013_1.png/800x400bb.png")
    imageCol1.image(image="https://is3-ssl.mzstatic.com/image/thumb/PurpleSource126/v4/30/26/c3/3026c319-8a66-a90a-6d30-254e9379483c/d02ce17f-318b-44e6-8036-836d8f333750_6.5_3__U2013_1.png/800x400bb.png")
    imageCol2.image(image="https://is1-ssl.mzstatic.com/image/thumb/PurpleSource116/v4/b4/0b/2d/b40b2d5f-1613-c605-4fce-81d8fc783dc5/c4180cc7-a2b8-49e2-ab97-0240a23d8fdd_6.5_2__U2013_1.png/800x400bb.png")
    imageCol2.image(image="https://is5-ssl.mzstatic.com/image/thumb/PurpleSource126/v4/a4/e3/96/a4e396e5-c8d0-99a3-f021-4516377cdd4c/14501208-dd7e-4f5d-aaf3-9e20a6239852_6.5_4__U2013_1.png/800x400bb.png")

    st.divider()
    st.markdown("""
    ### Architecture
    I built the system, as shown in the following diagram. I utilized Terraform, AWS, and GitLab to create the entire system, excluding the TLS Certificate.
    """)
    st.image(ConnectPoint_img_path, caption="Connect Point Architecture")

    st.markdown("""
    ### Technology Stack
    - **Mobile App**: Flutter
    - **Backend**: Python, Django, AWS, Terraform, Firebase
    - **CI/CD**: GitLab
    - **Point Card**: FeliCa(NFC)
    """
                )


if __name__ == "__main__":
    main()
