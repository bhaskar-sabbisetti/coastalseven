import requests

BASE_URL = "http://localhost:8000/api/v1"

def test_flow():
    # 1. Signup
    print("\n1. Testing Signup...")
    signup_data = {
        "email": "bhaskar@sepnoty.com",
        "password": "StrongPass123!",
        "full_name": "Bhaskar Sepnoty"
    }
    try:
        r = requests.post(f"{BASE_URL}/auth/signup", json=signup_data)
        if r.status_code == 201:
            print("✅ Signup Successful:", r.json())
        elif r.status_code == 400 and "already registered" in r.text:
             print("ℹ️ User already exists (Skipping signup validation)")
        else:
            print("❌ Signup Failed:", r.text)
            return
    except Exception as e:
        print(f"❌ Connection Error: {e}")
        return

    # 2. Login
    print("\n2. Testing Login...")
    login_data = {
        "username": "bhaskar@sepnoty.com",
        "password": "StrongPass123!"
    }
    r = requests.post(f"{BASE_URL}/auth/login", data=login_data)
    if r.status_code == 200:
        token = r.json()
        print("✅ Login Successful. Token received.")
        access_token = token["access_token"]
    else:
        print("❌ Login Failed:", r.text)
        return

    # 3. Get Profile (Protected)
    print("\n3. Testing Protected Route (/users/me)...")
    headers = {"Authorization": f"Bearer {access_token}"}
    r = requests.get(f"{BASE_URL}/users/me", headers=headers)
    if r.status_code == 200:
        print("✅ Protected Route Success:", r.json())
    else:
        print("❌ Protected Route Failed:", r.text)

if __name__ == "__main__":
    test_flow()
