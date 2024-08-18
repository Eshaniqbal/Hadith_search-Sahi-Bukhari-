import pandas as pd
import streamlit as st

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv('dataset/data.csv')

data = load_data()

# Custom HTML for favicon and CSS styling
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
    .footer {
        font-size: 0.9em;
        color: #999;
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 20px 0;
      
        border-top: 1px solid #ddd;
    }
    .footer a {
        color: #4682b4;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    <link rel="icon" type="image/x-icon" href="favicon.ico">
    """, unsafe_allow_html=True)

# Streamlit app layout
st.title('Hadith Search Application(Sahih Bukhari)')

# Input for Hadith ID
st.subheader('Search for Hadith:')
hadith_id = st.text_input('Enter Hadith No:', '')

# Add a search button
if st.button('Search'):
    if hadith_id:
        # Filter data based on Hadith ID
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

# Footer
st.markdown("""
    <div class="footer">
        <p>&copy; 2024 Hadith Search Application. All rights reserved.</p>
        <p>Developed by <a href="https://github.com/Eshaniqbal" target="_blank">Eshan Iqbal</a></p>
    </div>
    """, unsafe_allow_html=True)
