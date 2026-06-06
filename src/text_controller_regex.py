import os
import re  # Python's built-in Regular Expressions library
from pynput.keyboard import Key, Controller

# Initialize our familiar keyboard executor
keyboard = Controller()

def clean_and_normalize_text(raw_text):
    """
    NLP STEP 1: TEXT NORMALIZATION
    Takes messy human typing, drops it to lowercase, and strips all punctuation.
    """
    # Convert to lowercase
    lowercase_text = raw_text.lower()
    
    # Regex: replace everything that is NOT a alphanumeric character or space with nothing
    cleaned_text = re.sub(r'[^\w\s]', '', lowercase_text)
    
    # Split the sentence into an array of individual words (Tokenization)
    tokens = cleaned_text.split()
    
    return cleaned_text, tokens

def parse_user_intent(cleaned_text):
    """
    NLP STEP 2: INTENT CLASSIFICATION
    Scans the normalized text against keyword arrays to determine what the user wants.
    """
    # Define our structural keyword dictionaries (Lexicons)
    mute_keywords = ["mute", "silent", "quiet", "shush"]
    unmute_keywords = ["unmute", "sound", "volume", "loud"]
    skip_keywords = ["next", "skip", "forward"]
    prev_keywords = ["previous", "back", "rewind"]
    pause_keywords = ["pause", "play", "stop", "toggle"]

    # Match the intent
    if any(word in cleaned_text for word in mute_keywords):
        # Edge check case: "unmute" contains the word "mute"! 
        # We must ensure "unmute" wasn't actually said.
        if "unmute" not in cleaned_text:
            return "INTENT_MUTE"
            
    if any(word in cleaned_text for word in unmute_keywords):
        return "INTENT_UNMUTE"
        
    if any(word in cleaned_text for word in skip_keywords):
        return "INTENT_NEXT_TRACK"
        
    if any(word in cleaned_text for word in prev_keywords):
        return "INTENT_PREV_TRACK"
        
    if any(word in cleaned_text for word in pause_keywords):
        return "INTENT_PLAY_PAUSE"
        
    return "UNKNOWN_INTENT"

# --- MAIN TERMINAL ENGINE LOOP ---
print("=============================================")
print("🤖 Local NLP Command Console Online V1.0     ")
print("Type a command (e.g., 'Hey, please mute the sound!')")
print("Type 'exit' or 'quit' to close the engine.   ")
print("=============================================\n")

while True:
    # Read raw string input from user keyboard
    user_input = input("User Prompt 👤 > ")
    
    if user_input.lower() in ['exit', 'quit']:
        print("Shutting down NLP Engine. Goodbye!")
        break
        
    if not user_input.strip():
        continue
        
    # Run text normalization pipeline
    normalized_str, word_tokens = clean_and_normalize_text(user_input)
    
    # Extract intent classification
    intent = parse_user_intent(normalized_str)
    
    print(r"  └── [Normalized Text]:", f"'{normalized_str}'")
    print(r"  └── [Word Tokens]:   ", word_tokens)
    
    # --- STEP 3: NATIVE HOTKEY EXECUTION ---
    if intent == "INTENT_MUTE":
        print("  ⚡ [OS ACTION]: Executing System Mute...")
        # Since Windows media mute is a toggle, we'll assume it handles state natively
        keyboard.press(Key.media_volume_mute)
        keyboard.release(Key.media_volume_mute)
        
    elif intent == "INTENT_UNMUTE":
        print("  ⚡ [OS ACTION]: Executing System Unmute...")
        keyboard.press(Key.media_volume_mute)
        keyboard.release(Key.media_volume_mute)
        
    elif intent == "INTENT_NEXT_TRACK":
        print("  ⚡ [OS ACTION]: Skipping to Next Track...")
        keyboard.press(Key.media_next)
        keyboard.release(Key.media_next)
        
    elif intent == "INTENT_PREV_TRACK":
        print("  ⚡ [OS ACTION]: Jumping to Previous Track...")
        keyboard.press(Key.media_previous)
        keyboard.release(Key.media_previous)
        
    elif intent == "INTENT_PLAY_PAUSE":
        print("  ⚡ [OS ACTION]: Toggling Playback State...")
        keyboard.press(Key.media_play_pause)
        keyboard.release(Key.media_play_pause)
        
    else:
        print("  ❌ [OS ACTION]: Intent unrecognized. Please rephrase your command.")
    print("-" * 50)
