import requests

BASE_URL = "https://restful-booker.herokuapp.com"


def check(name, condition):
    if condition:
        print(f"[PASS] {name}")
        return True
    else:
        print(f"[FAIL] {name}")
        return False


def main():
    passed = 0
    failed = 0

    print("\nRESTful Booker API Test Tool")
    print("=" * 40)

    # 1. Authentication
    response = requests.post(
        f"{BASE_URL}/auth",
        json={
            "username": "admin",
            "password": "password123"
        }
    )

    if check("Authentication", response.status_code == 200 and "token" in response.json()):
        passed += 1
        token = response.json()["token"]
    else:
        failed += 1
        token = None

    # 2. Create Booking
    booking_data = {
        "firstname": "Sourav",
        "lastname": "Rana",
        "totalprice": 500,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-10-01",
            "checkout": "2026-10-05"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(
        f"{BASE_URL}/booking",
        json=booking_data
    )

    if check(
        "Create Booking",
        response.status_code == 200 and "bookingid" in response.json()
    ):
        passed += 1
        booking_id = response.json()["bookingid"]
    else:
        failed += 1
        booking_id = None

    if booking_id:

        # 3. Get Booking
        response = requests.get(
            f"{BASE_URL}/booking/{booking_id}"
        )

        if check(
            "Get Booking",
            response.status_code == 200
            and response.json().get("firstname") == "Sourav"
        ):
            passed += 1
        else:
            failed += 1

        # 4. Invalid Booking ID
        response = requests.get(
            f"{BASE_URL}/booking/999999"
        )

        if check(
            "Invalid Booking ID",
            response.status_code == 404
        ):
            passed += 1
        else:
            failed += 1

        # 5. Update Booking
        if token:
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Cookie": f"token={token}"
            }

            updated_data = {
                "firstname": "SouravUpdated",
                "lastname": "RanaUpdated",
                "totalprice": 750,
                "depositpaid": False,
                "bookingdates": {
                    "checkin": "2026-10-10",
                    "checkout": "2026-10-15"
                },
                "additionalneeds": "Lunch"
            }

            response = requests.put(
                f"{BASE_URL}/booking/{booking_id}",
                headers=headers,
                json=updated_data
            )

            if check(
                "Update Booking",
                response.status_code == 200
            ):
                passed += 1
            else:
                failed += 1

            # 6. Verify Updated Booking
            response = requests.get(
                f"{BASE_URL}/booking/{booking_id}"
            )

            if check(
                "Verify Updated Booking",
                response.status_code == 200
                and response.json().get("firstname") == "SouravUpdated"
                and response.json().get("totalprice") == 750
            ):
                passed += 1
            else:
                failed += 1

        # 7. Get All Bookings
        response = requests.get(
            f"{BASE_URL}/booking"
        )

        if check(
            "Get All Bookings",
            response.status_code == 200
            and isinstance(response.json(), list)
        ):
            passed += 1
        else:
            failed += 1

    print("\n" + "=" * 40)
    print(f"Total Tests : {passed + failed}")
    print(f"Passed      : {passed}")
    print(f"Failed      : {failed}")
    print("=" * 40)


if __name__ == "__main__":
    main()