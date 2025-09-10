# CloudLift Agent — Day 1 Starter

This starter contains **Day 1** deliverables: a focused demo scenario, starter repo layout, sample inventory data, and a draft architecture sketch.

## What you’ll do on Day 1
1) Join the hackathon & request credits/Kiro (see `devpost/idea_pitch.txt`).  
2) Pick the demo scope (2–3 small apps).  
3) Save your **sample inventory** (CSV/JSON) in `sample_data/`.  
4) Review acceptance criteria in `tasks/day1_checklist.md`.  
5) Commit + push to GitHub.

## Repo layout (initial)
```
architecture/diagram.mmd     # Mermaid architecture diagram (edit online or locally)
sample_data/inventory.csv    # Example CMDB-like inventory for 3 small apps
sample_data/inventory.json   # Same as JSON
sample_data/golden_plan.json # Example agent output shape for planning
agent/prompts/system.md      # System prompt scaffold
agent/prompts/fewshots.md    # Few-shot examples scaffold
tasks/day1_checklist.md      # Acceptance criteria + task list
scripts/seed_demo.sh         # (Optional) seed helper (placeholder)
devpost/idea_pitch.txt       # Copy/paste 2–3 line idea + checklist for submission page
```

> **Note:** All provisioning is optional at this stage. Keep the Day 1 focus on **scope + data + criteria**.

## Next
On Day 2–3 you’ll attach Bedrock AgentCore tools and wire the first planning chain.