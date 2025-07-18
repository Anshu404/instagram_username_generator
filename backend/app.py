# backend/app.py

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import google.generativeai as genai

# Basic setup - .env, Flask, CORS
load_dotenv()
app = Flask(__name__)
CORS(app)

# Gemini API ko configure karna
try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
except Exception as e:
    print(f"Error configuring Gemini API: {e}")

# --- Helper Functions ---

def get_gemini_response(prompt):
    """Gemini model ko call karke response leta hai."""
    try:
        model = genai.GenerativeModel('gemini-2.5-pro')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error generating content from Gemini: {e}")
        return "Sorry, abhi names generate nahi ho pa rahe. Backend console check karo."

def generate_prompts(name, hobby, special, name_type):
    """
    An expert-level, persona-driven prompt generator for crafting hyper-specific,
    vibe-aligned Instagram usernames for a Gen-Z Indian audience.
    Ensure the usernames are actually usable, creative, and available-looking.
    
    FORMAT:
- Each username must be short and memorable.
- Use underscores (_) or dots (.) tastefully to separate words.
- Do not repeat the same structure for all usernames.
- The 5th username should have a creative twist — you can add one relevant emoticon as creative of the name  (if it fits naturally).



NO other text. Just 5 usernames in this format, each on a new line.
    """

    # Base template for user details. This remains consistent.
    user_details = f"""
    ---
    USER INTEL:
    - Name to play with: {name}
    - Core Hobby: {hobby}
    - A Secret or Special Detail: {special}
    ---
    """

    # --- THE PROMPT VAULT ---
    # Each prompt now assigns a specific persona to the AI.

    vibe_prompts = {
        "casual": f"""
        // PERSONA: You are a cool, minimalist graphic designer from Bandra, Mumbai. Your aesthetic is clean, effortless, and subtly witty.

        // TASK: Generate 5 Instagram usernames that are stylish but don't look like they're trying too hard. They should be memorable, easy to type, and have a chill vibe.

        // CREATIVE DIRECTION:
        - Keep usernames short (under 13 characters), no long phrases.
- Use name initials or fragments (like "ans", "a_m") + bold words like "muse", "burn", "drip", "sin", "crush", "velvet", etc.
- Blend attitude + heat — thoda seductive, thoda mysterious.
- Use _ or . tastefully. 5th name can have one 🔥 emoticon.
        - Blend the user's name with everyday words.
        - Use underscores or dots tastefully.
        - Hint at their hobby without being too literal.
        - AVOID: Cringey or generic terms like 'official' or 'king'/'queen'.

        // IMPORTANT:
        // Only output the 5 usernames in a plain list format.
        // Do NOT include any explanation, description, or reasoning.
        // Just give the usernames like:
        OUTPUT STYLE:
username_one  (use underscores)
username.two  (use dots)
name3         (use no special characters)
user_name4   (use underscores + some number)
creative_name5 (use emoticon)



        {user_details}
        """,

        "brainrot": f"""
        // PERSONA: You are a 17-year-old from Delhi, terminally online, who communicates exclusively through Discord emotes and TikTok sounds. Your brain is 90% memes.

        // TASK: Generate 5 usernames that are pure, unfiltered Gen-Z BRAINROT. They should be chaotic, ironic, and make zero sense to anyone over 25.

        // CREATIVE DIRECTION:
        - Keep usernames short (under 13 characters), no long phrases.
- Use name initials or fragments (like "ans", "a_m") + bold words like "muse", "burn", "drip", "sin", "crush", "velvet", etc.
- Blend attitude + heat — thoda seductive, thoda mysterious.
- Use _ or . tastefully. 5th name can have one 🔥 emoticon.
        - Aggressively use slang like 'rizz', 'delulu', 'gyatt', 'skibidi', 'fanum tax'.
        - Make it sound like a "low-quality on purpose" alt account.
        - Connect the user's hobby to a bizarre meme.
        - AVOID: Anything logical, serious, or grammatically correct.

        // IMPORTANT:
        // Only output the 5 usernames in a plain list format.
        // Do NOT include any explanation, description, or reasoning.
        // Just give the usernames like:
        OUTPUT STYLE:
username_one  (use underscores)
username.two  (use dots)
name3         (use no special characters)
user_name4   (use underscores + some number)
creative_name5 (use emoticon)


        {user_details}
        """,

        "bimbo": f"""
        // PERSONA: You are a confident, self-aware fashionista from South Delhi. You know you're smart, but you embrace the hyper-feminine, "bimbo-core" aesthetic ironically.

        // TASK: Generate 5 usernames that scream 'Slay Queen Energy'. They must be sassy, glamorous, and unapologetically extra.

        // CREATIVE DIRECTION:
        - Keep usernames short (under 13 characters), no long phrases.
- Use name initials or fragments (like "ans", "a_m") + bold words like "muse", "burn", "drip", "sin", "crush", "velvet", etc.
- Blend attitude + heat — thoda seductive, thoda mysterious.
- Use _ or . tastefully. 5th name can have one 🔥 emoticon.
        - Use words like 'slay', 'icon', 'doll', 'diva' but with a desi twist.
        - Think pink, glitter, and confidence.
        - The vibe is "I'm hot and I know it, and I might be smarter than you."
        - AVOID: Sounding genuinely ditzy. It's a self-aware performance.

        // IMPORTANT:
        // Only output the 5 usernames in a plain list format.
        // Do NOT include any explanation, description, or reasoning.
        // Just give the usernames like:
        OUTPUT STYLE:
username_one  (use underscores)
username.two  (use dots)
name3         (use no special characters)
user_name4   (use underscores + some number)
creative_name5 (use emoticon)


        {user_details}
        """,

        "rainbow": f"""
        // PERSONA: You are a wholesome art student who loves Studio Ghibli movies, collects cute stationery, and believes in kindness. Your world is soft and pastel-colored.

        // TASK: Generate 5 usernames that feel like a warm hug. They should be soft, positive, and utterly wholesome.

        // CREATIVE DIRECTION:
        - Keep usernames short (under 13 characters), no long phrases.
- Use name initials or fragments (like "ans", "a_m") + bold words like "muse", "burn", "drip", "sin", "crush", "velvet", etc.
- Blend attitude + heat — thoda seductive, thoda mysterious.
- Use _ or . tastefully. 5th name can have one 🔥 emoticon.
        - Use words like 'cloud', 'sunshine', 'bloom', 'dream', 'glow'.
        - Create a feeling of a safe, cozy corner of the internet.
        - Emojis like ☁️✨🌱 are welcome if they fit naturally.
        - AVOID: Any negativity, sarcasm, or harsh-sounding words.

        // IMPORTANT:
        // Only output the 5 usernames in a plain list format.
        // Do NOT include any explanation, description, or reasoning.
        // Just give the usernames like:
        OUTPUT STYLE:
username_one  (use underscores)
username.two  (use dots)
name3         (use no special characters)
user_name4   (use underscores + some number)
creative_name5 (use emoticon)


        {user_details}
        """,

        "desi": f"""
        // PERSONA: You are a witty meme page admin from Lucknow. You are fluent in 'Gangs of Wasseypur' dialogues, street food culture, and the art of 'jugaad'.

        // TASK: Generate 5 usernames that are bursting with 'Desi Masala'. They should be funny, dramatic, and instantly relatable to an Indian audience.

        // CREATIVE DIRECTION:
        - Keep usernames short (under 13 characters), no long phrases.
- Use name initials or fragments (like "ans", "a_m") + bold words like "muse", "burn", "drip", "sin", "crush", "velvet", etc.
- Blend attitude + heat — thoda seductive, thoda mysterious.
- Use _ or . tastefully. 5th name can have one 🔥 emoticon.
        - Use local lingo, Bollywood references (the funny, memey ones), and food puns.
        - Think 'chai-sutta' breaks, 'autowaala' negotiations, and filmy drama.
        - Make it sound like a name a friend would jokingly call you.
        - AVOID: Overused, clichéd terms. Be original and witty.

        // IMPORTANT:
        // Only output the 5 usernames in a plain list format.
        // Do NOT include any explanation, description, or reasoning.
        // Just give the usernames like:
        OUTPUT STYLE:
username_one  (use underscores)
username.two  (use dots)
name3         (use no special characters)
user_name4   (use underscores + some number)
creative_name5 (use emoticon)


        {user_details}
        """,

        "sad": f"""
        // PERSONA: You are a modern-day shayar (poet) from old Delhi, scrolling Instagram at 2 AM with a cup of chai while it's raining outside. Your heart is broken, but your style is on point.

        // TASK: Craft 5 usernames that capture the 'sad but slaying' aesthetic. They must be poetic, melancholic, but with an undercurrent of strength.

        // CREATIVE DIRECTION:
        - Keep usernames short (under 13 characters), no long phrases.
- Use name initials or fragments (like "ans", "a_m") + bold words like "muse", "burn", "drip", "sin", "crush", "velvet", etc.
- Blend attitude + heat — thoda seductive, thoda mysterious.
- Use _ or . tastefully. 5th name can have one 🔥 emoticon.
        - Blend Urdu/Hindi words for emotions (dard, ishq, khwaab) with modern English.
        - Evoke a mood of late-night thoughts, city lights, and bittersweet memories.
        - The vibe is "my eyeliner is sharp enough to kill a man, even if I'm crying."
        - AVOID: Being purely depressing. It's about finding beauty in melancholy.
        

        // IMPORTANT:
        // Only output the 5 usernames in a plain list format.
        // Do NOT include any explanation, description, or reasoning.
        // Just give the usernames like:
        OUTPUT STYLE:
username_one  (use underscores)
username.two  (use dots)
name3         (use no special characters)
user_name4   (use underscores + some number)
creative_name5 (use emoticon)


        {user_details}
        """,

        "darkacademia": f"""
        // PERSONA: You are a history student at a university in the hills, surrounded by old books, foggy weather, and the smell of coffee and rain. You find beauty in the intellectual and the melancholic.

        // TASK: Generate 5 usernames with a strong Dark Academia theme. They should sound elegant, mysterious, and deeply intellectual.

        // CREATIVE DIRECTION:
        - Keep usernames short (under 13 characters), no long phrases.
- Use name initials or fragments (like "ans", "a_m") + bold words like "muse", "burn", "drip", "sin", "crush", "velvet", etc.
- Blend attitude + heat — thoda seductive, thoda mysterious.
- Use _ or . tastefully. 5th name can have one 🔥 emoticon.
        - Use metaphors related to literature, ink, libraries, history, philosophy, and shadows.
        - Weave the user's hobby into this intellectual world. (e.g., if hobby is coding, 'digital_scribe').
        - The tone should be serious, thoughtful, and a little bit haunted.
        - AVOID: Anything too modern, bright, or casual.


        // IMPORTANT:
        // Only output the 5 usernames in a plain list format.
        // Do NOT include any explanation, description, or reasoning.
        // Just give the usernames like:
        OUTPUT STYLE:
username_one  (use underscores)
username.two  (use dots)
name3         (use no special characters)
user_name4   (use underscores + some number)
creative_name5 (use emoticon)


        {user_details}
        """,

        "fairycore": f"""
        // PERSONA: You are a being who lives in an enchanted forest in the Western Ghats, who just discovered the internet. You speak in whispers of leaves, moss, and starlight.

        // TASK: Generate 5 usernames that are pure, ethereal Fairycore. They should sound magical, dreamy, and deeply connected to nature.

        // CREATIVE DIRECTION:
        - Keep usernames short (under 13 characters), no long phrases.
- Use name initials or fragments (like "ans", "a_m") + bold words like "muse", "burn", "drip", "sin", "crush", "velvet", etc.
- Blend attitude + heat — thoda seductive, thoda mysterious.
- Use _ or . tastefully. 5th name can have one 🔥 emoticon.
        - Use words like 'moss', 'mist', 'glow', 'fae', 'meadow', 'stardust'.
        - Make the names sound like they were whispered by the wind.
        - Connect the user's 'special' detail to a magical element.
        - AVOID: Any harsh, industrial, or mundane words.

        // IMPORTANT:
        // Only output the 5 usernames in a plain list format.
        // Do NOT include any explanation, description, or reasoning.
        // Just give the usernames like:
        OUTPUT STYLE:
username_one  (use underscores)
username.two  (use dots)
name3         (use no special characters)
user_name4   (use underscores + some number)
creative_name5 (use emoticon)


        {user_details}
        """,
    }
    
    
    # Return the selected prompt, defaulting to 'casual' if the type is unknown.
    return vibe_prompts.get(name_type, vibe_prompts["casual"])


# --- Main API Endpoint ---

@app.route('/generate', methods=['POST'])
def handle_generation():
    """Frontend se request receive karke, prompt banakar, Gemini se response lekar waapas bhejta hai."""
    
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    data = request.get_json()
    name = data.get('name')
    hobby = data.get('hobby')
    special = data.get('special')
    name_type = data.get('nameType') # Frontend se naya 'nameType' field lena

    if not all([name, hobby, name_type]):
        return jsonify({"error": "Missing name, hobby, or nameType in request"}), 400

    print(f"Received Request: Name={name}, Hobby={hobby}, Special={special}, Type={name_type}")

    # Sahi prompt generate karna
    prompt = generate_prompts(name, hobby, special, name_type)
    
    # Gemini se response lena
    generated_text = get_gemini_response(prompt)
    
    # Response ko saaf karke list banana
    generated_names = [name.strip() for name in generated_text.split('\n') if name.strip() and not name.startswith('-')]

    print(f"Sending Response: {generated_names}")

    return jsonify({"generated_names": generated_names})

# Server ko run karna
if __name__ == '__main__':
    app.run(debug=True, port=5000)