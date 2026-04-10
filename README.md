# HW2 — Content Brief to Blog Post Generator

**Course:** Generative AI for Business — JHU Carey Business School (Spring 2026)
**Student:** Eric Pou

## What This Does

This prototype takes a structured content brief (topic, audience, tone, key points)
and uses an LLM to generate a polished first-draft blog post. It is designed for
content marketers who need to accelerate the brief-to-draft step without sacrificing
quality or brand voice.

## Workflow

- **Input:** Structured content brief with topic, audience, tone, and key points
- **Output:** 200-300 word first-draft blog post saved to a timestamped .md file
- **Model:** Claude Haiku (claude-haiku-4-5-20251001) via Anthropic API

## Repository Structure

    hw2/
    ├── README.md         — this file
    ├── app.py            — main Python script
    ├── prompts.md        — 3 prompt versions with observations
    ├── eval_set.md       — 5 test cases with quality criteria
    └── report.md         — findings and deployment recommendation

## How to Run

1. Set your Anthropic API key as an environment variable:
   export ANTHROPIC_API_KEY="your-key-here"

2. Install dependencies:
   pip3 install anthropic --break-system-packages

3. Run the script:
   python3 app.py

Output is saved to outputs_TIMESTAMP.md in the same folder.

## Video Walkthrough

[Add YouTube link here after recording]