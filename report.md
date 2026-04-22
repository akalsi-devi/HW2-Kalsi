# HW2 Report: Meeting Summary → Action Items Prototype

## Business Use Case
Many professionals spend significant time manually summarizing meetings 
and distributing action items. This prototype automates that process by 
taking raw meeting notes as input and producing a structured summary, 
action item list, and flags for human review.

- **User:** Office workers, project managers, executive assistants
- **Input:** Raw, unstructured meeting notes
- **Output:** Structured summary, action items with owners and deadlines, 
  and flagged ambiguities
- **Value:** Saves time, reduces errors, ensures action items are tracked

## Model Choice
I used Claude Haiku 4.5 via the Anthropic API. I chose it because it is 
fast, affordable, and sufficient for a structured summarization task that 
does not require deep reasoning.

## Baseline vs. Final Design

**Version 1 (baseline):** Simple prompt asking for a summary and bullet 
list. Output was readable but inconsistent — sometimes invented owners, 
didn't handle missing action items gracefully.

**Version 2:** Added explicit formatting instructions and told the model 
not to invent owners. Output improved but still lacked a way to flag 
ambiguity.

**Version 3 (final):** Added a "Flags for Human Review" section and 
changed unknown owners to "Unassigned." Output is now structured, 
consistent, and honest about what it doesn't know.

## Where the Prototype Still Fails
The model occasionally misses implied action items or flags too many 
things for human review when notes are clear. It also cannot verify 
whether deadli