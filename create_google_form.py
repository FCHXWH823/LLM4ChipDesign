#!/usr/bin/env python3
"""
Google Forms Creation Helper for LLM4ChipDesign Prerequisite Survey

This script provides utilities to help create and manage the prerequisite survey
using Google Forms API. Note: This requires Google API credentials and the 
Google Forms API to be enabled in your Google Cloud Console.

Installation:
pip install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2

Setup:
1. Go to Google Cloud Console
2. Create a new project or select existing
3. Enable Google Forms API
4. Create credentials (OAuth 2.0 client ID)
5. Download credentials.json file
6. Place in same directory as this script
"""

import json
import os
from typing import Dict, List, Any

try:
    from googleapiclient.discovery import build
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    GOOGLE_API_AVAILABLE = True
except ImportError:
    GOOGLE_API_AVAILABLE = False
    print("Google API client not installed. Install with:")
    print("pip install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2")

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/forms.body']

class GoogleFormsSurveyCreator:
    """Helper class to create Google Forms survey from JSON configuration"""
    
    def __init__(self, credentials_file='credentials.json', token_file='token.json'):
        self.credentials_file = credentials_file
        self.token_file = token_file
        self.service = None
        
    def authenticate(self):
        """Authenticate with Google API"""
        if not GOOGLE_API_AVAILABLE:
            raise ImportError("Google API client libraries not available")
            
        creds = None
        if os.path.exists(self.token_file):
            creds = Credentials.from_authorized_user_file(self.token_file, SCOPES)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not os.path.exists(self.credentials_file):
                    raise FileNotFoundError(f"Credentials file {self.credentials_file} not found")
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, SCOPES)
                creds = flow.run_local_server(port=0)
            
            with open(self.token_file, 'w') as token:
                token.write(creds.to_json())
        
        self.service = build('forms', 'v1', credentials=creds)
        return True
    
    def create_form_from_json(self, json_file='google_forms_structure.json'):
        """Create Google Form from JSON configuration"""
        if not self.service:
            self.authenticate()
            
        with open(json_file, 'r') as f:
            config = json.load(f)
        
        form_config = config['form']
        
        # Create the form
        form = {
            "info": {
                "title": form_config['title'],
                "description": form_config['description']
            }
        }
        
        result = self.service.forms().create(body=form).execute()
        form_id = result['formId']
        
        print(f"Created form with ID: {form_id}")
        print(f"Form URL: https://docs.google.com/forms/d/{form_id}/edit")
        
        # Add questions
        self._add_questions_to_form(form_id, form_config['sections'])
        
        # Configure settings
        self._configure_form_settings(form_id, form_config.get('settings', {}))
        
        return form_id
    
    def _add_questions_to_form(self, form_id: str, sections: List[Dict]):
        """Add questions to the form"""
        requests = []
        
        for section in sections:
            # Add section header if specified
            if section.get('title'):
                requests.append({
                    "createItem": {
                        "item": {
                            "title": section['title'],
                            "description": section.get('description', ''),
                            "pageBreakItem": {}
                        },
                        "location": {"index": len(requests)}
                    }
                })
            
            # Add questions in the section
            for question in section['questions']:
                question_item = self._create_question_item(question)
                requests.append({
                    "createItem": {
                        "item": question_item,
                        "location": {"index": len(requests)}
                    }
                })
        
        if requests:
            batch_update = {"requests": requests}
            self.service.forms().batchUpdate(
                formId=form_id, body=batch_update).execute()
    
    def _create_question_item(self, question: Dict) -> Dict:
        """Create a question item from configuration"""
        item = {
            "title": question['text'],
            "description": question.get('description', ''),
        }
        
        if question['required']:
            item["required"] = True
        
        question_type = question['type']
        
        if question_type == 'SHORT_ANSWER':
            item["textItem"] = {"paragraph": False}
        elif question_type == 'PARAGRAPH':
            item["textItem"] = {"paragraph": True}
        elif question_type == 'MULTIPLE_CHOICE':
            item["choiceItem"] = {
                "type": "RADIO",
                "options": [{"value": opt} for opt in question['options']]
            }
        elif question_type == 'CHECKBOX':
            item["choiceItem"] = {
                "type": "CHECKBOX",
                "options": [{"value": opt} for opt in question['options']]
            }
        elif question_type == 'DROPDOWN':
            item["choiceItem"] = {
                "type": "DROP_DOWN",
                "options": [{"value": opt} for opt in question['options']]
            }
        elif question_type == 'LINEAR_SCALE':
            item["scaleItem"] = {
                "low": question.get('scale_low', 1),
                "high": question.get('scale_high', 5),
                "lowLabel": question.get('low_label', ''),
                "highLabel": question.get('high_label', '')
            }
        
        return item
    
    def _configure_form_settings(self, form_id: str, settings: Dict):
        """Configure form settings"""
        requests = []
        
        if settings.get('collectEmail'):
            requests.append({
                "updateSettings": {
                    "settings": {"quizSettings": {"isQuiz": False}},
                    "updateMask": "quizSettings.isQuiz"
                }
            })
        
        if requests:
            batch_update = {"requests": requests}
            self.service.forms().batchUpdate(
                formId=form_id, body=batch_update).execute()

