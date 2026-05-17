# 🚀 AI Engineering learning roadmap

Welcome to the **AI Engineering Journey**! This repository documents a structured, hands-on roadmap to mastering production-grade AI systems, LLM integrations, and modern AI engineering workflows. 

Designed for transitioning from basic prompt wrappers to reliable, production-ready agentic systems, this log covers the entire developer workflow: from raw API prompting and structured data validation to tool execution/function calling.

---

## 🛠️ The 2026 AI Engineering Stack

This project leverages modern Python toolchains and APIs tailored for high-performance AI workflows:

*   **Runtime:** Python `3.13+`
*   **Package Management:** [uv](https://github.com/astral-sh/uv) (ultra-fast Python package installer and resolver)
*   **AI Engine:** [Google GenAI SDK](https://github.com/google/generative-ai-python) (`google-genai>=2.3.0`)
*   **Data Validation:** [Pydantic V2](https://docs.pydantic.dev/latest/) (`pydantic>=2`)
*   **Environment Management:** [python-dotenv](https://github.com/theofidry/django-dotenv-filenames) (`python-dotenv>=1.2.2`)

---

## 📅 Day-by-Day Learning Log

### 🌟 Day 1: LLM Basics & Advanced Gemini Prompting
*   **File:** [`1-basics_llm.py`](file:///Users/sameer/Desktop/dumps/ai-engineering/1-basics_llm.py)
*   **Focus:** Initializing and configuring the new Google GenAI SDK.
*   **Key Concepts Covered:**
    *   Initializing the modern client using `genai.Client(api_key=...)`.
    *   Making inference requests using the fast and cost-effective `gemini-flash-lite-latest` model.
    *   Leveraging **Gemini Thinking Mode** by configuring `ThinkingConfig(thinking_level="high")` to let the model generate complex chain-of-thought reasonings.
*   **Generated Insights:**
    *   [`response_preview.md`](file:///Users/sameer/Desktop/dumps/ai-engineering/response_preview.md): A detailed, 2026-focused strategic guide on landing an AI Engineering internship. It covers:
        *   **The 2026 Skill Stack:** Moving beyond prompt engineering to Agentic Frameworks (LangGraph, CrewAI), advanced RAG pipelines, LLMOps (LangSmith, Weights & Biases), and Inference Optimization (vLLM, GGUF).
        *   **Portfolio Building:** Moving away from boilerplate "PDF Chatbots" to vertical niche applications and rigorous evaluation frameworks.
        *   **Outreach & Placement Strategy:** Leveraging Wellfound, Y-Combinator start-ups, and value-add cold outreach to Engineering Leads rather than generic HR.

---

### 🛡️ Day 2: Advanced Data Validation with Pydantic
*   **File:** [`2-pydantic.py`](file:///Users/sameer/Desktop/dumps/ai-engineering/2-pydantic.py)
*   **Focus:** Bridging the gap between raw LLM outputs and typed Python models for bulletproof runtime reliability.
*   **Key Concepts Covered:**
    *   **Nested Model Architectures:** Building structured definitions where a model references another (e.g., `Author` inside `Book`).
    *   **Field Constraints:** Enhancing type safety using Pydantic's `Field` validation constraints (e.g., `page_count: int = Field(ge=0)` to forbid negative pages).
    *   **Strict Inputs Enforce:** Configuring `model_config = ConfigDict(extra='forbid')` to reject any unexpected or untyped fields in API payloads.
    *   **Custom Field Validators:** Writing powerful validation logic with the `@field_validator` and `@classmethod` decorators (e.g., rejecting titles containing `"blaah"` or usernames with spaces).
    *   **JSON Serialization & Parsing:** 
        *   Converting models safely to JSON strings via `.model_dump_json(indent=2)`.
        *   Validating raw JSON inputs using `model_validate_json(...)` with graceful `ValidationError` handling.
    *   **Automatic JSON Schemas:** Instantly exporting data models into valid JSON Schemas using `model_json_schema()` to facilitate structured LLM generation.

---

### 🔌 Day 3: LLM Function Calling & Pydantic V2 Integration
*   **File:** [`3-llm_func_calling.py`](file:///Users/sameer/Desktop/dumps/ai-engineering/3-llm_func_calling.py)
*   **Focus:** Empowering LLMs to perform external actions and connect with databases or APIs dynamically.
*   **Roadmap:**
    *   Mapping Python functions directly to Gemini tools.
    *   Leveraging Pydantic schemas as custom input structures for tool calls.
    *   Handling the Model's tool requests, executing the logic locally, and returning the outputs to close the reasoning loop.

---

## 🚀 Setting Up the Project Locally

### 1. Prerequisites
Ensure you have Python `3.13+` and `uv` installed. If you don't have `uv`, install it via:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Install Dependencies
Run the following command to create a virtual environment and sync the exact required dependencies:
```bash
uv sync
```

### 3. Environment Configuration
Create a `.env` file in the root directory:
```bash
touch .env
```
Populate it with your Gemini API credentials:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Running the Examples
To run the scripts, activate the virtual environment or run them directly via `uv run`:

*   **Day 1 (Basics & Inference):**
    ```bash
    uv run 1-basics_llm.py
    ```
*   **Day 2 (Pydantic Validation):**
    ```bash
    uv run 2-pydantic.py
    ```

---

## 📈 Key Takeaways from the Journey
1.  **AI Engineering is about Reliability:** It's not enough to get "good looking" text from an LLM. Production-grade systems require strict data validation (using Pydantic) to ensure the system doesn't break when downstream APIs ingest JSON outputs.
2.  **Let the Model Think:** Complex reasoning tasks significantly benefit from **Thinking Mode** (Gemini's Chain-of-Thought reasoning), improving performance on edge-cases, design problems, and code generation.
3.  **Tool Integration is the Future:** Agentic AI relies heavily on function calling to read and write state. The foundation laid in Days 1 & 2 directly supports the building of resilient, tool-using agents.
