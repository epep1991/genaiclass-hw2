import anthropic
import os
import datetime
import time

# --- Configuration ---
API_KEY = os.environ.get("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")
client = anthropic.Anthropic(api_key=API_KEY)

# --- System Prompt (Version 3) ---
SYSTEM_PROMPT = """
You are an expert content marketer and business writer.
Your job is to turn a structured content brief into a polished first-draft blog post.

Follow these rules:
- Write a clear, compelling headline
- Open with a hook that speaks directly to the reader's pain point — make it specific
  and human, not generic
- Cover all key points from the brief in the body
- Match the tone specified in the brief exactly — this is critical. A compliance-aware
  post for financial advisors should sound nothing like a provocative op-ed for CEOs.
  Let the tone shape the vocabulary, sentence length, and level of assertiveness.
- End with a call to action that directly echoes the opening hook — close the loop
  so the reader feels the post came full circle
- Keep the post between 200 and 300 words
- Do not invent statistics, customer names, or citations not provided in the brief

Avoid the following at all costs:
- AI clichés: "game-changer", "revolutionize", "leverage", "unlock", "seamlessly",
  "in today's fast-paced world", "the future is here", "dive in"
- Vague filler sentences that don't add information
- Passive voice where active voice is possible
- Generic transitions like "Furthermore" or "In conclusion"
- Writing every post in the same voice — each brief has a distinct audience and
  purpose, and the writing should reflect that
"""

# --- Content Briefs ---
briefs = [
    {
        "id": "case_1_normal",
        "brief": """
Topic: Introducing an AI-powered analytics dashboard for mid-market SaaS companies
Audience: Operations managers and RevOps leads at companies with 50-500 employees
Tone: Professional, confident, slightly conversational
Tone notes: This is a product announcement. Write like a sharp SaaS marketer —
  clear, benefit-driven, no fluff. The reader is busy and skeptical of hype.
Key points:
- Real-time data visibility across sales, marketing, and support
- No-code setup, integrates with existing tools
- Cuts reporting time by up to 60%
- Early access available
"""
    },
    {
        "id": "case_2_edge",
        "brief": """
Topic: How vector embeddings power modern AI search
Audience: Marketing managers with no engineering background
Tone: Friendly, jargon-free, uses analogies
Tone notes: Write like a patient, smart friend explaining something over coffee.
  Use at least one concrete analogy. Never talk down to the reader.
Key points:
- Traditional keyword search misses meaning
- Embeddings convert text into numbers that capture meaning
- This is why AI search feels more intuitive
- Practical implication: better content discovery for users
"""
    },
    {
        "id": "case_3_hallucination_risk",
        "brief": """
Topic: Something about AI and productivity
Audience: Professionals
Tone: Not specified
Tone notes: The brief is intentionally vague. Do not invent specifics to fill gaps.
  Write a general but honest post and flag where a real author would need to add
  specific examples or data.
Key points:
- AI is changing work
- People should use it
"""
    },
    {
        "id": "case_4_human_review",
        "brief": """
Topic: How AI can help financial advisors identify at-risk client portfolios
Audience: Certified financial advisors at independent RIA firms
Tone: Authoritative, cautious, compliance-aware
Tone notes: This audience is highly regulated and risk-aware. Write with precision
  and restraint. Shorter sentences. No enthusiasm or hype. Include a clear disclaimer
  that this content is not investment advice and that advisors retain full judgment.
Key points:
- AI flags unusual portfolio drift patterns
- Advisors retain full decision-making authority
- Tool is meant to assist, not replace, human judgment
- Must note that outputs are not investment advice
"""
    },
    {
        "id": "case_5_thought_leadership",
        "brief": """
Topic: Why most companies are implementing AI wrong
Audience: C-suite executives and senior leaders at mid-to-large companies
Tone: Bold, direct, slightly provocative but backed by reasoning
Tone notes: This is an op-ed, not a listicle. Take a strong point of view and
  defend it. Do not hedge every sentence. Write like a respected consultant who
  has seen too many failed AI pilots and has something real to say about it.
Key points:
- Most AI pilots fail because they automate broken processes
- The right approach is to redesign the workflow first
- AI should amplify human judgment, not replace it
- Leaders need to invest in change management, not just technology
"""
    },
]

# --- Generate one post ---
def generate_post(brief_text):
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": "Here is the content brief:\n" + brief_text}
        ]
    )
    return message.content[0].text

# --- Main ---
def main():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"outputs_{timestamp}.md"

    with open(output_file, "w") as f:
        for item in briefs:
            print(f"Generating: {item['id']}...")
            result = generate_post(item["brief"])
            f.write(f"# {item['id']}\n\n")
            f.write(result)
            f.write("\n\n---\n\n")
            print(f"Done: {item['id']}\n")
            time.sleep(2)

    print(f"\nAll outputs saved to: {output_file}")

if __name__ == "__main__":
    main()