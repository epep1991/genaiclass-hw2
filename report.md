# HW2 Report — Content Brief to Blog Post Generator

## Business Use Case

Content marketing teams spend significant time turning strategic briefs into
publishable first drafts. A typical brief-to-post workflow involves a writer
interpreting the brief, drafting, and iterating — often taking 2-4 hours per post.

This prototype automates the first-draft step: given a structured content brief
(topic, audience, tone, key points), it produces a 200-300 word blog post draft
ready for human review and editing. The target user is a content marketer or
consultant managing multiple clients or campaigns simultaneously.

## Model Choice

I used Claude Haiku (claude-haiku-4-5-20251001) via the Anthropic API. I originally
attempted to use Google Gemini (gemini-2.0-flash) via Google AI Studio, but hit
free-tier rate limits during testing. I switched to Claude Haiku because I already
had API access, and Haiku is fast, inexpensive, and well-suited for structured
writing tasks that don't require deep reasoning.

## Baseline vs. Final Design

**Version 1 (baseline):** A simple system prompt asking for a headline, hook, key
points, and CTA. Output quality was acceptable but generic — hooks were decent,
but body copy relied heavily on AI clichés and all 5 posts sounded similar
regardless of audience or tone brief.

**Version 2:** Added explicit banned phrases ("game-changer", "revolutionize",
"seamlessly", etc.), required the CTA to echo the opening hook, and pushed for
more human and specific language. Quality improved noticeably — less filler,
stronger narrative arc — but voice differentiation across cases remained weak.

**Version 3 (final):** Added per-brief tone notes giving the model specific
direction for each case, added an explicit instruction to differentiate voice
across posts, and reduced word count to 200-300 words. This produced the strongest
results — the financial advisor post was notably more restrained and precise, while
the CEO op-ed was more assertive and direct. Shorter format eliminated padding and
made the hook/CTA loop tighter.

## Where the Prototype Still Fails

Case 3 (vague brief) consistently produced generic output regardless of prompt
version. With almost no input to work with, the model defaulted to filler — broad
claims about AI with no specifics. This is expected behavior, not a bug, but it
confirms that the workflow requires a reasonably complete brief to produce usable
output. Any post generated from a vague brief needs heavy human editing before
publication.

The financial advisor case (Case 4) also requires mandatory compliance review before
publishing. The model included appropriate disclaimers, but whether the framing meets
regulatory standards is a legal question, not a writing question.

## Deployment Recommendation

I would recommend deploying this workflow in a limited capacity — specifically as a
first-draft tool for experienced content marketers who will review and edit every
output before publication. It should not be used to publish directly without human
review.

Deployment conditions:
- Brief must meet a minimum quality threshold (topic, audience, tone, and at least
  3 key points required)
- All outputs reviewed by a human editor before publishing
- Financial, legal, or medical topics require specialist review regardless of output
  quality
- The system should be re-evaluated if the underlying model changes