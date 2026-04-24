This repository, FinOps-Oracle, is the exact embodiment of your "Shift-Left FinOps" philosophy.

When the interview panel asks, "How do you balance innovation with budget constraints?" this repo proves you don't just ask engineers to "spend less." You build automated guardrails that make cost-efficiency the default state.

Here is the playbook for Repo #5:

Upload the FinOps/CI-CD architecture diagram from your portfolio into this repository's root folder and name it architecture-diagram.png.

Replace the current README.md with the executive code block below.

📋 Copy-Paste This for FinOps-Oracle README.md
Markdown
# 💰 FinOps Oracle: AI-Powered IaC Cost Guardrail

Cloud waste happens at the pull request, not the invoice. If you are waiting for the monthly AWS or Azure bill to see what you spent, the budget is already blown.

**FinOps Oracle** is an automated CI/CD gatekeeper that intercepts Infrastructure-as-Code (Terraform) Pull Requests, calculates the exact financial impact using Infracost, and leverages a local, air-gapped LLM to recommend mathematically optimized, cheaper cloud instances *before* the code is ever merged.

![FinOps Oracle Architecture Diagram](./architecture-diagram.png)

### 📈 Business Impact & Enterprise ROI
* **Proactive Cost Prevention (Shift-Left FinOps):** Treats cloud cost as a system architecture metric rather than an accounting problem. It stops budget overruns before the compute is ever provisioned.
* **Developer-Friendly Governance:** It doesn't just block PRs and frustrate engineers; it acts as an automated "Cloud Economist," providing engineers with actionable, cheaper instance alternatives directly in the PR comments.
* **Air-Gapped Privacy:** Utilizes local LLM inferencing (Llama-3). Proprietary infrastructure topologies and internal naming conventions are never transmitted to public cloud LLM providers.

### 🏗️ System Architecture Flow

1. **The Intercept:** The CI/CD pipeline triggers immediately upon a Terraform (`.tf`) modification.
2. **The Deterministic Calculation:** The Infracost engine parses the Terraform plan and generates a deterministic, line-item JSON breakdown of the proposed infrastructure's monthly cost against live cloud market rates.
3. **The AI Economist Analysis:** The JSON cost matrix is fed into the air-gapped LLM, which evaluates the resource allocation and searches for architectural arbitrage opportunities (e.g., suggesting a burstable instance type over a general-purpose one based on the resource tags).
4. **The Actionable Verdict:** Cost-saving recommendations are posted back to the developer for immediate remediation.

### 🚀 Quick Start (Local Execution)

**Prerequisites**
1. **Ollama:** Install and run locally. Pull the model: `ollama run llama3`.
2. **Infracost:** Install the CLI and authenticate: `infracost auth login`.
3. **Python:** Ensure Python 3.10+ is installed.

**Execution Steps**
1. Install the required libraries:
```bash
pip install requests
```
2. Generate the deterministic cost breakdown from the intentionally expensive example-terraform directory:

```bash
infracost breakdown --path example-terraform --format json --out-file cost.json
```

3. Run the FinOps Oracle to analyze the cost matrix and generate savings recommendations:

```bash
python scripts/finops_oracle.py
```

