"""
Test script to verify cookie-based authentication
"""
import requests

BASE_URL = "http://localhost:8000"

def test_login():
    """Test login and cookie setting"""
    print("Testing login...")
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": "sama@gmail.com", "password": "sama123"}
    )
    print(f"Status: {response.status_code}")
    print(f"Cookies: {response.cookies}")
    print(f"Response: {response.json()}")
    return response.cookies

def test_protected_route(cookies):
    """Test accessing protected route with cookie"""
    print("\nTesting protected route...")
    response = requests.get(
        f"{BASE_URL}/analytics/dashboard",
        cookies=cookies
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

def test_logout(cookies):
    """Test logout and cookie clearing"""
    print("\nTesting logout...")
    response = requests.post(
        f"{BASE_URL}/auth/logout",
        cookies=cookies
    )
    print(f"Status: {response.status_code}")
    print(f"Cookies after logout: {response.cookies}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    try:
        cookies = test_login()
        if cookies:
            test_protected_route(cookies)
            test_logout(cookies)
    except Exception as e:
        print(f"Error: {e}")
