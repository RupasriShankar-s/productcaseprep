import streamlit as st
import google.generativeai as genai
import os

# Page setup
st.set_page_config(page_title="Haas Product Case Prep Buddy", page_icon="🌟")
st.title("🌟 Product Case Prep Buddy")
st.write("Practice product management case questions and receive AI-generated feedback from your handy dandy HaaSistant")

# Gemini API Key input (can be managed through Streamlit Secrets or UI)
api_key = st.secrets.get("GEMINI_API_KEY", None)
if not api_key:
    api_key = st.text_input("🔑 Enter your Gemini API Key", type="password")

if not api_key:
    st.warning("Please enter your Gemini API key to continue.")
    st.stop()

genai.configure(api_key=api_key)

# Sidebar selections
case_type = st.sidebar.selectbox("Select Case Type", [
    "Design a New Feature",
    "Improve a Metric",
    "Evaluate a Product",
    "Prioritize Roadmap",
    "Launch Strategy"
])

hint_mode = st.sidebar.checkbox("Hint Mode")

# Default prompts
default_prompts = {
    "Design a New Feature": "Design a new feature for Airbnb to help solo travelers.",
    "Improve a Metric": "Instagram engagement is down 20% among Gen Z. What would you do?",
    "Evaluate a Product": "Evaluate the success of Google Pixel phones.",
    "Prioritize Roadmap": "You're a PM at Spotify. How do you prioritize lyrics, AI DJ, and social listening?",
    "Launch Strategy": "How would you launch a new grocery delivery app in a mid-sized U.S. city?"
}

# Initialize session state for dynamic prompt
if "dynamic_prompt" not in st.session_state:
    st.session_state.dynamic_prompt = default_prompts[case_type]

# Handle prompt refresh
col1, col2 = st.columns([10, 1])
with col1:
    st.subheader("🧠 Case Prompt")
    st.write(f"**Prompt:** {st.session_state.dynamic_prompt}")
with col2:
    if st.button("🔄", help="Refresh prompt"):
        with st.spinner("Generating new prompt..."):
            model = genai.GenerativeModel(model_name="gemini-2.0-flash")
            response = model.generate_content([
                f"Generate a fresh product management case interview question in the category: {case_type}. Be concise and realistic."
            ])
            st.session_state.dynamic_prompt = response.text.strip()

# User response input
user_response = st.text_area("Your Answer", height=250)

if st.button("Submit Answer") and user_response:
    with st.spinner("Generating feedback using Gemini..."):
        model = genai.GenerativeModel(model_name="gemini-2.0-flash")
        messages = [
            f"Case Prompt: {st.session_state.dynamic_prompt}",
            f"Candidate Response: {user_response}",
            "You are a product management case interview coach. Provide structured feedback based on frameworks like CIRCLES, AARM, or product metrics. Be clear, concise, and helpful."
        ]

        if hint_mode:
            messages.append("Also include actionable suggestions or framework tips if the answer is incomplete.")

        response = model.generate_content(messages)

        st.subheader("📋 AI Feedback")
        st.markdown(response.text)

        # Download button for feedback
        st.download_button(
            label="📥 Download Feedback",
            data=response.text,
            file_name="case_feedback.txt",
            mime="text/plain"
        )

st.markdown("---")
st.markdown("_Note: Gemini Pro is used for all feedback generation. Toggle Hint Mode for coaching-style tips._")
