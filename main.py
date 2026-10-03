
# This is the main entry point for the project

import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post


def main():

    # -----------------------------
    # Page configuration
    # -----------------------------

    st.set_page_config(
        page_title="LinkedIn Post Generator",
        page_icon="💼",
        layout="wide"
    )

    # -----------------------------
    # Custom CSS
    # -----------------------------

    st.markdown("""
        <style>
    /* Topic, Length, Language labels */
.stSelectbox label {
    color: #000000 !important;
    font-weight: 600;
}

/* Select box */
.stSelectbox div[data-baseweb="select"] > div {
    background-color: #000000 !important;
    border: 1px solid #000000 !important;
}

/* Selected text */
.stSelectbox div[data-baseweb="select"] span {
    color: #000000 !important;
}    
        /* Main background */
        .stApp {
            background-color: #f4f7fb;
        }

        /* Main title */
        .main-title {
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            color: #E91E63;
            margin-bottom: 5px;
        }

        /* Subtitle */
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #555555;
            margin-bottom: 35px;
        }

        /* Generate button */
        .stButton > button {
            background-color: #D63384;
            color: white;
            border-radius: 8px;
            border: none;
            padding: 10px 25px;
            font-size: 17px;
            font-weight: bold;
        }

        .stButton > button:hover {
            background-color: #004182;
            color: white;
        }

        /* Generated post */
        .post-box {
    background-color: white;
    color: #000000 !important;
    padding: 25px;
    border-radius: 12px;
    border-left: 5px solid #0A66C2;
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.08);
    font-size: 17px;
    line-height: 1.7;
    white-space: pre-wrap;
}

        </style>
    """, unsafe_allow_html=True)


    # -----------------------------
    # Header
    # -----------------------------

    st.markdown(
        '<div class="main-title">💼 LinkedIn Post Generator</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Create engaging LinkedIn posts with AI ✨</div>',
        unsafe_allow_html=True
    )


    # -----------------------------
    # Load Few Shot Posts
    # -----------------------------

    fs = FewShotPosts()


    # -----------------------------
    # Input options
    # -----------------------------

    col1, col2, col3 = st.columns(3)

    length_options = ["Short", "Medium", "Long"]

    language_options = [
        "English",
        "French",
        "Spanish",
        "Hinglish"
    ]


    with col1:
        selected_tag = st.selectbox(
            "🏷️ Topic",
            options=fs.get_tags()
        )


    with col2:
        selected_length = st.selectbox(
            "📏 Length",
            options=length_options
        )


    with col3:
        selected_language = st.selectbox(
            "🌐 Language",
            options=language_options
        )


    # -----------------------------
    # Generate button
    # -----------------------------

    st.write("")

    col_button1, col_button2, col_button3 = st.columns(
        [1, 1, 1]
    )

    with col_button2:

        generate = st.button(
            "✨ Generate Post",
            use_container_width=True
        )


    # -----------------------------
    # Generate post
    # -----------------------------

    if generate:

        with st.spinner("Creating your LinkedIn post..."):

            post = generate_post(
                selected_length,
                selected_language,
                selected_tag
            )


        # -----------------------------
        # Display generated post
        # -----------------------------

        st.markdown(
            '<h3 style="color: #E91E63;">🚀 Your LinkedIn Post</h3>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="post-box">
            {post}
            </div>
            """,
            unsafe_allow_html=True
        )


if __name__ == "__main__":
    main()

