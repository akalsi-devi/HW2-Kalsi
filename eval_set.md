# Evaluation Set: Meeting Summary → Action Items

## Case 1: Normal Case
**Input:** "Met with the product team. We reviewed the Q3 roadmap. 
Jane will update the feature list by Monday. Tom needs to schedule 
user interviews next week. Budget approval is still pending with finance."

**What a good output should do:** Summarize the roadmap review, list 
Jane and Tom's action items with deadlines.

---

## Case 2: Normal Case
**Input:** "Sales call with Acme Corp. They're interested in the enterprise 
plan but need a custom quote. Mike will send the pricing proposal by Thursday. 
Follow-up call scheduled for next Friday at 3pm."

**What a good output should do:** Note the sales interest, list Mike's 
action item with deadline, mention follow-up.

---

## Case 3: Edge Case — No Clear Action Items
**Input:** "Team standup. Everyone gave status updates. Things are generally 
on track. No blockers mentioned. Good vibes all around."

**What a good output should do:** Produce a short summary, handle the 
absence of action items gracefully without making them up.

---

## Case 4: Edge Case — Very Long/Messy Notes
**Input:** "Ok so we talked about a lot of things. First Sarah brought up 
the website redesign which has been delayed again because the contractor 
is slow. Then we got sidetracked talking about the holiday party. Bob 
thinks we should do a dinner, Lisa wants a daytime event. Then back to 
business - David needs to follow up with the contractor by Wednesday. 
Also someone needs to book the venue for the party but we didn't decide who."

**What a good output should do:** Extract the relevant business action 
items, ignore or briefly note the off-topic discussion.

---

## Case 5: Likely to Fail/Hallucinate — Ambiguous Ownership
**Input:** "Discussed the new hiring plan. Someone needs to post the job 
listings. The interviews should start next month. Compensation bands need 
to be finalized before we can move forward."

**What a good output should do:** List action items without inventing 
owners that weren't mentioned. Flag ambiguity rather than hallucinating names.