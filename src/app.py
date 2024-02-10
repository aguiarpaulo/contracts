from frontend import ExcelValidatorUI
from backend import process_excel, excel_to_sql
import logging
import sentry_sdk

sentry_sdk.init(
    dsn="https://6cee69d21063f4615b44dcf164ce9527@o4505699197452288.ingest.sentry.io/4506644154417152",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

def main():
    ui = ExcelValidatorUI()
    ui.display_header()

    upload_file = ui.upload_file()

    if upload_file:
        df, result, errors = process_excel(upload_file)
        ui.display_results(result,errors)

        if errors:
            ui.display_wrong_message()
            logging.error("Spreadsheet had schema error")
            sentry_sdk.capture_message("The Excel spreadsheet was wrong")
        elif ui.display_save_button():
            excel_to_sql(df)
            ui.display_success_message()
            logging.info("The SQL database was successfully sent")
            sentry_sdk.capture_message("The SQL database has been updated")

if __name__ == "__main__":
    main()