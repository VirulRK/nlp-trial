import os
import spacy
from pynput.keyboard import Key, Controller

# Initialize the keyboard emulator
keyboard = Controller()

print("🧠 Loading local AI model with Hybrid Verification (en_core_web_md)...")
nlp = spacy.load("en_core_web_md")
print("✅ AI Model Loaded successfully.\n")

# Anchor definitions expanded for cleaner semantic routing
INTENT_ANCHORS = {
    "INTENT_MUTE": nlp("mute silent lower sound volume quiet stop"),
    "INTENT_UNMUTE": nlp("unmute sound audio volume loud speak"),
    "INTENT_NEXT_TRACK": nlp("skip forward next track song advance"),
    "INTENT_PREV_TRACK": nlp("go back previous track song rewind return"),
    "INTENT_PLAY_PAUSE": nlp("pause play resume stop toggle media playback"),
    "INTENT_VOL_UP": nlp("increase volume make louder raise higher turn up"),
    "INTENT_VOL_DOWN": nlp("decrease volume make quieter lower turn down")
}

def classify_intent_hybrid(user_text):
    """
    NLP PHASE 4: HYBRID CLASSIFICATION (FIXED)
    Combines expanded token overrides with vector fallback for bulletproof routing.
    """
    cleaned_text = user_text.lower().strip()
    user_doc = nlp(cleaned_text)
    
    # --- STEP 1: HARD TOKEN OVERRIDES (Instant 100% Matches) ---
    words = [token.text for token in user_doc]
    
    # Track Navigation
    if "next" in words or "advance" in words or "forward" in words:
        return "INTENT_NEXT_TRACK", 1.0
    if "prev" in words or "previous" in words or "back" in words or "rewind" in words:
        return "INTENT_PREV_TRACK", 1.0
        
    # Play / Pause Fix
    if "pause" in words or "play" in words or "stop" in words or "toggle" in words:
        return "INTENT_PLAY_PAUSE", 1.0
        
    # Mute / Unmute Fix
    if "unmute" in words:
        return "INTENT_UNMUTE", 1.0
    if "mute" in words or "silent" in words or "shush" in words:
        return "INTENT_MUTE", 1.0
        
    # Volume Control
    if "up" in words or "increase" in words or "louder" in words or "raise" in words:
        return "INTENT_VOL_UP", 1.0
    if "down" in words or "decrease" in words or "quieter" in words or "lower" in words:
        return "INTENT_VOL_DOWN", 1.0

    # --- STEP 2: FALLBACK TO VECTOR SIMILARITY ---
    best_intent = "UNKNOWN_INTENT"
    highest_similarity_score = 0.0
    
    for intent_name, anchor_doc in INTENT_ANCHORS.items():
        score = user_doc.similarity(anchor_doc)
        if score > highest_similarity_score:
            highest_similarity_score = score
            best_intent = intent_name
            
    CONFIDENCE_THRESHOLD = 0.65
    if highest_similarity_score < CONFIDENCE_THRESHOLD:
        return "UNKNOWN_INTENT", highest_similarity_score
        
    return best_intent, highest_similarity_score

# --- MAIN TERMINAL ENGINE LOOP ---
print("====================================================")
print("🤖 Hybrid Local AI Command Console Online V3.0      ")
print("Tokens and Vectors are fully synced. Test away!     ")
print("Type 'exit' or 'quit' to terminate the loop.       ")
print("====================================================\n")

while True:
    user_input = input("User Prompt 👤 > ")
    
    if user_input.lower() in ['exit', 'quit']:
        print("Shutting down AI Engine. Goodbye!")
        break
        
    if not user_input.strip():
        continue
        
    # Execute Hybrid Engine Matcher
    intent, confidence = classify_intent_hybrid(user_input)
    
    print(r"  └── [AI Analysis]:")
    print(f"      ├── Intent Match: {intent}")
    print(f"      └── Confidence:   {confidence:.2%}")
    
    # --- HOTKEY EXECUTION MAPPING ---
    if intent == "INTENT_MUTE":
        print("  ⚡ [OS ACTION]: Executing Mute...")
        keyboard.press(Key.media_volume_mute)
        keyboard.release(Key.media_volume_mute)
        
    elif intent == "INTENT_UNMUTE":
        print("  ⚡ [OS ACTION]: Executing Unmute...")
        keyboard.press(Key.media_volume_mute)
        keyboard.release(Key.media_volume_mute)
        
    elif intent == "INTENT_NEXT_TRACK":
        print("  ⚡ [OS ACTION]: Skipping Forward...")
        keyboard.press(Key.media_next)
        keyboard.release(Key.media_next)
        
    elif intent == "INTENT_PREV_TRACK":
        print("  ⚡ [OS ACTION]: Rewinding Back...")
        keyboard.press(Key.media_previous)
        keyboard.release(Key.media_previous)
        
    elif intent == "INTENT_PLAY_PAUSE":
        print("  ⚡ [OS ACTION]: Toggling Playback State...")
        keyboard.press(Key.media_play_pause)
        keyboard.release(Key.media_play_pause)
        
    elif intent == "INTENT_VOL_UP":
        print("  ⚡ [OS ACTION]: Pumping Volume Up...")
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        
    elif intent == "INTENT_VOL_DOWN":
        print("  ⚡ [OS ACTION]: Dropping Volume Down...")
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        
    else:
        print("  ❌ [OS ACTION]: Target intent unclear. Please rephrase.")
    print("-" * 65)