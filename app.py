import streamlit as st
from transformers import pipeline

# Set up the Streamlit page
st.set_page_config(page_title="Legal Clause Generator", layout="centered")
st.title("📝 Legal Clause Generator")

# Dropdown for selecting clause type
clause_type = st.selectbox("Choose a clause type:", [
    "Arbitration Clause",
    "Confidentiality Clause",
    "Indemnity Clause",
    "Termination Clause",
    "Force Majeure Clause",
    "Governing Law Clause",
    "Severability Clause"
])

# Textbox for optional context input
context = st.text_area("Enter additional context (optional):")

# Load the text generation model (cached so it loads once)
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

generator = load_model()

# Generate clause when button is clicked
if st.button("Generate Clause"):
    prompt = f"Write a detailed and professional {clause_type.lower()} for a legal agreement. {context}"
    result = generator(prompt, max_length=150, num_return_sequences=1)
    clause = result[0]['generated_text']

    st.success("Generated Clause:")
    st.code(clause, language='markdown')
