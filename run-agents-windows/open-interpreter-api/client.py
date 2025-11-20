# client.py
import requests
import json

BASE_URL = ""

def send_chat_complete(message):
    """
    Sends a message and waits for the complete response.
    """
    print(f"Sending (complete) message: {message!r}")
    resp = requests.get(f"{BASE_URL}/chat", params={"message": message})
    resp.raise_for_status()
    data = resp.json()
    print("\n--- Complete Response ---")
    print(f"Message: {data['message']}")
    print(f"Status: {data['status']}")
    print(f"Response:\n{data['response']}")
    print("-------------------------\n")

def send_chat_stream(message):
    """
    Sends a message and streams the response.
    """
    print(f"Sending (stream) message: {message!r}")
    with requests.get(f"{BASE_URL}/chat_stream", params={"message": message}, stream=True) as resp:
        resp.raise_for_status()
        for line in resp.iter_lines():
            if line:
                decoded = line.decode('utf-8')
                if decoded.startswith("data: "):
                    print(decoded[len("data: "):], end="", flush=True)
    print("\n--- Stream Ended ---\n")

def get_history():
    """
    Fetches the chat history.
    """
    print("Requesting chat history...")
    resp = requests.get(f"{BASE_URL}/history")
    resp.raise_for_status()
    history = resp.json()
    print("\n--- Chat History ---")
    print(json.dumps(history, indent=2))
    print("--------------------\n")

if __name__ == "__main__":
    # Example usage:
    send_chat_complete("python code to print fancy hello!")
    # send_chat_stream("python code to print hello!")
    print()
    get_history()


