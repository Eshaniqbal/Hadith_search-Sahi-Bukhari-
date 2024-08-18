import pandas as pd
import streamlit as st

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv('dataset/data.csv')

data = load_data()


st.title('Hadith Search Application (Sahih Bukhari)')
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    body {
        font-family: 'Poppins', sans-serif;
    }
    
    .title {
        font-size: 2em;
        color: #2e8b57;
    }
    .header {
        font-size: 1.5em;
        color: #4682b4;
    }
    .result {
        border: 1px solid #ddd;
        padding: 10px;
        margin-bottom: 10px;
    }
    .button {
        background-color: #4682b4;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
    }
    .button:hover {
        background-color: #315f8b;
    }
    </style>
    """, unsafe_allow_html=True)


st.subheader('Search for Hadith No:')
hadith_id = st.text_input('Enter Hadith No:', '')


if st.button('Search'):
    if hadith_id:
       
        result = data[data['hadith_id'].astype(str) == hadith_id]
        
        if not result.empty:
            st.markdown("<div class='header'>Search Results:</div>", unsafe_allow_html=True)
            for index, row in result.iterrows():
                st.markdown(f"""
                    <div class='result'>
                    <p><strong>Source:</strong> {row['source']}</p>
                    <p><strong>Chapter No:</strong> {row['chapter_no']}</p>
                    <p><strong>Hadith No:</strong> {row['hadith_id']}</p>
                    <p><strong>Chapter:</strong> {row['chapter']}</p>
                    <p><strong>Text (AR):</strong> {row['text_ar']}</p>
                    <p><strong>Text (EN):</strong> {row['text_en']}</p>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.write("No results found for this Hadith ID.")
    else:
        st.write("Please enter a Hadith ID to search.")
