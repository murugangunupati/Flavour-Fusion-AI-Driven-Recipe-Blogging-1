import streamlit as st
import google.generativeai as genai
import random

# Directly set API key
GOOGLE_API_KEY = "AIzaSyARIslpvh3yfTNS77SSoYxqE08Ar-RgOhQ"

# Configure Google Generative AI
genai.configure(api_key="AIzaSyARIslpvh3yfTNS77SSoYxqE08Ar-RgOhQ")

# Function to generate a programming joke
def get_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "How do you comfort a JavaScript bug? You console it!",
        "Why did the Python programmer break up with the Java programmer? Because he didn't like Java's class!"
    ]
    return random.choice(jokes)

# Function to generate a recipe blog
def recipe_generation(user_input, word_count):
    st.write("📝 Generating your recipe... Please wait!")
    st.write(f"💡 Here's a joke while you wait: {get_joke()}")

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"Write a {word_count}-word blog post about {user_input}")
    
    return response.text if response else "⚠️ Error generating recipe!"

# Streamlit UI
st.title("Flavour Fusion: AI-Driven Recipe Blogging 🍲")

user_input = st.text_input("Enter a Recipe Topic", placeholder="Vegan Chocolate Cake")
word_count = st.number_input("Enter Word Count", min_value=100, max_value=2000, step=100)

if st.button("Generate Recipe"):
    if user_input and word_count:
        recipe = recipe_generation(user_input, word_count)
        st.text_area("Generated Recipe", value=recipe, height=300)
    else:
        st.warning("⚠️ Please enter a topic and word count!")
