import sys
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import openpyxl
import xlwings as xw

def main():
    try:
        # Check for the correct number of command-line arguments
        if len(sys.argv) != 3:
            print("Usage: python job.py <job_link> <programming_language>")
            sys.exit(1)

        job_link = sys.argv[1]
        programming_language = sys.argv[2]

        # Define a mapping of numbers to programming languages
        programming_languages = {
            '1': 'C#',
            '2': 'Python',
            '3': 'Mix',
            '4': 'Other'
        }

        # Check if the provided number is valid
        if programming_language not in programming_languages:
            print("Invalid programming language number. Choose 1 for C#, 2 for Python, 3 for Mix, or 4 for Other.")
            sys.exit(1)

        # Get the corresponding programming language based on the input number
        programming_language = programming_languages[programming_language]

        # Define the full path to the Excel file in the user's Downloads directory
        excel_file_path = os.path.expanduser("~/Downloads/Applied/applied.xlsx")

        # Check if the Excel file exists, and create it if it doesn't
        if not os.path.isfile(excel_file_path):
            workbook = openpyxl.Workbook()
            workbook.save(excel_file_path)

        # Open the Excel file with xlwings
        wb = xw.Book(excel_file_path)
        sheet = wb.sheets.active

        # Add header row if the sheet is empty
        if sheet.range('A1').value is None:
            header = ["Links", "Description", "Jobs Applied", "Company Name", "Date", "Programming Language"]
            sheet.range('A1').value = header

        # Add job link and short description (defaulting to "N/A") to Excel
        current_row = sheet.range('A' + str(sheet.cells.last_cell.row)).end('up').row + 1
        sheet.range('A' + str(current_row)).value = job_link
        sheet.range('B' + str(current_row)).value = "N/A"

        # Create a clickable hyperlink for the job link
        sheet.range('A' + str(current_row)).api.Hyperlinks.Add(Anchor=sheet.range('A' + str(current_row)).api,
                                                              Address=job_link, TextToDisplay="Link")

        # Fetch job details from the link
        response = requests.get(job_link)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        job_title = soup.find('title').text

        # Check if the company name element exists
        company_name_element = soup.find('a', href=True, attrs={'data-tracking-control-name': 'public_jobs_company_name'})

        if company_name_element:
            company_name = company_name_element.text.strip()
        else:
            company_name = "N/A (Applied)"

        job_date = datetime.now().strftime('%Y-%m-%d')

        # Add job details to Excel
        sheet.range('C' + str(current_row)).value = job_title
        sheet.range('D' + str(current_row)).value = company_name
        sheet.range('E' + str(current_row)).value = job_date
        sheet.range('F' + str(current_row)).value = programming_language

        # Automatically resize the cells to fit the content
        for column in sheet.used_range.columns:
            column.autofit()

        # Save the Excel file and close it
        wb.save()
        wb.close()

    except requests.exceptions.RequestException as e:
        print(f"Error making the HTTP request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
