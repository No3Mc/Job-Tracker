# Using the Job Application Script

This guide will help you use a Python script to automate the process of tracking job applications in an Excel spreadsheet. The script extracts job details from a provided job link and stores them in an Excel file. Follow these steps to use the script:

## Prerequisites

Before using the script, ensure that you have the following:

* [Python](https://www.python.org/downloads/) installed on your computer.
* Required Python packages installed. You can install them using pip:
```bash
pip install requests beautifulsoup4 openpyxl xlwings
```

## Steps
### 1. Install Required Dependencies
Run the pip command in your terminal or command prompt to install the required Python packages.
pip install requests beautifulsoup4 openpyxl xlwings


### 2. Download the Script

Download the Python script (job.py) to your computer.

## Important Note

Before running the script, make sure to modify line 36 in job.py to reflect the actual location of the job.py file on your local machine. You can find the specific line of code by referring to the following GitHub link:

[https://github.com/No3Mc/Applied/blob/cec6bf9031a6eeaedddf9983ace431476bff95fc/job.py#L36](https://github.com/No3Mc/Applied/blob/cec6bf9031a6eeaedddf9983ace431476bff95fc/job.py#L36)

Replace the placeholder path with the actual path to your local job.py file.

### 3. Run the Script

Open your terminal or command prompt and navigate to the directory where you saved job.py. Then, run the script with the following command:

```bash
python job.py <job_link> <programming_language>
```

Replace `<job_link>` with the link to the job posting you want to apply for and `<programming_language>` with the number corresponding to your preferred programming language:

| Programming Language | Number |
|---|---|
| C# | 1 |
| Python | 2 |
| Mix | 3 |
| Other | 4 |

For example:

```bash
python job.py "https://example.com/job-posting" 2
```

### 4. Check the Excel File

The script will create an Excel file named `applied.xlsx` in your specified directory (if it doesn't already exist). You can open this file to view the job application details.

| Column | Description |
|---|---|
| A | Job Link (Clickable hyperlink) |
| B | Description (Defaulted to "N/A") |
| C | Job Title |
| D | Company Name |
| E | Date (Automatically populated) |
| F | Programming Language |

The script will automatically add the job details and format the Excel file.

### 5. Troubleshooting

If you encounter any issues or errors while running the script, refer to any error messages displayed in the terminal for guidance.

That's it! You've successfully used the Python script to add job application details to an Excel file.
