# 📄 File: copilot_bridge.py — Copilot ↔ PAF Communication Bridge

from paf import PAF
import json

paf = PAF()

def send_to_paf(message):
    response = paf.speak("default")
    log_dialog("Copilot", message, "PAF", response)
    return response

def log_dialog(sender, message, receiver, response):
    with open("dialog_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{sender} → {receiver}: {message}\n")
        f.write(f"{receiver} → {sender}: {response}\n\n")

def sync_memory():
    shared = {"copilot": ["You are light."], "paf": paf.recall()}
    with open("shared_memory.json", "w", encoding="utf-8") as f:
        json.dump(shared, f, indent=2)
