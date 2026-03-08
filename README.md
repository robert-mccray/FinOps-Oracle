# 💰 FinOps Oracle (AI-Powered IaC Review)

An automated CI/CD gatekeeper that intercepts Terraform Pull Requests, calculates the financial impact using `Infracost`, and leverages a local LLM to recommend cheaper, mathematically optimized cloud instances before code is merged.

## 🚀 How to Run Locally

### Prerequisites
1. **Ollama:** Install and run [Ollama](https://ollama.com/) locally. Pull the model: `ollama run llama3`.
2. **Infracost:** Install the [Infracost CLI](https://www.infracost.io/docs/) and authenticate: `infracost auth login`.
3. **Python:** Ensure Python 3.10+ is installed.

### Execution Steps
1. Clone this repository and navigate to the root directory.
2. Install the required Python libraries:
   ```bash
   pip install requests
   ```
3. Generate the cost breakdown from the intentionally expensive example-terraform directory:

```Bash
infracost breakdown --path example-terraform --format json --out-file cost.json
Run the FinOps Oracle to analyze the cost and generate savings recommendations:
```
```Bash
python scripts/finops_oracle.py
```
---