def create_manual_instructions():
    """Generate step-by-step manual instructions for creating the form"""
    instructions = """
    MANUAL GOOGLE FORMS CREATION INSTRUCTIONS
    =========================================
    
    Since the Google Forms API requires authentication setup, here are manual 
    instructions to create the survey:
    
    1. GO TO GOOGLE FORMS
       - Visit https://forms.google.com
       - Click "Blank" to create a new form
    
    2. SET UP FORM BASICS
       - Title: "LLM4ChipDesign Prerequisite Survey"
       - Description: "This survey assesses participants' background knowledge 
         for the LLM4ChipDesign course/workshop. Your responses will help us 
         tailor the content to match the audience's experience level."
    
    3. CONFIGURE SETTINGS
       - Click the settings gear icon
       - General tab:
         ✓ Collect email addresses
         ✓ Limit to 1 response
         ✓ Allow response editing
       - Presentation tab:
         ✓ Show progress bar
         ✗ Shuffle question order
    
    4. ADD QUESTIONS
       Follow the detailed questions in 'LLM4ChipDesign_Prerequisite_Survey.md'
       
       For each question:
       - Copy the question text
       - Select the appropriate question type
       - Add answer options for multiple choice/checkbox questions
       - Set required/optional as specified
    
    5. ORGANIZE WITH SECTIONS
       - Add section breaks for each major category
       - Sections: Personal Info, Education, Hardware Design, ML/AI, Goals
    
    6. TEST THE FORM
       - Use "Preview" to test the form
       - Check that all questions work correctly
       - Verify logic and flow
    
    7. SHARE THE FORM
       - Click "Send" 
       - Copy the link to share with participants
       - Can also embed in websites or create QR codes
    
    8. SET UP RESPONSE COLLECTION
       - Responses automatically save to Google Sheets
       - Access via "Responses" tab
       - Download as CSV/Excel for analysis
    """
    
    with open('manual_creation_instructions.txt', 'w') as f:
        f.write(instructions)
    
    print("Manual creation instructions saved to 'manual_creation_instructions.txt'")

def generate_csv_template():
    """Generate a CSV template for expected responses"""
    import csv
    
    headers = [
        'Timestamp', 'Email', 'Name', 'Institution', 'Role', 'Education Level',
        'Field of Study', 'HDL Experience', 'HDL Languages', 'Digital Design Experience',
        'EDA Tools', 'Verification Experience', 'Verification Methods', 'Testbench Experience',
        'Programming Experience', 'Programming Languages', 'HLS Experience', 'ML Experience',
        'LLM Experience', 'AI Frameworks', 'Code Generation with LLMs', 'CNF Knowledge',
        'Prefix Circuits Knowledge', 'FSM Knowledge', 'SPICE Knowledge', 'Hardware Security',
        'IP Piracy Awareness', 'Research Experience', 'Learning Goals', 'Topics of Interest',
        'Project Applications', 'Additional Experience', 'Questions/Concerns'
    ]
    
    with open('survey_response_template.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        # Add a sample row with placeholder data
        sample_row = ['Sample'] * len(headers)
        writer.writerow(sample_row)
    
    print("CSV template saved to 'survey_response_template.csv'")

def main():
    """Main function to demonstrate usage"""
    print("LLM4ChipDesign Survey Creation Helper")
    print("=====================================")
    
    # Check if Google API is available
    if not GOOGLE_API_AVAILABLE:
        print("\nGoogle API not available. Generating manual instructions...")
        create_manual_instructions()
        generate_csv_template()
        return
    
    # Check for credentials
    if not os.path.exists('credentials.json'):
        print("\nGoogle API credentials not found.")
        print("To use automated form creation:")
        print("1. Go to Google Cloud Console")
        print("2. Enable Google Forms API") 
        print("3. Create OAuth 2.0 credentials")
        print("4. Download as 'credentials.json'")
        print("\nGenerating manual instructions instead...")
        create_manual_instructions()
        generate_csv_template()
        return
    
    # Try to create form automatically
    try:
        creator = GoogleFormsSurveyCreator()
        form_id = creator.create_form_from_json()
        print(f"\nForm created successfully!")
        print(f"Form ID: {form_id}")
        print(f"Edit URL: https://docs.google.com/forms/d/{form_id}/edit")
        print(f"Response URL: https://docs.google.com/forms/d/{form_id}/viewform")
        
    except Exception as e:
        print(f"\nError creating form: {e}")
        print("Generating manual instructions...")
        create_manual_instructions()
    
    # Always generate helpful files
    generate_csv_template()
    print("\nAdditional files created:")
    print("- manual_creation_instructions.txt")
    print("- survey_response_template.csv")

if __name__ == "__main__":
    main()