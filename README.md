# Using the Extension

This extension designed for LinkedIn. The extension adds features to help manage and organize job listings on LinkedIn. Here's an overview of its key functions:

1. **Initialization**: The code initializes variables and retrieves stored data from local storage, including job data, click count, and job count.

2. **Job List Management**:
   - You can add a job listing to the extension by clicking the "Applied" button.
   - The extension extracts the job title and page URL from the currently active LinkedIn tab and stores this data along with the click count.
   - The job listings are displayed in an ordered list, and the click count is updated.

3. **Clear Job List**:
   - You can clear the job list by clicking the "Clear All" button. This action also clears the job data from local storage.

4. **Show/Hide Job List**:
   - The "Show Job List" button toggles the visibility of the job list.

5. **Export to Excel**:
   - The "Export to Excel" button allows you to export the job data as an Excel file.
   - It generates an Excel worksheet with job descriptions and links and saves it as "Applied.xlsx."

The extension enhances your LinkedIn job search experience by allowing you to keep track of the jobs you've viewed and easily export this data for further analysis.

**Note**: This code is designed to be used as part of a Chrome extension and relies on Chrome extension APIs, such as `chrome.scripting`, `chrome.runtime`, and `chrome.storage`, to interact with the LinkedIn web page and manage data.

## How to Use the Extension

To use this extension, follow these steps based on your browser:

### Chrome

1. Open Google Chrome.

2. Click on the three vertical dots (menu icon) in the top-right corner of the browser window.

3. Go to "Extensions" in the menu.

4. Enable "Developer mode" in the top-right corner of the Extensions page.

5. Click the "Load unpacked" button and select the folder containing the extension files.

6. The extension should now appear in your Chrome browser's toolbar.

7. Visit LinkedIn and click on the extension icon to activate it. Follow the on-screen instructions to use the extension features.

### Microsoft Edge

1. Open Microsoft Edge.

2. Click on the three horizontal dots (menu icon) in the top-right corner of the browser window.

3. Go to "Extensions" in the menu.

4. Enable "Developer mode" in the bottom-left corner of the Extensions page.

5. Click the "Load unpacked" button and select the folder containing the extension files.

6. The extension should now appear in your Edge browser's toolbar.

7. Visit LinkedIn and click on the extension icon to activate it. Follow the on-screen instructions to use the extension features.

### Mozilla Firefox

1. Open Mozilla Firefox.

2. Click on the three horizontal lines (menu icon) in the top-right corner of the browser window.

3. Go to "Add-ons" in the menu.

4. Click on "Extensions" in the sidebar.

5. Click the gear icon in the top-right corner and select "Debug Add-ons."

6. Click the "Load Temporary Add-on" button and select the folder containing the extension files.

7. The extension should now appear in your Firefox browser.

8. Visit LinkedIn and click on the extension icon to activate it. Follow the on-screen instructions to use the extension features.

Now, you can use the extension to enhance your LinkedIn job search experience and manage your job listings effectively.

---

# Using the Python Job Application Script

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
