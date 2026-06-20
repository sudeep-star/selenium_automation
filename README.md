# Selenium Test Automation Framework

## Overview

This project demonstrates a robust web automation framework developed using Python, Selenium WebDriver, and Pytest. The framework follows the Page Object Model (POM) design pattern to ensure scalability, maintainability, and code reusability.

The framework automates critical user workflows on the SauceDemo e-commerce application.

---

## Technologies Used

* Python
* Selenium WebDriver
* Pytest
* Page Object Model (POM)
* HTML Reports
* GitHub Actions
* Git & GitHub

---

## Framework Features

* Page Object Model architecture
* Reusable page methods
* Pytest fixtures
* Smoke and Regression test execution
* HTML test reporting
* Screenshot capture on failures
* Explicit waits for dynamic elements
* CI/CD integration using GitHub Actions

---

## Project Structure

project/

├── pages/

├── tests/

├── utilities/

├── screenshots/

├── reports/

├── .github/workflows/

├── conftest.py

├── pytest.ini

├── requirements.txt

└── README.md

---

## Test Coverage

### Login Functionality

* Successful login
* Invalid login validation
* Locked user validation

### Product Functionality

* Verify product listing
* Add products to cart
* Remove products from cart

### Cart Functionality

* Verify cart contents
* Verify cart count updates

### Checkout Functionality

* Complete checkout process
* Validate checkout information
* Verify successful order placement

---

## Design Principles

### Page Object Model (POM)

Separates page elements and actions from test logic, making the framework easier to maintain and extend.

### Pytest Fixtures

Fixtures are used for browser setup and teardown, reducing code duplication.

### Explicit Waits

Explicit waits improve test stability by synchronizing test execution with application behavior.

---

## Running the Framework

Install dependencies:

pip install -r requirements.txt

Run all tests:

pytest -v

Run smoke tests:

pytest -m smoke

Run regression tests:

pytest -m regression

Generate HTML report:

pytest --html=reports/report.html --self-contained-html

---

## Continuous Integration

GitHub Actions is configured to automatically:

* Install project dependencies
* Execute automated tests
* Validate framework integrity on code changes

---

## Future Improvements

* API Automation Framework
* Parallel Test Execution
* Docker Integration
* Cross-Browser Testing
* Test Data Management
* Advanced Reporting Solutions

---

## Author

Sudeep Adhikary

QA Automation Engineer

Python | Selenium | Pytest | GitHub Actions
