# Excel Validator

The Excel Validator is a tool designed to ensure that only data that has been previously agreed upon with business stakeholders is entered, thus avoiding breaking business area indicators.

## Features

- **Data Validation:** The Excel Validator implements rules to validate the data entered in the Excel file, ensuring that only valid data conforming to business rules is accepted.

- **Database Integration:** After data validation, a button is available to automatically direct the validated data to the database. This allows the data to be easily consumed in Business Intelligence projects.

## How to Use

1. Upload the Excel file containing the data to be validated.
2. Click on the "Validate" button to start the data validation process.
3. After successful validation, click on the "Send to Database" button to send the validated data to the database.

## Automated Testing

Automated tests have been incorporated into the `ci.yml` file and are triggered on each pull request. This ensures that future developments in the code will not affect the validation rules previously agreed upon with the business area.

---

With the Excel Validator, you can be sure that your data is always compliant with business rules, ensuring the integrity of the business area indicators.


@@ -1 +1,24 @@
### Installation and Configuration

1. Clone the repository:
```bash
git clone https://github.com/aguiarpaulo/excel_validator.git
cd excel_validator
```
2. Configure the correct Python version with `pyenv`:
```bash
pyenv install 3.11.5
pyenv local 3.11.5
```
3. Install project dependencies:
```bash
python -m venv .venv
# The default is to use .venv
source .venv/bin/activate
# Linux e mac
.venv\Scripts\Activate
# Windows
pip install -r requirements.txt
```
4. Run and test the project:
```bash
task run
task test
```