import streamlit as st
import pronouncing
from xai_grok_sdk import XAI

# Load API key from Streamlit secrets
xai_api_key = st.secrets["XAI_API_KEY"]

# Initialize xAI clients
xai_text = XAI(api_key=xai_api_key, model="grok-2-1212")
xai_image = XAI(api_key=xai_api_key, model="grok-2-image-1212")

# Function to extract phonemes from a name
def get_phonemes(name):
    phonemes = pronouncing.phones_for_word(name.lower())
    return phonemes[0].split() if phonemes else []

# Function to map phonemes to chakras, Bhavas, and Rasas
def map_to_essence(phonemes):
    essence_map = {
        "p": ("Manipura", "Veera", "Energetic"),
        "b": ("Muladhara", "Shanta", "Peaceful"),
        "t": ("Manipura", "Raudra", "Fierce"),
        "d": ("Muladhara", "Shanta", "Stable"),
        "k": ("Manipura", "Veera", "Powerful"),
        "g": ("Muladhara", "Shanta", "Rooted"),
        "f": ("Vishuddha", "Karuna", "Gentle"),
        "v": ("Anahata", "Karuna", "Compassionate"),
        "θ": ("Sahasrara", "Shanta", "Ethereal"),
        "ð": ("Anahata", "Shanta", "Soft"),
        "s": ("Vishuddha", "Karuna", "Flowing"),
        "z": ("Anahata", "Shringara", "Loving"),
        "ʃ": ("Sahasrara", "Shanta", "Transcendent"),
        "ʒ": ("Anahata", "Shringara", "Expressive"),
        "h": ("Anahata", "Shanta", "Breath"),
        "m": ("Muladhara", "Shanta", "Peaceful"),
        "n": ("Ajna", "Shanta", "Intuitive"),
        "ŋ": ("Ajna", "Shanta", "Resonant"),
        "l": ("Svadhisthana", "Hasya", "Playful"),
        "r": ("Manipura", "Veera", "Dynamic"),
        "w": ("Svadhisthana", "Hasya", "Fluid"),
        "j": ("Vishuddha", "Shringara", "Creative"),
        "tʃ": ("Manipura", "Raudra", "Bold"),
        "dʒ": ("Anahata", "Shringara", "Vibrant"),
        "i": ("Vishuddha", "Shringara", "Creative"),
        "ɪ": ("Vishuddha", "Shringara", "Inspired"),
        "e": ("Anahata", "Karuna", "Open"),
        "ɛ": ("Anahata", "Karuna", "Heartfelt"),
        "æ": ("Manipura", "Veera", "Assertive"),
        "a": ("Manipura", "Veera", "Energetic"),
        "ɑ": ("Muladhara", "Shanta", "Grounded"),
        "ɔ": ("Svadhisthana", "Hasya", "Warm"),
        "o": ("Svadhisthana", "Hasya", "Joyful"),
        "u": ("Svadhisthana", "Hasya", "Playful"),
        "ʊ": ("Svadhisthana", "Hasya", "Cheerful"),
        "ʌ": ("Manipura", "Veera", "Strong"),
        "ə": ("Anahata", "Shanta", "Neutral"),
        "ɝ": ("Ajna", "Shanta", "Reflective"),
        "ɚ": ("Ajna", "Shanta", "Introspective"),
        "aɪ": ("Vishuddha", "Shringara", "Expressive"),
        "aʊ": ("Manipura", "Veera", "Adventurous"),
        "ɔɪ": ("Svadhisthana", "Hasya", "Lively"),
        "eɪ": ("Anahata", "Karuna", "Uplifting"),
        "oʊ": ("Svadhisthana", "Hasya", "Harmonious"),
    }
    for phoneme in phonemes:
        phoneme_key = phoneme.replace("0", "").replace("1", "").replace("2", "")
        if phoneme_key in essence_map:
            chakra, bhava, rasa = essence_map[phoneme_key]
            return {"chakra": chakra, "bhava": bhava, "essence": rasa.lower()}
    return {"chakra": "Anahata", "bhava": "Shanta", "essence": "neutral"}

# Function to generate lore using xAI Grok API
def generate_lore(essence):
    try:
        messages = [{"role": "user", "content": f"Generate a short lore (50-100 words) based on the essence: {essence}"}]
        response = xai_text.invoke(messages=messages)
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating lore: {str(e)}"

# Function to generate image using xAI Grok 2 Image Gen
def generate_image(essence):
    try:
        response = xai_image.generate_image(prompt=f"a {essence} scene, vibrant, detailed, artistic")
        return response.image_url
    except Exception as e:
        return f"Error generating image: {str(e)}"

# Streamlit UI
st.title("Name Essence Generator")
st.write("Enter a name like Mahan H R Gowda to discover its emotive essence, lore, and a visual representation.")

name = st.text_input("Enter a name", placeholder="e.g., Luna")
if st.button("Generate"):
    if name:
        with st.spinner("Generating..."):
            phonemes = get_phonemes(name)
            essence_data = map_to_essence(phonemes)
            lore = generate_lore(essence_data["essence"])
            image_url = generate_image(essence_data["essence"])

            st.subheader("Results")
            st.write(f"**Phonemes**: {' '.join(phonemes) if phonemes else 'Not found'}")
            st.write(f"**Chakra**: {essence_data['chakra']}")
            st.write(f"**Bhava**: {essence_data['bhava']}")
            st.write(f"**Essence (Rasa)**: {essence_data['essence'].capitalize()}")
            st.write(f"**Lore**: {lore}")
            if isinstance(image_url, str) and image_url.startswith("http"):
                st.image(image_url, caption=f"A {essence_data['essence']} scene")
            else:
                st.error(image_url)
    else:
        st.error("Please enter a name!")