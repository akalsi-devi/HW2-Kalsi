import os
import anthropic

SYSTEM_PROMPT = """You are an expert meeting assistant. Given raw meeting notes, produce:

## Summary
2-3 sentences on key decisions, topics discussed, and outcomes.

## Action Items
List each action item as: [Owner or 'Unassigned'] - [Task] - [Due: date or 'No deadline mentioned']
If no action items exist, write: 'No action items identified.'

## Flags for Human Review
Note anything ambiguous, unresolved, or requiring follow-up that 
the model is not confident about.

Important: Never invent names, owners, or deadlines not present in the notes."""

def summarize_meeting(notes):
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": f"Please summarize these meeting notes:\n\n{notes}"}
        ]
    )

    return message.content[0].text

if __name__ == "__main__":
    test_notes = """
    Met with marketing team today. Sarah said the campaign is behind schedule.
    John needs to finish the designs by Friday. We also talked about the budget -
    it's been cut by 20%. Lisa will send a revised timeline to everyone by EOD.
    Next meeting is Thursday at 2pm.
    """

    result = summarize_meeting(test_notes)
    print("=== MEETING SUMMARY ===")
    print(result)

    with open("output.txt", "w") as f:
        f.write(result)
    print("\nOutput saved to output.txt")
