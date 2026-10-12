import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="DCOM Adaptive Error-Control Coding",
    page_icon="📡",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent

st.title("📡 DCOM Adaptive Error-Control Coding")
st.subheader("MATLAB Simulation Results & Performance Analysis")

st.markdown("""
This dashboard presents MATLAB simulation outputs for
adaptive error-control coding, including BER comparison,
decision-tree analysis, adaptive decisions, and code rate.
""")

# 1. MATLAB graphs
st.header("1. MATLAB Simulation Graphs")

graphs = [
    ("DCOM_BER_Comparison.png", "Figure 1: BER Comparison"),
    ("Figure2_Decision_Tree.png", "Figure 2: Decision Tree"),
    ("Figure3_Adaptive_Decisions.png", "Figure 3: Adaptive Decisions"),
    ("Figure4_Code_Rate.png", "Figure 4: Code Rate")
]

for filename, caption in graphs:
    path = BASE_DIR / filename
    if path.exists():
        st.subheader(caption)
        st.image(str(path), use_container_width=True)
    else:
        st.warning(f"Missing file: {filename}")

# 2. MATLAB CSV results
st.header("2. MATLAB Results Data")

csv_files = [
    ("DCOM_BER_Results.csv", "BER Comparison Results"),
    ("DCOM_Adaptive_Decisions.csv", "Adaptive Decisions Results")
]

for filename, title in csv_files:
    path = BASE_DIR / filename
    if path.exists():
        st.subheader(title)
        try:
            df = pd.read_csv(path)
            st.dataframe(df, use_container_width=True)

            st.download_button(
                label=f"Download {filename}",
                data=path.read_bytes(),
                file_name=filename,
                mime="text/csv",
                key=filename
            )
        except Exception as e:
            st.error(f"Error reading {filename}: {e}")
    else:
        st.warning(f"Missing file: {filename}")

st.divider()
st.caption("DCOM Adaptive Error-Control Coding | MATLAB Simulation")
