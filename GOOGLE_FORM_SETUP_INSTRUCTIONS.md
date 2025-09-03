# LLM4ChipDesign Course Prerequisite Survey - Google Form Setup

This directory contains the necessary files to create a Google Form for the LLM4ChipDesign course prerequisite survey.

## Files Generated

1. **create_llm4chipdesign_survey.gs** - Google Apps Script code to create the form
2. **survey_structure.json** - JSON structure of the survey for reference
3. **GOOGLE_FORM_SETUP_INSTRUCTIONS.md** - This instruction file

## Quick Setup Instructions

### Method 1: Using Google Apps Script (Recommended)

1. **Open Google Apps Script**
   - Go to [script.google.com](https://script.google.com)
   - Sign in with your Google account

2. **Create New Project**
   - Click "New Project"
   - Give it a name like "LLM4ChipDesign Survey Creator"

3. **Add the Script**
   - Delete the default `myFunction()` code
   - Copy and paste the entire content from `create_llm4chipdesign_survey.gs`
   - Save the project (Ctrl+S)

4. **Run the Script**
   - Select the `createSurveyForm` function from the dropdown
   - Click the "Run" button (▶️)
   - Grant necessary permissions when prompted
   - Check the execution log for the form URLs

5. **Access Your Form**
   - The script will output two URLs:
     - **Form URL**: Share this with students to fill out the survey
     - **Edit URL**: Use this to modify the form if needed

### Method 2: Manual Form Creation

If you prefer to create the form manually, use the `survey_structure.json` file as a reference for:
- Question types and titles
- Answer choices and scales
- Section organization
- Required vs. optional fields

## Form Structure

The survey includes 7 main sections:

1. **Student Information** (6 questions)
2. **Prerequisite Course Assessment** (15 questions)
3. **Specific Course Experience** (8 questions)
4. **Tools and Software Experience** (3 questions)
5. **Project Experience** (4 questions)
6. **Learning Goals and Expectations** (4 questions)
7. **Additional Information** (1 questions)

## Form Settings

- **Email Collection**: Enabled
- **Response Editing**: Allowed
- **Public Access**: Accepting responses
- **Confirmation Message**: Custom thank you message

## Customization Options

After creating the form, you can:

1. **Modify Questions**: Add, remove, or edit questions as needed
2. **Adjust Styling**: Change colors, fonts, and themes
3. **Set Response Limits**: Control who can respond and when
4. **Configure Notifications**: Get email alerts for new responses
5. **Export Responses**: Download data to Google Sheets or CSV

## Response Collection

- Responses are automatically collected in Google Forms
- Can be viewed in the form's "Responses" tab
- Can be exported to Google Sheets for analysis
- Individual response summary and analytics available

## Troubleshooting

### Common Issues:

1. **Permission Errors**: Make sure you're signed in to the correct Google account
2. **Script Timeout**: The script should complete in under 30 seconds
3. **Form Not Found**: Check the execution log for error messages

### Getting Help:

- Check Google Apps Script documentation
- Verify all quotation marks and syntax in the script
- Test with a simpler version first if issues persist

## Form URL Distribution

Once created, you can:
- Share the form URL directly with students
- Embed the form in a website or learning management system
- Create a QR code for easy mobile access
- Add it to course materials and announcements

Generated on: September 03, 2025 at 01:31 AM
