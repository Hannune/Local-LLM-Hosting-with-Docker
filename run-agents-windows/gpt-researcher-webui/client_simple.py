import requests

API_URL = "http://<ip>:<port>/report/"  # trailing slash to avoid 307

def create_report(task: str):
    payload = {
        "task": task,
        "report_type": "research_report",
        "report_source": "web",
        "tone": "Objective",     # must match enum capitalization
        "headers": {},
        "repo_name": "",
        "branch_name": "",
        "generate_in_background": False,
    }
    r = requests.post(API_URL, json=payload, timeout=600)
    r.raise_for_status()
    data = r.json()
    print(data.get("report") or data)

if __name__ == "__main__":
    create_report("what team may win the NBA finals?")
