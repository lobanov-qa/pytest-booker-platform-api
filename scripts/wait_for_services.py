"""
Wait until all microservices are healthy.
Used in CI to wait for services to be ready before running tests.
"""

import sys
import time
import httpx


SERVICES = [
    {"name": "auth", "port": 3004},
    {"name": "booking", "port": 3000},
    {"name": "branding", "port": 3002},
    {"name": "message", "port": 3006},
    {"name": "report", "port": 3005},
    {"name": "room", "port": 3001},
]
"""List of microservices with their names and ports for health checks.

Each service is checked via URL: http://localhost:port/name/actuator/health.
Used by wait_for_services to verify availability.
"""


TIMEOUT_PER_SERVICE = 15.0
"""Timeout in seconds for a single request to /actuator/health.

If the service does not respond within this time, the request is considered failed.
"""


TOTAL_TIMEOUT = 120
"""Total timeout in seconds for waiting all services to become healthy.

If not all services are ready within this time, the script exits with code 1.
"""


INTERVAL = 3
"""Interval in seconds between full check cycles of remaining services.

The script waits this amount before retrying if not all services are ready.
"""


def check_service(name: str, port: int) -> bool:
    """Check the health status of a single microservice.

    Sends a GET request to the /actuator/health endpoint and validates:
      - HTTP status code is 200
      - Response is valid JSON
      - "status" field equals "UP"

    Prints informative messages about the current state.

    Args:
        name (str): Service name (used in URL and logs)
        port (int): Port where the service is running

    Returns:
        bool: True if service is healthy (200 + {"status": "UP"}), False otherwise.
    """
    url = f"http://localhost:{port}/{name}/actuator/health"
    print(f"🔍 Checking {name} at {url}...")
    try:
        response = httpx.get(url, timeout=TIMEOUT_PER_SERVICE)
        if response.status_code == 200:
            try:
                data = response.json()
                if data.get("status") == "UP":
                    print(f"✅ {name} (port {port}) is UP")
                    return True
                else:
                    print(f"🟡 {name} returned status: {data.get('status')}")
            except httpx.ResponseNotJSON:
                print(f"❌ {name}: response is not JSON — {response.text}")
        else:
            print(f"❌ {name}: status {response.status_code} — {response.text}")
    except (httpx.ConnectError, httpx.TimeoutException, httpx.ReadError) as e:
        print(f"⏳ {name} error (connect/timeout/read): {e}")
    return False


def wait_for_services():
    """Main function that waits for all microservices to become healthy.

    In a loop, checks each service from the SERVICES list using check_service.
    Healthy services are removed from the remaining list.
    Continues until all services are healthy or TOTAL_TIMEOUT is reached.

    On timeout, prints the list of unready services and exits with code 1.
    On success, prints a completion message and exits with code 0.

    Uses INTERVAL for delay between check cycles.
    """
    print("🟧 Waiting for microservices to start...")
    start_time = time.time()

    remaining = SERVICES.copy()

    while remaining:
        if time.time() - start_time > TOTAL_TIMEOUT:
            print("💥 Timeout while waiting for services.")
            for s in remaining:
                print(f"🛑 Failed to wait for: {s['name']}:{s['port']}")
            sys.exit(1)

        print(f"\n🔄 Check attempt... Remaining: {[s['name'] for s in remaining]}")
        newly_healthy = []

        for service in remaining:
            if check_service(service["name"], service["port"]):
                newly_healthy.append(service)

        for s in newly_healthy:
            remaining.remove(s)

        if remaining:
            time.sleep(INTERVAL)

    print("🟢 All services are up and healthy!")


if __name__ == "__main__":
    """Entry point of the script.

    Calls wait_for_services() when the script is run directly.
    Does nothing when the module is imported.
    """
    wait_for_services()

