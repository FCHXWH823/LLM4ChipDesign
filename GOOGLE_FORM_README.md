# LLM4ChipDesign Course Prerequisite Survey - Google Form

This directory contains everything needed to create a Google Form for the LLM4ChipDesign course prerequisite survey.

## 🚀 Quick Start

1. **Generate the form files** (if not already done):
   ```bash
   python3 create_google_form.py
   ```

2. **Validate the structure**:
   ```bash
   python3 validate_survey.py
   ```

3. **Create the Google Form**:
   - Open [script.google.com](https://script.google.com)
   - Create a new project
   - Copy content from `create_llm4chipdesign_survey.gs`
   - Run the `createSurveyForm` function

## 📁 Generated Files

| File | Description |
|------|-------------|
| `create_llm4chipdesign_survey.gs` | Google Apps Script to automatically create the form |
| `survey_structure.json` | Complete survey structure in JSON format |
| `GOOGLE_FORM_SETUP_INSTRUCTIONS.md` | Detailed setup instructions |
| `validate_survey.py` | Validation script to verify the survey structure |

## 📊 Survey Structure

The survey contains **41 questions** across **7 sections**:

1. **Student Information** (6 questions) - Basic student details
2. **Prerequisite Course Assessment** (15 questions) - Experience ratings for key subjects
3. **Specific Course Experience** (8 questions) - Detailed course background
4. **Tools and Software Experience** (3 questions) - Familiarity with relevant tools
5. **Project Experience** (4 questions) - Hands-on experience
6. **Learning Goals and Expectations** (4 questions) - Course objectives
7. **Additional Information** (1 question) - Open feedback

## 🎯 Key Features

- ✅ **Email collection** enabled for tracking responses
- ✅ **Response editing** allowed for students to update answers
- ✅ **Mobile-friendly** design works on all devices
- ✅ **Automatic validation** ensures data quality
- ✅ **Export capabilities** to Google Sheets or CSV

## 🔧 Customization

After creating the form, you can:
- Modify questions or add new ones
- Change styling and themes
- Set response limits and deadlines
- Configure email notifications
- Add logic branching for conditional questions

## 📈 Response Analysis

Responses can be analyzed using:
- Google Forms built-in analytics
- Export to Google Sheets for advanced analysis
- Integration with other data analysis tools

## 🆘 Support

For detailed instructions, see `GOOGLE_FORM_SETUP_INSTRUCTIONS.md`

For troubleshooting:
1. Verify you're signed into the correct Google account
2. Check that the script has proper permissions
3. Ensure all code is copied correctly without truncation

---

*Generated for LLM4ChipDesign - Generative AI for Chip Design Course*