# REST API Automation Framework

An automated API testing framework built with Python, PyTest, Requests, JSON Schema, Faker, and Allure Reports.

---

## Tech Stack

* Language: Python 3.10+
* Test Runner: PyTest
* HTTP Client: Requests
* Data Validation: JSON Schema
* Test Data Generation: Faker
* Reporting: Allure Framework

---

## Project Structure
```text
.
├── api_clients/       # API clients (HTTP methods, endpoint wrappers)
├── config/            # Environment configurations and base URLs
├── schemas/           # JSON Schemas for response payload validation
├── tests/             # Positive and negative test suites
├── conftest.py        # PyTest fixtures (Dependency Injection, client init)
├── requirements.txt   # Project dependencies
└── pytest.ini         # PyTest configuration and markers
```
---

## Setup & Installation

1. Clone the repository:
```bash
git clone https://github.com/Assembledis/pet_proj-1.git
cd pet_proj-1
```

2. Set up a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Linux/macOS
# .venv\Scripts\activate   # On Windows
```

3. Install dependencies:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Running Tests

Run all tests:
pytest

Run tests and generate Allure results:
pytest --alluredir=allure-results

Serve the Allure report in your browser:
allure serve allure-results

---

## Key Features & Architecture

- API Client Pattern: Clear separation of test logic from HTTP communication.
- Dynamic Test Data: Automated fake data generation using Faker.
- Schema Validation: Response body structure and type assertions via JSON Schema.
- Comprehensive Test Coverage: Includes both happy path scenarios and negative test cases (400, 404, edge cases).
- Rich Reporting: Integrated with Allure Reports for clear test execution analytics.
