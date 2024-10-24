import streamlit as st
from config import GOOGLE_API_KEY
from gemini_adapter import GeminiAdapter, GeminiConfig

def init_session_state():
    if 'gemini' not in st.session_state:
        gemini_config = GeminiConfig(
            temperature=0.7,
            max_output_tokens=100,
            top_p=0.8,
            top_k=40
        )
        adapter = GeminiAdapter(GOOGLE_API_KEY)
        adapter.setup_model(gemini_config)
        st.session_state['gemini'] = adapter

def main():
    st.title("Gemini AI Chat Interface")
    
    init_session_state()
    

    st.sidebar.header("Model Configuration")
    current_temp = st.session_state.gemini.get_current_temperature()
    current_tokens = st.session_state.gemini.get_current_max_tokens()
    
    temperature = st.sidebar.slider("Temperature", 0.0, 1.0, current_temp)
    max_tokens = st.sidebar.number_input("Max Tokens", 50, 1000, current_tokens)
    

    if (temperature != current_temp or max_tokens != current_tokens):
        new_config = GeminiConfig(
            temperature=temperature,
            max_output_tokens=max_tokens
        )
        st.session_state.gemini.setup_model(new_config)
    

    user_input = st.text_area("Enter your prompt:", height=100)
    
    if st.button("Generate"):
        if user_input:
            with st.spinner("Generating response..."):
                response = st.session_state.gemini.generate_response(user_input)
                st.write("Response:")
                st.markdown(response)  # Using markdown for better formatting

if __name__ == "__main__":
    main()