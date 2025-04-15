# Flipkart Automation Framework 🔍🛒

This is an end-to-end test automation framework for Flipkart using Selenium, PyTest, and Allure for reporting.

Tech
- Python 🐍
- Selenium WebDriver
- PyTest
- Page Object Model (POM)
- Allure Reporting
- Git + GitHub

📁 Project Structure
- `pages/` - Page classes following POM
- `tests/` - Test cases
- `conftest.py` - Fixtures for setup/teardown
- `utils/` - Utility/helper methods

🧪 How to Run Tests
```bash
pytest --alluredir=allure-results
allure serve allure-results
