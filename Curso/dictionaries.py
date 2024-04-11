monthConversions = {
    "jan": "Janeiro",
    "fev": "Fevereiro",
    "mar": "marco",
    1 : "AAAA"
}

print(monthConversions["mar"])
print(monthConversions.get("jan"))
print(monthConversions.get("jansa", "Not a valid jey"))
