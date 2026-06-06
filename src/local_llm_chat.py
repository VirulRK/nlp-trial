import ollama
import sys

print("🤖 Local LLM Streaming Console Initialized.")
print("Talking to 'phi3' model offline... Type 'exit' to quit.\n")

while True:
    # 1. Capture user prompt
    user_prompt = input("You 👤 > ")
    
    if user_prompt.lower() in ['exit', 'quit']:
        print("Closing chat. Goodbye!")
        break
        
    if not user_prompt.strip():
        continue
        
    print("AI 🧠 > ", end="", flush=True)
    
    try:
        # 2. Send prompt to the local Ollama background server
        # We set stream=True so the model sends back data chunk-by-chunk
        response_stream = ollama.chat(
            model='phi3',
            messages=[{'role': 'user', 'content': user_prompt}],
            stream=True,
        )
        
        # 3. Stream the words live to the terminal screen
        for chunk in response_stream:
            # Print each word/token as it arrives without adding a new line
            print(chunk['message']['content'], end="", flush=True)
            
    except Exception as e:
        print(f"\n❌ Error connecting to Ollama: {e}")
        print("Make sure Ollama is running in your Windows system tray!")
        
    print("\n" + "-"*60)