Local NLP & Generative AI Evolution 🤖🧠
This repository documents my hands-on journey from the fundamentals of Natural Language Processing (NLP) to deploying Generative Large Language Models (LLMs) entirely offline. By moving away from cloud-based abstractions, this project explores the underlying engineering mechanics of text processing across three distinct architectural phases.

📂 Project Architecture

Phase 1: Deterministic Text Normalization
File: text_controller.py (Initial Version)
Concepts: Tokenization, Lowercasing, Regex Punctuation Stripping.
Core Logic: A rule-based terminal string engine that captures raw human input and uses keyword arrays to trigger native OS media keys via pynput.

Phase 2: Semantic Vector Spaces
File: text_controller.py (Refined Version)
Concepts: Word Embeddings, Cosine Similarity, Hybrid Token Validation.
Core Logic: Implements local machine learning using spaCy (en_core_web_md). It calculates the geometric distance between user text and anchor intents to understand context and synonyms (e.g., mapping "Advance the track" to a skip command).
Hybrid Layer: Includes strict string token checks to prevent the vector engine from confusing directional opposites (like "next" vs. "previous") that occupy adjacent coordinates.

Phase 3: Local Generative AI Streaming
File: local_llm_chat.py
Concepts: Model Quantization, Local Runtimes, Token Streams.
Core Logic: Connects Python to an offline Ollama server running Microsoft's 3.8-billion parameter phi3 model. Features real-time token streaming (stream=True) to feed generated characters directly into the terminal with zero cloud latency.


⚙️ Local Setup & Requirements

1. Install Dependencies
Ensure you have the required text processing, environment control, and hardware emulation libraries installed:


pip install spacy pynput ollama click
python -m spacy download en_core_web_md


2. Configure Local Model
Download and launch Ollama, then pull the local model weight packet:


ollama run phi3


3. Execution
Run the respective scripts from your workspace directory to test the pipelines:


# To test NLP text control
python text_controller.py

# To test local generative streaming
python local_llm_chat.py


Built as part of an exploration into offline, low-latency AI engineering.
