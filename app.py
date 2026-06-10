import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
    page_title="SEORAE SEOUL",
    page_icon="◼",
    layout="wide"
)

ASSET_DIR = Path(".")


def image_to_base64(path):
    if not path.exists():
        return ""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


main_img = image_to_base64(ASSET_DIR / "main.jpg")
img1 = image_to_base64(ASSET_DIR / "image1.jpg")
img2 = image_to_base64(ASSET_DIR / "image2.jpg")
img3 = image_to_base64(ASSET_DIR / "image3.jpg")


st.markdown("""
<style>
    .stApp {
        background-color: #ffffff;
        color: #111111;
    }

    header, footer {
        visibility: hidden;
    }

    .block-container {
        padding: 2rem 3rem 4rem 3rem;
        max-width: 100%;
    }

    .nav {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        font-size: 13px;
        letter-spacing: 0.04em;
        margin-bottom: 70px;
    }

    .nav-left {
        font-weight: 500;
    }

    .nav-right a {
        margin-left: 28px;
        text-decoration: none;
        color: #111111;
    }

    .project-title {
        font-size: 42px;
        font-weight: 400;
        letter-spacing: -0.03em;
        line-height: 1.1;
        margin-bottom: 16px;
    }

    .project-meta {
        font-size: 13px;
        line-height: 1.8;
        color: #555555;
        margin-bottom: 60px;
    }

    .hero-img {
        width: 100%;
        height: auto;
        margin-bottom: 70px;
    }

    .section {
        display: grid;
        grid-template-columns: 1fr 2fr;
        gap: 60px;
        margin: 80px 0;
    }

    .section-title {
        font-size: 13px;
        color: #777777;
    }

    .section-text {
        font-size: 18px;
        line-height: 1.75;
        letter-spacing: -0.02em;
    }

    .gallery {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 24px;
        margin-top: 60px;
    }

    .gallery img {
        width: 100%;
        height: auto;
    }

    .bottom-nav {
        display: flex;
        justify-content: space-between;
        margin-top: 90px;
        font-size: 13px;
    }

    .work-list {
        margin-top: 90px;
        font-size: 14px;
        line-height: 2.1;
    }

    .work-list a {
        color: #111111;
        text-decoration: none;
    }

    @media (max-width: 768px) {
        .nav {
            display: block;
        }

        .nav-right {
            margin-top: 20px;
        }

        .nav-right a {
            display: block;
            margin: 8px 0;
        }

        .project-title {
            font-size: 32px;
        }

        .section {
            grid-template-columns: 1fr;
            gap: 20px;
        }

        .gallery {
            grid-template-columns: 1fr;
        }
    }
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="nav">
    <div class="nav-left">YOUR STUDIO</div>
    <div class="nav-right">
        <a href="#">About</a>
        <a href="#">Work</a>
        <a href="#">Jobs</a>
        <a href="#">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="project-title">
    SEORAE SEOUL
</div>

<div class="project-meta">
    Type: Architecture / Housing / Cultural Space<br>
    Location: Seoul, Korea<br>
    Status: Design Proposal<br>
    Year: 2026
</div>
""", unsafe_allow_html=True)


if main_img:
    st.markdown(
        f'<img class="hero-img" src="data:image/jpeg;base64,{main_img}">',
        unsafe_allow_html=True
    )
else:
    st.warning("assets/main.jpg 이미지를 넣으면 메인 이미지가 표시됩니다.")


st.markdown("""
<div class="section">
    <div class="section-title">Overview</div>
    <div class="section-text">
        This project proposes a new urban living structure in Seoul, combining compact residential units,
        cultural programs, and elevated public space. The building is designed as a layered system where
        housing, circulation, greenery, and community programs are connected vertically and horizontally.
    </div>
</div>

<div class="section">
    <div class="section-title">Design Concept</div>
    <div class="section-text">
        The project responds to the density of Seoul by creating a continuous urban section.
        Rather than separating private and public programs, the proposal allows them to overlap through
        terraces, shared platforms, and suspended volumes.
    </div>
</div>
""", unsafe_allow_html=True)


st.markdown('<div class="gallery">', unsafe_allow_html=True)

for img in [img1, img2, img3]:
    if img:
        st.markdown(
            f'<img src="data:image/jpeg;base64,{img}">',
            unsafe_allow_html=True
        )

st.markdown('</div>', unsafe_allow_html=True)


st.markdown("""
<div class="section">
    <div class="section-title">Information</div>
    <div class="section-text">
        Program: Residential Units, Cultural Space, Green Roof, Public Deck<br>
        Structure: Steel Truss System<br>
        Site Condition: Urban Roadside / Public Transit Node<br>
        Keywords: Layered City, Elevated Living, Urban Commons
    </div>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="bottom-nav">
    <div>prev / next</div>
    <div>Back to Work</div>
</div>

<div class="work-list">
    <a href="#">01 Urban Housing Seoul</a><br>
    <a href="#">02 Cultural Platform</a><br>
    <a href="#">03 Mixed-use Structure</a><br>
    <a href="#">04 Public Roof Garden</a><br>
    <a href="#">05 Seoul Elevated Street</a>
</div>
""", unsafe_allow_html=True)
