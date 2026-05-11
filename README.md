# Rule-Based Cognitive Architecture

This is my first independent Python project at a relatively large scale in 2019. It is a rule-based conversational and system automation project built for learning and experimentation. It was built without prior knowledge of LLMs.

## Overview

Cortex is a Python application that uses manual intent mapping, JSON knowledge files, and simple response selection to handle basic conversation and a set of system tasks.

## What It Does

- Handles greetings, self descriptions, help prompts, and simple fallback responses
- Supports system queries such as time, battery, and network status
- Can open selected applications and perform some local file and web actions
- Stores conversation and task information in local JSON files

## What It Does Not Do

- It does not learn automatically from conversation
- It does not use large language models
- It does not provide real-time web intelligence beyond the features already implemented
- It does not handle complex multi-turn reasoning

## Running It

```bash
bash setup_env.sh
python Cortex.py
```

## Project Layout

- Brain: knowledge and response data
- Core: main runtime logic
- Skills: action handlers
- SystemUtils: background utilities
- Security: encryption and decryption helpers

## Notes

This repository is kept as an early project archive. The code shows how the system was built at the time, with later cleanup focused on making the Python parts easier to run and understand.
