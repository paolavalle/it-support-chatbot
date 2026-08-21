# ticket_manager.py — Gestión de tickets

import json
import os
from datetime import datetime

STORAGE_FILE = "storage.json"

def load_tickets() -> list:
    if not os.path.exists(STORAGE_FILE):
        return []
    with open(STORAGE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tickets(tickets: list):
    with open(STORAGE_FILE, "w", encoding="utf-8") as f:
        json.dump(tickets, f, ensure_ascii=False, indent=2)

def create_ticket(user: str, description: str,
                  category: str, priority: str) -> dict:
    tickets = load_tickets()
    now = datetime.now()
    ticket_id = f"TKT-{now.strftime('%Y%m%d')}-{len(tickets)+1:03d}"
    ticket = {
        "id": ticket_id,
        "user": user,
        "description": description,
        "category": category,
        "priority": priority,
        "status": "Abierto",
        "created_at": now.strftime("%Y-%m-%d %H:%M:%S")
    }
    tickets.append(ticket)
    save_tickets(tickets)
    return ticket

def get_ticket(ticket_id: str) -> dict:
    tickets = load_tickets()
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket
    return None
