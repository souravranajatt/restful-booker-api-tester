# RESTful Booker API Testing Tool

Automated API testing tool for the RESTful Booker API.

## Requirements
- Python 3
- Internet connection

## Setup

Install the required dependency:

```bash
python3 -m pip install -r requirements.txt

## Run Tests

Run the automated test tool:

```bash
./run.sh

## Tests Included

The tool tests:

1. Authentication
2. Create Booking
3. Get Booking
4. Invalid Booking ID
5. Update Booking
6. Verify Updated Booking
7. Get All Bookings

## Test Result

Example successful execution:

```text
Total Tests : 7
Passed      : 7
Failed      : 0

## Project Structure

```text
restful-booker-api-tester/
├── tool/
│   └── test_api.py
├── postman/
├── jmeter/
├── report/
├── requirements.txt
├── run.sh
└── README.md