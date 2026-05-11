# Rule-Based Cognitive Architecture (2019 Early Version)

An archived early learning project demonstrating system-level and algorithmic thinking prior to the widespread availability of modern generative LLMs.

## Overview

Developed throughout 2019, this is a from-scratch, rule-based natural language understanding (NLU) pipeline written in Python. Rather than using black-box models, this project attempts to process language deterministically by mapping logic to a biologically inspired directory structure.

This was my first independent Python project at a relatively large scale, built as a learning exercise.

## The Architecture

* Frontal Lobe (/Brain/FrontalLobe/): Handles executive function, cross-referencing input against manual JSON dictionaries to map intent and assign confidence scores.
* Broca's Area (/Core/BrocaArea.py): Orchestrates speech production and system output.
* Limbic System (/Brain/Limbic/): Manages chronological logging and system memory states.

## Evolution & Context

While the NLP logic is rudimentary by today's standards, building this manual intent-mapping system required deep algorithmic orchestration and state management. The foundational logic required to manually wire this cognitive architecture served as the direct stepping stone for current work in custom physics staging algorithms, C++ node-based APIs, and 3D machine learning.

---

## Quick Start

### Prerequisites

- Python 3.8+
- pip
- Git

### Installation (One-Click Setup)

```bash
git clone https://github.com/yourusername/Rule-Based-Cognitive-Architecture.git
cd Rule-Based-Cognitive-Architecture
bash setup_env.sh
```

This will:
1. Create a Python virtual environment (.venv/)
2. Install all dependencies
3. Validate the installation

### Running Cortex

```bash
python Cortex.py
```


```
System initialization: Configuration check returned no result. Proceeding with default settings.
System ready. Cortex is prepared to assist you.

CORTEX>_
```

---

## Example Conversation

```
CORTEX> hello
Hello! I'm Cortex, your AI assistant. How can I help?

CORTEX> who created you
I was created by Rishabh Gupta as part of the Rule-Based Cognitive Architecture project.

CORTEX> what time is it
The current time is 14:30:45.

CORTEX> open chrome
Opening Chrome for you. Just a moment.

CORTEX> goodbye
Goodbye! It was nice talking to you. See you next time!
```

For more examples and question types Cortex can handle, see CONVERSATION_GUIDE.md.

---

## Features & Capabilities

### STRENGTHS - What Cortex Can Do Well

- System Information: Time, battery status, network connectivity
- Application Control: Launch apps (cross-platform: Windows/Linux/Mac)
- File Operations: Backup files, list directories
- Web Search: Redirect to Google/Wikipedia searches
- Task Logging: Remember and retrieve logged tasks
- Self-Description: Information about itself, creator, creation date

### LIMITATIONS

- No Learning: Cannot adapt to user preferences or learn new patterns at runtime
- No Real-Time Data: No API integrations for weather, news, or web content
- No Context Memory: Each query is independent; no multi-turn conversation state
- Pattern-Based Only: Requires explicit sentence patterns in understand.json to recognize queries
- No Spell Correction: Typos often cause "I don't know" responses

See CONVERSATION_GUIDE.md for a detailed capabilities matrix.

---

## Project Structure

```
Rule-Based-Cognitive-Architecture/
Brain/                      Knowledge base and learning
  FrontalLobe/             Intent mapping and understand patterns
  Limbic/                  Conversation history and logging
  Response/                Response templates (response.json)
Core/                       Main modules
  CortexModule.py          Main interaction loop
  BrocaArea.py             Language processing
  Configure.py             System configuration
  Response.py              Response generation
Skills/                     Action handlers
  Action.py                App launching, web search, etc.
CodeReac/                  Command execution
  __init__.py              ResponseRefiner() handler
Security/                  Encryption and decryption
SystemUtils/               Background tasks and logging
Cortex.py                 Entry point
setup_env.sh              One-click installer
requirements.txt          Dependencies
CONVERSATION_GUIDE.md     Detailed conversation reference
LICENSE                   MIT License
README.md                 This file
```

---

## Technical Details

### Intent Recognition Pipeline

1. Input Processing: User input converted to lowercase
2. Sentence Classification: Matched against patterns in understand.json
3. Confidence Scoring: Intent assigned with high/medium/low confidence
4. Response Selection: Response retrieved from response.json based on confidence
5. Command Execution: If action needed, execute via CodeReac.ResponseRefiner()
6. Logging: Store in Brain/Limbic/JResponse/jresponse.json

### Key Files

- Brain/Response/response.json - Maps intent codes to conversational responses
- Brain/Response/response_library.json - Full response templates for all categories
- Brain/FrontalLobe/understand/understand.json - Sentence patterns to intent codes
- Brain/FrontalLobe/understand/learning_code.json - Intent code ordering
- Brain/Limbic/JResponse/jresponse.json - Conversation history

---

## Cross-Platform Support

Cortex runs on Windows, Linux, and macOS:

- Application launching uses platform-specific commands
- File paths use OS-agnostic methods
- Screen clearing adapted per platform
- Tested on Python 3.8, 3.10, 3.12

---

## Extending Cortex

### Add a New Conversation Pattern

1. Edit Brain/FrontalLobe/understand/understand.json
   - Add sentence pattern and intent code

2. Edit Brain/Response/response.json
   - Add responses for that intent code

3. Optional: Add Handler in CodeReac/__init__.py
   - If action needs to execute (launch app, etc.)

See CONVERSATION_GUIDE.md for step-by-step instructions.

---

## Known Issues

- Linux/Mac: Some legacy code paths still reference Windows-only commands (being migrated)
- API Limitations: Web requests may fail without proper network setup
- Parse Library: Minor compatibility issue with requests-html on Python 3.12+ (workaround included)

---

## License

MIT License - See LICENSE file for details.

## Author

Rishabh Gupta (2019)

This project was created as an educational exercise in natural language processing, system architecture, and algorithmic design before the widespread adoption of transformer-based LLMs.
