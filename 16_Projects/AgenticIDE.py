তাহলে কোথায় Planning?

Planning হচ্ছে:
Goal
↓
Break Goal
↓
Execute
↓
Observe
↓
Update Plan
↓
Execute Next

Example
Goal
↓
Need JWT
↓
Need Package
↓
Need Config
↓
Need Middleware
↓
Need Test


কোথায় Function Calling?:
LLM
↓
read_file()
↓
write_file()
↓
run_terminal()
↓
git_commit()
↓
browser_open()
সব Function Call।



কোথায় Reasoning?:
Read Error
↓
Understand
↓
Why?
↓
Generate Fix
এটাই Reasoning।



কোথায় Memory?:
Agent মনে রাখে Already Read Program.cs, Already Installed Package, Already Modified appsettings.json যাতে আবার না করে।

কোথায় RAG?:
যদি Documentation লাগে
User
↓
Need JWT
↓
Search Docs
↓
Relevant Documentation
↓
LLM


কোথায় Reflection?:
Build Fail
↓
নিজের Code দেখে
↓
ভুল বুঝে
↓
Fix করে
↓
আবার Compile
এটাকে Reflection Loop বলে।



পুরো Agent Architecture:
                    User Goal
                         │
                         ▼
                Natural Language Understanding
                         │
                         ▼
                    Planning Module
                         │
        ┌────────────────┼─────────────────┐
        ▼                ▼                 ▼
   Read File        Search Docs      Read Project
        │                │                 │
        └────────────────┼─────────────────┘
                         ▼
                  Context Building
                         │
                         ▼
              LLM Reasoning Engine
                         │
       ┌─────────────────┼──────────────────┐
       ▼                 ▼                  ▼
 Generate Code     Tool Calling      Decide Next Step
       │                 │                  │
       ▼                 ▼                  ▼
   Write Files     Terminal/Git/Test    Browser/IDE
       │                 │                  │
       └─────────────────┼──────────────────┘
                         ▼
                  Observe Results
                         │
                  Success?
                  │          │
                 Yes         No
                  │          ▼
                  │     Reflection
                  │          │
                  └──────────┘
AI Engineer Roadmap অনুযায়ী

Transformer / LLM → কীভাবে মডেল ভাষা ও কোড বোঝে।
Function Calling / Tool Use → কীভাবে LLM বাইরের টুল (ফাইল, টার্মিনাল, ব্রাউজার) ব্যবহার করে।
RAG (Retrieval-Augmented Generation) → কীভাবে ডকুমেন্ট বা কোডবেস থেকে তথ্য আনে।
Agent Planning → কীভাবে বড় Goal-কে ছোট ছোট Task-এ ভাগ করে।
Agent Memory → কীভাবে আগের কাজ মনে রাখে।
Reflection / Self-Correction → কীভাবে Build Error দেখে আবার ঠিক করে।