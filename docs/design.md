# Design — IT Support Chatbot

## Componentes
- chatbot.py        → Interfaz de conversación
- classifier.py     → Motor de clasificación
- ticket_manager.py → Gestión y almacenamiento
- storage.json      → Base de datos local

## Flujo principal
Usuario → chatbot.py → classifier.py → ticket_manager.py → storage.json

## Arquitectura
- Capa de presentación: chatbot.py
- Capa de lógica: classifier.py
- Capa de datos: ticket_manager.py + storage.json
