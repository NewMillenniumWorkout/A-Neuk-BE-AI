# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**ANeuk** is an AI-powered emotional awareness and diary generation service designed to prevent fake emotion addiction and expand emotional vocabulary. The service uses conversational AI to help users write diary entries, analyze emotions, and learn diverse emotional vocabulary through natural chat interactions.

### Core Functionality

This FastAPI backend provides three main AI services:

1. **Conversational Chat** (`/ai/chat/`): Natural dialogue to gather daily experiences and emotions
2. **Diary Generation** (`/ai/diary/`): Convert chat conversations into diary entries with emotion analysis
3. **Sentence Remaking** (`/ai/remake/`): Regenerate sentences incorporating selected emotion words naturally

## Development Commands

This project uses [uv](https://docs.astral.sh/uv/) as the package manager for fast, reliable dependency management.

### Initial Setup

```bash
# Install dependencies
uv sync

# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh  # macOS/Linux
# or
brew install uv  # macOS with Homebrew
```

### Running the Application

```bash
# Run with uvicorn
uv run uvicorn src.main:app --host 0.0.0.0 --port 8000

# Or run with auto-reload for development
uv run uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

### Managing Dependencies

```bash
# Add a new dependency
uv add package-name

# Add a development dependency
uv add --dev package-name

# Update all dependencies
uv sync

# Update a specific package
uv add package-name@latest
```

### Docker

```bash
# Build the Docker image
docker build -t aneuk-ai .

# Run the container
docker run -p 8000:8000 --env-file .env aneuk-ai
```

### Environment Setup

Copy `.env-example` to `.env` and configure the following:

```bash
# Swagger UI authentication
SWAGGER_USERNAME=
SWAGGER_PASSWORD=

# API Keys
OPENAI_API_KEY=        # For GPT models (gpt-4o, gpt-4o-mini, etc.)
GOOGLE_API_KEY=        # For Gemini models
DICTIONARY_API_KEY=    # For dictionary lookups

# LLM Configuration
# All model settings are in src/config/llm_config.yaml
# No environment variables needed for model selection!
```

## Architecture

### Project Structure

```
src/
├── ai_cores/           # Core AI processing logic
│   ├── chat_cores/     # Chat generation
│   ├── diary_cores/    # Diary generation, splitting, emotion finding
│   └── remake_cores/   # Sentence reconstruction with emotions
├── config/             # Centralized configuration
│   └── llm_config.py   # LLM model selection and factory functions
├── routes/             # FastAPI route handlers
├── models/             # Pydantic models for requests/responses
├── utils/              # Utilities (auth, emotion data)
└── static/             # Static files
```

### AI Processing Pipeline

The diary generation follows a multi-stage pipeline:

1. **Chat Phase** (`chat_cores/generate.py`):
   - Uses Gemini 2.5 Flash (or GPT-4o-mini) with temperature=0.7
   - Maintains conversation history with `HumanMessage` and `AIMessage`
   - System prompt guides natural Korean conversation about daily events
   - Avoids forced emotion discussions; redirects off-topic conversations

2. **Diary Generation** (`diary_cores/generate.py`):
   - Input: Complete chat history
   - Uses Gemini 2.5 Flash (or GPT-4o) with temperature=0.7
   - Generates diary from user's perspective (not assistant's)
   - Few-shot prompting with 3 Korean diary examples
   - Output: Single diary entry in informal Korean

3. **Paragraph Splitting** (`diary_cores/split.py`):
   - Input: Generated diary text
   - Uses GPT-4o-mini with temperature=0
   - Few-shot prompting with 3 splitting examples
   - Splits diary into topic-based paragraphs
   - JSON output parsing with `DairyStrList` model

4. **Emotion Analysis** (`diary_cores/find_emotions.py`):
   - **Two-tier system**: First finds emotion categories, then specific emotions
   - Uses 11 emotion categories: 기쁨, 흥미, 놀람, 중성, 슬픔, 지루, 공포, 분노, 통증, 혐오, 기타
   - Emotion database: 434 Korean emotion words in `emotions.txt` (tab-separated: category + word)
   - For each paragraph:
     - Finds top 3 emotion categories (most likely to least expected)
     - For each category, extracts 10 specific emotions (7 common, 3 uncommon)
     - Runs async/parallel processing for performance
   - Temperature variations: Uses 4 LLMs with temperatures 0, 0.25, 0.5, 0.75
   - Output: List of `DiaryContent` with recommended emotions per paragraph

5. **Sentence Remaking** (`remake_cores/remake_sentence.py`):
   - Input: Original sentence + selected emotion words
   - Uses Gemini 2.5 Flash (or GPT-4o-mini) with temperature=0.25
   - Respects original sentiment (positive/negative)
   - Maintains user's writing style and tone
   - Naturally incorporates emotion words without forcing

### YAML-Based LLM Configuration

All LLM models are managed through **`src/config/llm_config.yaml`**, a declarative configuration file that defines:
- Model names for each task
- Temperature settings
- Provider-specific parameters (max_tokens, thinking_mode, etc.)

**Configuration File Structure:**
```yaml
models:
  chat:
    temperature: 0.7
    model_name: "gemini-flash-lite-latest"

  diary:
    temperature: 0.7
    model_name: "gemini-flash-lite-latest"

  diary_split:
    temperature: 0.0
    model_name: "gpt-4o-mini"
    max_tokens: 4096

  emotion_finding:
    primary:
      temperature: 0.0
      model_name: "gpt-4o-mini"
    low:
      temperature: 0.25
      model_name: "gpt-4o-mini"
    # ... 4 temperature variants

  remake:
    temperature: 0.25
    model_name: "gemini-flash-lite-latest"
```

**Changing Models:**
Simply edit `src/config/llm_config.yaml`:
```yaml
# Switch chat to OpenAI GPT-4o
chat:
  temperature: 0.7
  model_name: "gpt-4o"  # Changed from gemini
  max_tokens: 4096      # Optional: add parameters
```

**Supported Models:**
- **OpenAI**: `gpt-4o`, `gpt-4o-mini`, `gpt-4-turbo`, `o3-mini`, `o4-mini`
- **Google Gemini**: `gemini-flash-lite-latest`, `gemini-2.5-flash`, `gemini-pro`
- **Extensible**: Easy to add Anthropic Claude or other providers

**Factory Functions:**
- `get_chat_llm()`: Chat conversation
- `get_diary_llm()`: Diary generation
- `get_diary_split_llm()`: Paragraph splitting
- `get_emotion_finding_llms()`: Returns list of 4 LLMs with varying temperatures
- `get_remake_llm()`: Sentence remaking
- `get_llm_models(cfg_section)`: Bulk creation from config section

**Benefits:**
- ✅ No code changes needed to switch models
- ✅ Version control friendly (YAML is readable and diffable)
- ✅ Environment-agnostic (dev/staging/prod can use different configs)
- ✅ Provider-specific parameters supported (thinking_mode, reasoning_effort, etc.)
- ✅ OmegaConf integration for powerful configuration management

### LangChain Integration

All AI operations use LangChain:
- `ChatOpenAI` / `ChatGoogleGenerativeAI` for model interfaces
- `StrOutputParser` for text outputs
- `JsonOutputParser` with Pydantic models for structured outputs
- Async operations with `ainvoke()` for all LLM calls
- Message history with `SystemMessage`, `HumanMessage`, `AIMessage`

### Key Design Decisions

1. **YAML-Based LLM Config**: All models defined in `llm_config.yaml` for declarative, version-controlled configuration
2. **OmegaConf Integration**: Powerful config management with type safety and validation
3. **Async Processing**: All AI operations use async/await for better performance
4. **Parallel Execution**: Emotion finding runs multiple LLM calls concurrently using `asyncio.gather()`
5. **Temperature Control**: Lower temperatures (0) for deterministic tasks (splitting), higher (0.7) for creative tasks (chat, diary)
6. **Few-Shot Learning**: Provides concrete examples in prompts for better output quality
7. **JSON Output Parsing**: Enforces structured outputs using Pydantic models
8. **Error Handling**: Custom `LLMError` exception for LLM failures
9. **Swagger Auth**: Protected Swagger UI using `get_protected_docs()` utility

### Emotion Data Format

The `emotions.txt` file contains 434 Korean emotion words:
- Format: `{category}\t{emotion_word}`
- Example: `기쁨\t감사하다`
- Loaded at startup in `find_emotions.py` into `emotion_dict`
- Categories are shuffled before LLM processing to avoid bias

## Route Handlers

All routes follow a consistent pattern:
- Accept Pydantic request models
- Call async AI core functions
- Return Pydantic response models
- Handle `LLMError` exceptions with HTTP 500

Example:
```python
@router.post("/", response_model=DiaryResponse)
async def diary_post(request: DiaryRequest):
    original = await diary_generate(request)
    splitted = await diary_split(original)
    emotions = await diary_find_emotions(splitted)
    return DiaryResponse(chat_id=request.chat_id, content_list=emotions)
```

## Common Patterns

### Adding New AI Features

1. Create new module in `ai_cores/`
2. Define Pydantic models in `models/`
3. Create system prompts with Korean language specifications
4. Use appropriate temperature settings
5. Implement async function with LangChain chains
6. Add route handler in `routes/`
7. Register router in `main.py`

### Prompt Engineering Guidelines

- Always specify Korean language requirements explicitly
- Include exclusion criteria (what NOT to do)
- Provide 2-3 concrete examples (few-shot)
- Use temperature=0 for deterministic outputs
- Use temperature=0.7 for creative/conversational outputs
- Format JSON outputs with Pydantic schema instructions

### Message History Management

When working with chat history:
```python
messages = [SystemMessage(content=system_prompt)]
for m in request.messages:
    if m.role == "MEMBER":
        messages.append(HumanMessage(content=m.message))
    elif m.role == "ASSISTANT":
        messages.append(AIMessage(content=m.message))
```

## Testing & Debugging

- The `/ai/diary/` route includes `measure_time()` function for performance profiling
- Debug output in `diary.py` shows original, splitted, and emotion-tagged content
- Print statements in `remake_sentence.py` log input/output for verification

## Notes

- **Package Manager**: This project uses `uv` for dependency management. Always use `uv run` to execute commands.
- **No PYTHONPATH needed**: `uv run` automatically handles Python paths, so no need to set `PYTHONPATH=src`
- **YAML-Based Config**: All LLM models configured in `src/config/llm_config.yaml` - edit this file to change models
- **No Environment Variables for Models**: Model selection is purely YAML-based, no `LLM_PROVIDER` or similar env vars needed
- **Korean Language**: All prompts enforce Korean output with informal speech (반말)
- **Async Operations**: Never use blocking calls; always use async/await
- **Emotion Database**: The 434 emotion words are a core part of the research-based approach
- **Dependency Updates**: Use `uv add package@latest` to update packages; `uv.lock` is committed to ensure reproducible builds
