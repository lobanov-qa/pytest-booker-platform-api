import json
import os
from pathlib import Path

SERVICES = {
    "auth": {
        "file": "auth.json",
        "port": 3004,
        "name": "Auth Service",
        "description": "Authentication & Authorization",
        "icon": "key"
    },
    "booking": {
        "file": "booking.json",
        "port": 3000,
        "name": "Booking Service",
        "description": "Booking Management",
        "icon": "calendar"
    },
    "room": {
        "file": "room.json",
        "port": 3001,
        "name": "Room Service",
        "description": "Room Management",
        "icon": "home"
    },
    "message": {
        "file": "message.json",
        "port": 3006,
        "name": "Message Service",
        "description": "Message Management",
        "icon": "message-square"
    },
    "branding": {
        "file": "branding.json",
        "port": 3002,
        "name": "Branding Service",
        "description": "Branding & Settings",
        "icon": "palette"
    },
    "report": {
        "file": "report.json",
        "port": 3005,
        "name": "Report Service",
        "description": "Reporting & Analytics",
        "icon": "bar-chart"
    }
}


def generate_apis_json():
    apis = []
    for service_id, config in SERVICES.items():
        apis.append({
            "type": "file",
            "input": f"./apis/{config['file']}",
            "path": f"/api/{service_id}",
            "name": config["name"],
            "description": f"{config['description']} - Port {config['port']}",
            "options": {
                "examplesLanguage": "shell",
                "expandAllTags": False,
                "schemaDownload": {"enabled": True}
            }
        })

    with open(Path("apis") / "_apis.json", "w") as f:
        json.dump(apis, f, indent=2)
    print("✅ Generated apis/_apis.json")


def generate_navigation_json():
    navigation = [{
        "type": "category",
        "label": "Microservices",
        "description": "Independent services running on different ports",
        "collapsible": False,
        "icon": "server",
        "items": []
    }]

    for service_id, config in SERVICES.items():
        navigation[0]["items"].append({
            "type": "link",
            "label": config["name"],
            "description": f"Port {config['port']} - {config['description']}",
            "to": f"/api/{service_id}",
            "icon": config["icon"]
        })

    with open(Path("apis") / "_navigation.json", "w") as f:
        json.dump(navigation, f, indent=2)
    print("✅ Generated apis/_navigation.json")


if __name__ == "__main__":
    os.makedirs("apis", exist_ok=True)
    generate_apis_json()
    generate_navigation_json()
    print("Configuration generated successfully!")
    print("Next steps:")
    print("1. Update zudoku.config.ts to use the generated files")
    print("2. Create pages/overview.mdx for documentation")
    print("3. Run: npx zudoku dev")