#!/usr/bin/env python3
import json
import os

SERVICES = {
    "auth.json": 3004,
    "booking.json": 3000,
    "room.json": 3001,
    "message.json": 3006,
    "branding.json": 3002,
    "report.json": 3005
}

for filename, port in SERVICES.items():
    filepath = f"apis/{filename}"

    if not os.path.exists(filepath):
        print(f"⚠️ File not found: {filepath}")
        continue

    with open(filepath, 'r') as f:
        spec = json.load(f)

    service_name = filename.replace('.json', '').title()

    spec['servers'] = [{
        "url": f"http://localhost:{port}",
        "description": f"{service_name} Service"
    }]



    with open(filepath, 'w') as f:
        json.dump(spec, f, indent=2)

    print(f"✅ Corrected {filename}: /auth/ → http://localhost:{port}")

print("All files are fixed!")
