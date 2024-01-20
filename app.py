import streamlit as st
from openai import OpenAI
import json

# Function to serialize the output
def serialize(obj):
    """Recursively walk object's hierarchy."""
    if isinstance(obj, (bool, int, float, str)):
        return obj
    elif isinstance(obj, dict):
        obj = obj.copy()
        for key in obj:
            obj[key] = serialize(obj[key])
        return obj
    elif isinstance(obj, list):
        return [serialize(item) for item in obj]
    elif isinstance(obj, tuple):
        return tuple(serialize(item) for item in obj)
    elif hasattr(obj, '__dict__'):
        return serialize(obj.__dict__)
    else:
        return repr(obj)  # Don't know how to handle, convert to string

# Access the OpenAI API key from Streamlit secrets
api_key = st.secrets["openai_secret"]

# Initialize the OpenAI client with the API key from secrets
client = OpenAI(api_key=api_key)

# Streamlit UI components
st.title('''Hate Speech Detection''')

user_input = st.text_area("Enter your text to run the hate speech detection:")

if st.button('Moderate'):
    response = client.moderations.create(input=user_input)
    output = response.results[0]
    serialized_output = serialize(output)
    json_output = json.dumps(serialized_output, indent=2, ensure_ascii=False)
    st.json(json_output)

tab1, tab2, tab3 = st.tabs(['About', 'Why', 'Contact'])
with tab1:
    st.write("AI hate speech detection involves the use of artificial intelligence to identify and classify instances of hate speech in various forms of communication, such as social media posts, comments, and private messages. Several AI models have been developed for this purpose, each with its unique approach. For example, researchers have developed models that utilize deep learning and neural networks to capture different properties of hate speech, as well as traditional rule-based approaches combined with deep learning to improve accuracy and explainability.")
