#!/usr/bin/env python3
"""
LLM4ChipDesign Survey Demo - Shows what the Google Form will look like
This script provides a preview of the survey structure and questions.
"""

import json
from datetime import datetime


def display_form_preview():
    """Display a preview of what the Google Form will contain."""
    
    print("🎓 LLM4ChipDesign Course Prerequisite Survey")
    print("=" * 80)
    print()
    
    # Load survey structure
    try:
        with open('survey_structure.json', 'r') as f:
            survey = json.load(f)
    except FileNotFoundError:
        print("❌ Error: Please run 'python3 create_google_form.py' first to generate the survey files.")
        return False
    
    # Display form header
    print("📋 FORM DESCRIPTION:")
    print("-" * 50)
    print(survey['description'])
    print()
    
    # Display each section
    section_count = 0
    question_count = 0
    
    for section_key, section_data in survey['sections'].items():
        section_count += 1
        print(f"📄 SECTION {section_count}: {section_data['title'].upper()}")
        print("=" * 60)
        
        if 'description' in section_data:
            print(f"ℹ️  {section_data['description']}")
            print()
        
        for i, question in enumerate(section_data['questions'], 1):
            question_count += 1
            question_title = question['title']
            question_type = question['type']
            required = "* " if question.get('required', False) else "  "
            
            print(f"{required}Q{question_count}: {question_title}")
            
            # Show question type details
            if question_type == 'scale':
                scale = question['scale']
                labels = " | ".join(scale['labels'])
                print(f"    📊 Scale ({scale['min']}-{scale['max']}): {labels}")
            
            elif question_type == 'checkbox':
                print(f"    ☑️  Multiple choice (select all that apply):")
                for choice in question['choices']:
                    print(f"        ☐ {choice}")
            
            elif question_type == 'text':
                print(f"    📝 Short text answer")
            
            elif question_type == 'paragraph':
                print(f"    📝 Long text answer")
            
            elif question_type == 'date':
                print(f"    📅 Date picker")
            
            print()
        
        print()  # Extra space between sections
    
    # Display summary
    print("📊 SURVEY SUMMARY")
    print("=" * 60)
    print(f"Total Sections: {section_count}")
    print(f"Total Questions: {question_count}")
    
    required_count = sum(
        len([q for q in section['questions'] if q.get('required', False)])
        for section in survey['sections'].values()
    )
    print(f"Required Questions: {required_count}")
    print(f"Optional Questions: {question_count - required_count}")
    
    print()
    print("🔧 FORM SETTINGS")
    print("-" * 30)
    settings = survey['settings']
    print(f"Email Collection: {'Enabled' if settings['collect_email'] else 'Disabled'}")
    print(f"Response Editing: {'Allowed' if settings['allow_response_edits'] else 'Not Allowed'}")
    print(f"Accepting Responses: {'Yes' if settings['accepting_responses'] else 'No'}")
    
    return True


def show_prerequisites_detail():
    """Show detailed view of the prerequisite assessment section."""
    
    try:
        with open('survey_structure.json', 'r') as f:
            survey = json.load(f)
    except FileNotFoundError:
        print("❌ Error: survey_structure.json not found!")
        return False
    
    print("\n🎯 PREREQUISITE COURSE ASSESSMENT DETAIL")
    print("=" * 80)
    
    prereq_section = survey['sections']['prerequisite_assessment']
    print(f"Description: {prereq_section['description']}")
    print()
    
    print("Subject Areas to be Assessed:")
    print("-" * 40)
    
    for i, question in enumerate(prereq_section['questions'], 1):
        print(f"{i:2d}. {question['title']}")
    
    print()
    print("Rating Scale:")
    print("   0 = No Experience (Never studied or worked with this area)")
    print("   1 = Basic (Introductory course or minimal exposure)")  
    print("   2 = Intermediate (One or more courses with practical experience)")
    print("   3 = Advanced (Extensive coursework and/or professional experience)")
    print("   4 = Expert (Teaching/research level knowledge)")
    
    return True


def show_tools_detail():
    """Show detailed view of the tools and software section."""
    
    try:
        with open('survey_structure.json', 'r') as f:
            survey = json.load(f)
    except FileNotFoundError:
        print("❌ Error: survey_structure.json not found!")
        return False
    
    print("\n🛠️  TOOLS AND SOFTWARE EXPERIENCE DETAIL")
    print("=" * 80)
    
    tools_section = survey['sections']['tools_experience']
    
    for question in tools_section['questions']:
        print(f"\n📦 {question['title']}:")
        print("   " + "─" * (len(question['title']) + 1))
        for choice in question['choices']:
            print(f"   ☐ {choice}")
    
    return True


def main():
    """Main function to display the survey preview."""
    
    print("🔍 LLM4ChipDesign Survey Preview Tool")
    print("=" * 80)
    print("This tool shows you exactly what the Google Form will contain.")
    print()
    
    if not display_form_preview():
        return 1
    
    # Show additional details
    show_prerequisites_detail()
    show_tools_detail()
    
    print("\n🚀 NEXT STEPS")
    print("=" * 80)
    print("1. If the preview looks good, create the actual Google Form:")
    print("   • Open script.google.com")
    print("   • Create a new project")
    print("   • Copy the content from 'create_llm4chipdesign_survey.gs'")
    print("   • Run the 'createSurveyForm' function")
    print()
    print("2. For detailed instructions, see: GOOGLE_FORM_SETUP_INSTRUCTIONS.md")
    print("3. For validation, run: python3 validate_survey.py")
    print()
    print(f"📅 Preview generated on: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}")
    
    return 0


if __name__ == "__main__":
    exit(main())