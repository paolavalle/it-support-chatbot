import unittest
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from classifier import classify_ticket
from ticket_manager import create_ticket, get_ticket, load_tickets

TEST_STORAGE = "storage.json"

class TestIntegration(unittest.TestCase):

    def setUp(self):
        if os.path.exists(TEST_STORAGE):
            os.remove(TEST_STORAGE)

    def test_create_and_retrieve_ticket(self):
        description = "No tengo internet"
        classification = classify_ticket(description)
        ticket = create_ticket(
            user="Pame",
            description=description,
            category=classification["category"],
            priority=classification["priority"]
        )
        self.assertIsNotNone(ticket["id"])
        self.assertEqual(ticket["category"], "Red")
        self.assertEqual(ticket["status"], "Abierto")
        found = get_ticket(ticket["id"])
        self.assertEqual(found["id"], ticket["id"])
        self.assertEqual(found["user"], "Pame")

    def test_multiple_tickets(self):
        create_ticket("User1", "impresora rota", "Hardware", "Alta")
        create_ticket("User2", "error en office", "Software", "Media")
        tickets = load_tickets()
        self.assertEqual(len(tickets), 2)

    def tearDown(self):
        if os.path.exists(TEST_STORAGE):
            os.remove(TEST_STORAGE)

if __name__ == "__main__":
    unittest.main()
