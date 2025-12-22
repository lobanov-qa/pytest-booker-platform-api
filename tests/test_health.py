import httpx


get_user_response = httpx.get("http://localhost:3004/auth/actuator/health")
get_user_response_data = get_user_response.json()
print('GET user data:', get_user_response)
print('GET user data:', get_user_response_data)