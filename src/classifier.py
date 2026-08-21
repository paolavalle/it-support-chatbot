# classifier.py — Clasificación automática de tickets

KEYWORDS = {
    "Hardware": ["impresora", "pantalla", "teclado", "mouse",
                 "computadora", "pc", "monitor", "disco"],
    "Software": ["programa", "error", "instalacion", "actualizar",
                 "aplicacion", "sistema", "windows", "office"],
    "Red": ["internet", "red", "wifi", "conexion", "lento",
            "navegador", "correo", "vpn"],
    "Acceso": ["contraseña", "password", "usuario", "login",
               "acceso", "cuenta", "bloqueo"]
}

PRIORITY = {
    "Hardware": "Alta",
    "Software": "Media",
    "Red": "Alta",
    "Acceso": "Media"
}

def classify_ticket(description: str) -> dict:
    description_lower = description.lower()
    for category, keywords in KEYWORDS.items():
        for keyword in keywords:
            if keyword in description_lower:
                return {"category": category, "priority": PRIORITY[category]}
    return {"category": "General", "priority": "Baja"}
