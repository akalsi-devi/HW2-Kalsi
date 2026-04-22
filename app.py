import os
import anthropic

SYSTEM_PROMPT = """You are a helpful assistant that summarizes meeting notes.
Given raw meeting notes, produce:
1. A 2-3 sentence summary of the meeting
2. A bullet list of action items with owners if mentioned"""

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
