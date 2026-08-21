# chatbot.py — Interfaz conversacional

from classifier import classify_ticket
from ticket_manager import create_ticket, get_ticket

def show_welcome():
    print("=" * 45)
    print("   🤖 CHATBOT DE SOPORTE IT")
    print("=" * 45)
    print("Opciones:")
    print("  1. Reportar un problema")
    print("  2. Consultar estado de ticket")
    print("  3. Salir")
    print("=" * 45)

def report_problem():
    print("\n📝 NUEVO TICKET")
    user = input("Tu nombre: ").strip()
    description = input("Describe tu problema: ").strip()
    if not description:
        print("❌ La descripción no puede estar vacía.")
        return
    result = classify_ticket(description)
    ticket = create_ticket(
        user=user,
        description=description,
        category=result["category"],
        priority=result["priority"]
    )
    print("\n✅ Ticket creado exitosamente:")
    print(f"  ID:        {ticket['id']}")
    print(f"  Categoría: {ticket['category']}")
    print(f"  Prioridad: {ticket['priority']}")
    print(f"  Estado:    {ticket['status']}")

def check_ticket():
    print("\n🔍 CONSULTAR TICKET")
    ticket_id = input("Ingresa el ID del ticket: ").strip()
    ticket = get_ticket(ticket_id)
    if not ticket:
        print(f"❌ No se encontró el ticket: {ticket_id}")
        return
    print(f"\n📋 Ticket: {ticket['id']}")
    print(f"  Usuario:   {ticket['user']}")
    print(f"  Problema:  {ticket['description']}")
    print(f"  Categoría: {ticket['category']}")
    print(f"  Prioridad: {ticket['priority']}")
    print(f"  Estado:    {ticket['status']}")
    print(f"  Fecha:     {ticket['created_at']}")

def main():
    show_welcome()
    while True:
        option = input("\nElige una opción (1-3): ").strip()
        if option == "1":
            report_problem()
        elif option == "2":
            check_ticket()
        elif option == "3":
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    main()
