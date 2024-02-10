import streamlit as st

class ExcelValidatorUI:
    def __init__(self):
        self.set_page_config()

    def set_page_config(self):
        st.set_page_config(
            page_title='Excel Schema Validator'
        )

    def display_header(self):
        st.title("Attach the excel file")

    def upload_file(self):
        return st.file_uploader("Upload the excel file here", type=['xlsx'])
    
    def display_results(self,result,errors):
        if errors:
            for error in errors:
                st.error(f"Validation Error: {error}")
        else:
            st.success("the schema is correct")

    def display_save_button(self):
        return st.button("Save the data into database")
    
    def display_wrong_message(self):
        return st.error("Improvements required")
    
    def display_success_message(self):
        return st.success("Data successfully saved in the database!")

    
    
    