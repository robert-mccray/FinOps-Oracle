import json
import urllib.request
import subprocess

def run_infracost():
    # in a real run, this executes 'infracost breakdwon --path . --format json'
    # For local testing, we mock the expensive JSON output
    return {
        "totalMonthlyCost": "850.0",
        "projects": [{"name": "example-terraform", "metadata": {"instance_type": "Standard_D8s_v3"}}]
    }

def optimize_cost(cost_data):
    print(" Analyzing Terraform costs with Llama-3...")
    prompt = f"""
    You are a Principal Cloud FinOps Architect. Analyze this Infracost JSON.
    The current monthly cost is ${cost_data['totalMonthlyCost']}. The instance type is {cost_data['projects'][0]['metadata']['instance_type']}. 
    Suggest a modern, cheaper burstable instance type (like B-series) for a Dev environment, and calculate the estimated savings.
    """

    data = {"model": "llama3", "prompt": prompt, "stream": False}
    req = urllib.request.Request("http://localhost:11434/api/generate", data=json.dumps(data).encode("utf-8"))

    with urllib.request.urlopen(req) as response:
        print("\n================== FINOPS ORCALE REVIEW===============")
        print(json.loads(response.read().decode("utf-8"))["response"])
        print("======================================")

if __name__ == "__main__":
    optimize_cost(run_infracost())        