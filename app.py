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

# Display GitHub logo
st.image("https://i.ibb.co/kyK4hJb/github.png")

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
    st.video("https://static.streamlit.io/examples/star.mp4")
    st.write("AI hate speech detection involves the use of artificial intelligence to identify and classify instances of hate speech in various forms of communication, such as social media posts, comments, and private messages. Several AI models have been developed for this purpose, each with its unique approach. For example, researchers have developed models that utilize deep learning and neural networks to capture different properties of hate speech, as well as traditional rule-based approaches combined with deep learning to improve accuracy and explainability.")
with tab2:
    st.image("https://i.ibb.co/HN5bbPQ/bannerspeechbg.png")
    st.write("AI hate speech detection is important for several reasons. Firstly, it can help identify and flag harmful content swiftly and accurately, enabling platforms to take proactive measures to combat online hate speech and create a safer digital environment. Additionally, automated detection is appealing for its ability to find hate speech much quicker and in vastly greater quantities than humans. Furthermore, the use of AI in hate speech detection can help mitigate the damaging impact of hate speech on social media, offering the potential for safer online interactions. Despite the current challenges and limitations, the ongoing development of AI-powered tools for hate speech detection remains a crucial area of research and innovation in the fight against online hate and harassment.")
with tab3:
    st.write("Contact me at fake@email.com if you have any questions.")
