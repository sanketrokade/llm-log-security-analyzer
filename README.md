# LLM Log & Security Analyzer

## 📌 Overview

**LLM Log & Security Analyzer** is a modular, CLI-based prototype that uses a Large Language Model (LLM) to analyze system and security logs. It summarizes incidents, assesses severity, explains possible causes, and recommends remediation actions.

The project is designed as an **internal Proof-of-Concept (PoC)** suitable for security teams, SOC environments, and system administrators. It emphasizes **engineering discipline, modularity, and graceful failure handling**, rather than AI hype.

---

## 🎯 Key Objectives

* Reduce time spent manually analyzing verbose system and security logs
* Demonstrate practical usage of LLMs in cybersecurity workflows
* Provide structured, machine-readable outputs for downstream tools
* Ensure robustness when LLM services are unavailable

---

## 🧠 What This Project Is (and Is Not)

### ✅ This Project Is

* An **LLM-assisted log analysis tool**
* Focused on **integration and implementation**, not model training
* Designed with **production-style architecture**
* Compatible with **Windows (no admin access required)**

### ❌ This Project Is Not

* A custom-trained AI/ML model
* A replacement for SIEM or IDS systems
* A GPU- or CUDA-dependent application

---

## 🏗️ Architecture

```
Log File (.log)
      │
      ▼
Log Parser (filter + chunk)
      │
      ▼
Prompt Template (external file)
      │
      ▼
LLM Client (API / Fallback)
      │
      ▼
Structured Output (JSON)
```

### Design Highlights

* **Separation of concerns** (parser, prompt, LLM client)
* **Prompt stored outside code** for easy tuning
* **Graceful fallback** when LLM quota/API is unavailable
* **CLI-first design** for easy automation

---

## 📂 Project Structure

```
llm-log-security-analyzer/
│
├── logs/
│   └── sample.log
│
├── prompts/
│   └── log_analysis_prompt.txt
│
├── src/
│   ├── analyzer.py        # Main entry point
│   ├── llm_client.py      # LLM API + fallback handling
│   ├── log_parser.py      # Log reading, filtering, chunking
│   └── utils.py           # (reserved for future use)
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Requirements

* Python **3.9+** (tested on Python 3.14, Windows)
* Git
* Internet access (optional, for LLM API)

### Python Dependencies

```
openai
```

Install (user-space, no admin required):

```
python -m pip install --user -r requirements.txt
```

---

## 🔐 Environment Setup

### API Key (Optional but Recommended)

The tool uses an OpenAI-compatible API for LLM analysis.

Set the API key as a **user-level environment variable**:

**PowerShell (session-level):**

```
$env:OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxx"
```

> ⚠️ Never hardcode API keys or commit them to GitHub.

If no valid quota is available, the system **automatically falls back** to offline analysis.

---

## ▶️ Usage

Run the analyzer from the repository root:

```
python src/analyzer.py logs/sample.log
```

### Example Output (JSON)

```json
{
  "summary": "Multiple authentication failures detected",
  "severity": "Medium",
  "explanation": "Likely brute-force SSH attempt on privileged account",
  "recommended_action": "Block source IP, enforce SSH hardening, review authentication logs"
}
```

---

## 🧪 How It Works (Step-by-Step)

1. **Log Parsing**

   * Reads raw log files
   * Filters important entries (errors, failed auth, alerts)
   * Chunks logs to fit LLM context limits

2. **Prompt Injection**

   * Uses an external prompt template
   * Ensures consistent and controlled LLM behavior

3. **LLM Analysis**

   * Sends structured prompt to LLM
   * Requests strictly JSON output

4. **Graceful Fallback**

   * If API quota is exceeded or unavailable
   * Returns predefined structured analysis instead of crashing

---

## 🛡️ Error Handling & Reliability

* Authentication errors are clearly surfaced
* Rate-limit / quota issues trigger **offline fallback mode**
* Tool never crashes due to external LLM dependency

This behavior reflects **real-world production design**.

---

## 🔍 Example Use Cases

* SOC alert triage
* SSH brute-force detection explanation
* Log summarization for daily security reports
* Training junior admins on incident interpretation

---

## 🚀 Future Enhancements

Planned / Possible extensions:

* Numeric severity or risk scoring
* Batch processing of multiple log files
* Daily SOC summary report generation
* Local LLM inference (LLaMA / Ollama)
* Integration with SIEM pipelines
* Performance scaling and HPC-based log processing

---

## 📜 License

This project is intended as an internal prototype / educational PoC. Licensing can be added as needed.

---

## 👤 Author

**Sanket Rokade**
(Internal prototype for AI + Cyber Security exploration)

---

## ✅ Status

✔ Core pipeline implemented
✔ LLM integration complete
✔ Offline fallback supported
✔ Windows & no-admin compatible
