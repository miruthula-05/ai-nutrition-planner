from __future__ import annotations

import streamlit as st


def apply_theme() -> None:
    st.markdown(
        """
        <style>
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(125, 211, 252, 0.35), transparent 28%),
                radial-gradient(circle at top right, rgba(186, 230, 253, 0.55), transparent 30%),
                linear-gradient(180deg, #e0f2fe 0%, #f0f9ff 45%, #f8fdff 100%);
            color: #111111;
        }

        .hero-card,
        .panel-card,
        .food-card,
        .metric-card {
            background: rgba(255, 255, 255, 0.82);
            border: 1px solid rgba(56, 189, 248, 0.18);
            border-radius: 22px;
            box-shadow: 0 18px 42px rgba(56, 189, 248, 0.12);
            padding: 1.2rem 1.4rem;
            margin-bottom: 1rem;
            backdrop-filter: blur(10px);
        }

        .hero-title {
            font-size: 2.4rem;
            font-weight: 800;
            color: #0c4a6e;
            margin-bottom: 0.4rem;
        }

        .hero-copy,
        .soft-text {
            color: #334155;
            line-height: 1.6;
        }

        .section-title {
            font-size: 1.1rem;
            font-weight: 800;
            color: #075985;
            margin-bottom: 0.6rem;
        }

        .metric-label {
            color: #0369a1;
            font-size: 0.9rem;
        }

        .metric-value {
            color: #0c4a6e;
            font-size: 1.7rem;
            font-weight: 800;
        }

        .food-name {
            color: #0c4a6e;
            font-size: 1.15rem;
            font-weight: 800;
            margin-bottom: 0.35rem;
        }

        .stRadio > label,
        .stRadio [role="radiogroup"] label,
        .stRadio [role="radiogroup"] label span,
        .stRadio [role="radiogroup"] div,
        .stRadio [data-testid="stMarkdownContainer"],
        .stRadio [data-testid="stMarkdownContainer"] p,
        .stRadio [data-testid="stMarkdownContainer"] span {
            color: #000000 !important;
        }

        div[data-testid="stFormSubmitButton"] button {
            background: #ffffff;
            color: #000000;
            border: 1px solid #111111;
            border-radius: 999px;
            font-weight: 700;
        }

        div[data-testid="stButton"] button {
            background: rgba(240, 249, 255, 0.95);
            color: #0c4a6e;
            border: 1px solid rgba(14, 165, 233, 0.25);
            border-radius: 999px;
            font-weight: 600;
        }

        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #e0f2fe 0%, #dbeafe 100%);
            border-right: 1px solid rgba(14, 165, 233, 0.28);
        }

        section[data-testid="stSidebar"] * {
            color: #0f172a !important;
        }

        section[data-testid="stSidebar"] .stRadio > label {
            font-weight: 800;
            color: #0c4a6e !important;
            margin-bottom: 0.35rem;
        }

        section[data-testid="stSidebar"] [role="radiogroup"] label {
            background: rgba(255, 255, 255, 0.72);
            border: 1px solid rgba(56, 189, 248, 0.18);
            border-radius: 14px;
            padding: 0.55rem 0.75rem;
            margin-bottom: 0.45rem;
            display: block;
            width: 100%;
            min-width: 100%;
            box-sizing: border-box;
        }

        section[data-testid="stSidebar"] [role="radiogroup"] label:hover {
            background: rgba(255, 255, 255, 0.95);
            border-color: rgba(14, 165, 233, 0.35);
        }

        section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
            color: #334155 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
