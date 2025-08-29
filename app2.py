import streamlit as st
import os
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
# 🔑 Gemini API configure
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="Supply Chain Optimizer", layout="wide")

st.title("📊 AI-powered Supply Chain Optimization")
st.write("Upload a **CSV/Excel** file and get AI-generated supply chain optimization insights.")

uploaded_file = st.file_uploader("📂 Upload your dataset", type=["csv", "xlsx"])

if uploaded_file:
    # ✅ Read file with pandas
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # Show preview
    st.subheader("🔍 Data Preview")
    st.dataframe(df.head(10))

    if st.button("🚀 Generate Optimization Insights"):
        with st.spinner("Analyzing dataset with AI..."):
            # Convert dataframe to text
            csv_text = df.to_string(index=False)

            # Create prompt
            prompt = f"""
            You are a supply chain optimization expert.
            Analyze the following dataset and provide:
            1. Key insights and patterns
            2. Bottlenecks or inefficiencies
            3. Suggestions for optimization
            4. Predicted impact if optimizations are applied

            Dataset:
            {csv_text}
            """

            try:
                response = model.generate_content(prompt)
                st.subheader("📌 AI-Generated Insights")
                st.write(response.text)
            except Exception as e:
                st.error(f"❌ Error: {e}")

