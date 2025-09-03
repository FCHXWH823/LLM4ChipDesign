#!/usr/bin/env python3
"""
LLM4ChipDesign Course Prerequisite Survey - Google Form Generator
This script generates Google Apps Script code to create a Google Form for the prerequisite survey.
"""

import json
from datetime import datetime
from pathlib import Path


class GoogleFormGenerator:
    """Generator for Google Form creation scripts and data structures."""
    
    def __init__(self):
        self.form_title = "LLM4ChipDesign Course Prerequisite Survey"
        self.form_description = self._get_form_description()
        self.sections = self._define_survey_sections()
    
    def _get_form_description(self):
        """Get the form description text."""
        return (
            "Welcome to the LLM4ChipDesign course! This course explores the intersection of "
            "Large Language Models (LLMs) and chip design, covering topics such as automated "
            "Verilog generation, testbench creation, SystemVerilog assertions, and hardware-software "
            "co-design using AI.\n\n"
            "To ensure you have the necessary background knowledge and to tailor the course content "
            "to your experience level, please complete this prerequisite assessment survey. "
            "Your responses will help us understand your current knowledge and provide appropriate "
            "support during the course.\n\n"
            "Please answer all questions honestly. This survey is for assessment purposes only "
            "and will not affect your grade."
        )
    
    def _define_survey_sections(self):
        """Define all sections and questions for the survey."""
        return {
            "student_info": {
                "title": "Student Information",
                "questions": [
                    {"type": "text", "title": "Name", "required": True},
                    {"type": "text", "title": "Student ID", "required": True},
                    {"type": "text", "title": "Email", "required": True},
                    {"type": "text", "title": "Academic Year/Level", "required": True},
                    {"type": "text", "title": "Major/Program", "required": True},
                    {"type": "date", "title": "Date", "required": True}
                ]
            },
            "prerequisite_assessment": {
                "title": "Prerequisite Course Assessment",
                "description": (
                    "Please indicate your experience level with the following subject areas "
                    "that are fundamental to this course. Rate your experience using the scale:\n"
                    "• No Experience (0): Never studied or worked with this area\n"
                    "• Basic (1): Introductory course or minimal exposure\n"
                    "• Intermediate (2): One or more courses with practical experience\n"
                    "• Advanced (3): Extensive coursework and/or professional experience\n"
                    "• Expert (4): Teaching/research level knowledge"
                ),
                "questions": [
                    {
                        "type": "scale",
                        "title": "Digital Logic Design & Boolean Algebra",
                        "scale": {"min": 0, "max": 4, "labels": ["No Experience", "Basic", "Intermediate", "Advanced", "Expert"]},
                        "required": True
                    },
                    {
                        "type": "scale",
                        "title": "Computer Architecture & Organization",
                        "scale": {"min": 0, "max": 4, "labels": ["No Experience", "Basic", "Intermediate", "Advanced", "Expert"]},
                        "required": True
                    },
                    {
                        "type": "scale",
                        "title": "Hardware Description Languages (Verilog/SystemVerilog)",
                        "scale": {"min": 0, "max": 4, "labels": ["No Experience", "Basic", "Intermediate", "Advanced", "Expert"]},
                        "required": True
                    },
                    {
                        "type": "scale",
                        "title": "Programming Languages (Python, C/C++)",
                        "scale": {"min": 0, "max": 4, "labels": ["No Experience", "Basic", "Intermediate", "Advanced", "Expert"]},
                        "required": True
                    },
                    {
                        "type": "scale",
                        "title": "Data Structures & Algorithms",
                        "scale": {"min": 0, "max": 4, "labels": ["No Experience", "Basic", "Intermediate", "Advanced", "Expert"]},
                        "required": True
                    },
                    {
                        "type": "scale",
                        "title": "Machine Learning & Artificial Intelligence",
                        "scale": {"min": 0, "max": 4, "labels": ["No Experience", "Basic", "Intermediate", "Advanced", "Expert"]},
                        "required": True
                    },
                    {
                        "type": "scale",
                        "title": "Natural Language Processing (NLP)",
                        "scale": {"min": 0, "max": 4, "labels": ["No Experience", "Basic", "Intermediate", "Advanced", "Expert"]},
                        "required": True
                    },
                    {
                        "type": "scale",
                        "title": "Formal Verification & Model Checking",
                        "scale": {"min": 0, "max": 4, "labels": ["No Experience", "Basic", "Intermediate", "Advanced", "Expert"]},
                        "required": True
                    },
                    {
                        "type": "scale",
                        "title": "Electronic Design Automation (EDA) Tools",
                        "scale": {"min": 0, "max": 4, "labels": ["No Experience", "Basic", "Intermediate", "Advanced", "Expert"]},
                        "required": True
                    },
                    {
                        "type": "scale",
                        "title": "FPGA/ASIC Design Flow",
                        "scale": {"min": 0, "max": 4, "labels": ["No Experience", "Basic", "Intermediate", "Advanced", "Expert"]},
                        "required": True
                    },
                    {
                        "type": "scale",
                        "title": "High-Level Synthesis (HLS)",
                        "scale": {"min": 0, "max": 4, "labels": ["No Experience", "Basic", "Intermediate", "Advanced", "Expert"]},
                        "required": True
                    },
                    {
                        "type": "scale",
                        "title": "Hardware-Software Co-design",
                        "scale": {"min": 0, "max": 4, "labels": ["No Experience", "Basic", "Intermediate", "Advanced", "Expert"]},
                        "required": True
                    },
                    {
                        "type": "scale",
                        "title": "Computer Systems & Operating Systems",
                        "scale": {"min": 0, "max": 4, "labels": ["No Experience", "Basic", "Intermediate", "Advanced", "Expert"]},
                        "required": True
                    },
                    {
                        "type": "scale",
                        "title": "Software Engineering & Version Control",
                        "scale": {"min": 0, "max": 4, "labels": ["No Experience", "Basic", "Intermediate", "Advanced", "Expert"]},
                        "required": True
                    },
                    {
                        "type": "scale",
                        "title": "Mathematics (Linear Algebra, Statistics)",
                        "scale": {"min": 0, "max": 4, "labels": ["No Experience", "Basic", "Intermediate", "Advanced", "Expert"]},
                        "required": True
                    }
                ]
            },
            "specific_courses": {
                "title": "Specific Course Experience",
                "description": "Please list any specific courses you have completed in the following areas (include course names/codes if possible):",
                "questions": [
                    {"type": "paragraph", "title": "Digital Circuit Design / Logic Design", "required": False},
                    {"type": "paragraph", "title": "Computer Architecture", "required": False},
                    {"type": "paragraph", "title": "Verilog/VHDL/SystemVerilog", "required": False},
                    {"type": "paragraph", "title": "Machine Learning / AI", "required": False},
                    {"type": "paragraph", "title": "Programming (Python/C/C++)", "required": False},
                    {"type": "paragraph", "title": "Formal Methods / Verification", "required": False},
                    {"type": "paragraph", "title": "Embedded Systems", "required": False},
                    {"type": "paragraph", "title": "Other Relevant Courses", "required": False}
                ]
            },
            "tools_experience": {
                "title": "Tools and Software Experience",
                "description": "Please indicate your familiarity with the following tools and software (check all that apply):",
                "questions": [
                    {
                        "type": "checkbox",
                        "title": "EDA Tools",
                        "choices": [
                            "Vivado (Xilinx)",
                            "Quartus (Intel)",
                            "ModelSim/QuestaSim",
                            "Synopsys Tools",
                            "Cadence Tools",
                            "Verilator",
                            "GTKWave"
                        ],
                        "required": False
                    },
                    {
                        "type": "checkbox",
                        "title": "Programming Tools",
                        "choices": [
                            "Python",
                            "C/C++",
                            "MATLAB",
                            "Git/GitHub",
                            "Jupyter Notebooks",
                            "Linux/Unix",
                            "Command Line"
                        ],
                        "required": False
                    },
                    {
                        "type": "checkbox",
                        "title": "AI/ML Frameworks",
                        "choices": [
                            "TensorFlow",
                            "PyTorch",
                            "OpenAI API",
                            "Hugging Face",
                            "scikit-learn",
                            "NLTK/spaCy",
                            "Google Colab"
                        ],
                        "required": False
                    }
                ]
            },
            "project_experience": {
                "title": "Project Experience",
                "questions": [
                    {
                        "type": "paragraph",
                        "title": "Have you worked on any hardware design projects? If yes, please describe briefly:",
                        "required": False
                    },
                    {
                        "type": "paragraph",
                        "title": "Have you used any AI/ML tools or APIs in your projects? If yes, please describe:",
                        "required": False
                    },
                    {
                        "type": "paragraph",
                        "title": "Have you written Verilog or VHDL code before? What was the complexity level?",
                        "required": False
                    },
                    {
                        "type": "paragraph",
                        "title": "Have you used any LLMs (ChatGPT, Claude, etc.) for coding assistance? Please describe your experience:",
                        "required": False
                    }
                ]
            },
            "learning_goals": {
                "title": "Learning Goals and Expectations",
                "questions": [
                    {
                        "type": "paragraph",
                        "title": "What specific aspects of LLM-based chip design are you most interested in learning?",
                        "required": False
                    },
                    {
                        "type": "paragraph",
                        "title": "Do you have any specific career goals related to hardware design or AI?",
                        "required": False
                    },
                    {
                        "type": "paragraph",
                        "title": "What challenges do you expect to face in this course?",
                        "required": False
                    },
                    {
                        "type": "paragraph",
                        "title": "How do you prefer to learn new technical concepts? (hands-on, theory-first, examples, etc.)",
                        "required": False
                    }
                ]
            },
            "additional_info": {
                "title": "Additional Information",
                "questions": [
                    {
                        "type": "paragraph",
                        "title": "Please provide any additional information about your background, interests, or concerns that might be relevant to this course:",
                        "required": False
                    }
                ]
            }
        }
    
    def generate_google_apps_script(self):
        """Generate Google Apps Script code to create the form."""
        script = [
            "/**",
            " * LLM4ChipDesign Course Prerequisite Survey - Google Form Creator",
            f" * Generated on: {datetime.now().strftime('%B %d, %Y')}",
            " * ",
            " * Instructions:",
            " * 1. Open Google Apps Script (script.google.com)",
            " * 2. Create a new project",
            " * 3. Replace the default code with this script",
            " * 4. Run the 'createSurveyForm' function",
            " * 5. Check your Google Drive for the created form",
            " */",
            "",
            "function createSurveyForm() {",
            "  // Create the form",
            f"  var form = FormApp.create('{self.form_title}');",
            f"  form.setDescription(`{self.form_description}`);",
            "  ",
            "  // Configure form settings",
            "  form.setCollectEmail(true);",
            "  form.setAllowResponseEdits(true);",
            "  form.setAcceptingResponses(true);",
            "  ",
            "  // Add sections and questions",
            ""
        ]
        
        for section_key, section_data in self.sections.items():
            script.extend(self._generate_section_script(section_data))
            script.append("")
        
        script.extend([
            "  // Set confirmation message",
            "  form.setConfirmationMessage(",
            "    'Thank you for completing the LLM4ChipDesign Course Prerequisite Survey! ' +",
            "    'This information will help us provide the best possible learning experience ' +",
            "    'tailored to your background and goals.'",
            "  );",
            "  ",
            "  // Log the form URL",
            "  var formUrl = form.getPublishedUrl();",
            "  Logger.log('Form created successfully!');",
            "  Logger.log('Form URL: ' + formUrl);",
            "  Logger.log('Edit URL: ' + form.getEditUrl());",
            "  ",
            "  // Also display in console",
            "  console.log('Form created successfully!');",
            "  console.log('Form URL: ' + formUrl);",
            "  console.log('Edit URL: ' + form.getEditUrl());",
            "  ",
            "  return {",
            "    formUrl: formUrl,",
            "    editUrl: form.getEditUrl(),",
            "    formId: form.getId()",
            "  };",
            "}"
        ])
        
        return "\n".join(script)
    
    def _generate_section_script(self, section_data):
        """Generate script for a specific section."""
        script = [
            f"  // {section_data['title']} Section",
            f"  var section = form.addPageBreakItem().setTitle('{section_data['title']}');"
        ]
        
        if 'description' in section_data:
            script.append(f"  section.setHelpText(`{section_data['description']}`);")
        
        for question in section_data['questions']:
            script.extend(self._generate_question_script(question))
        
        return script
    
    def _generate_question_script(self, question):
        """Generate script for a specific question."""
        script = []
        
        if question['type'] == 'text':
            script.append(f"  var q = form.addTextItem().setTitle('{question['title']}');")
            if question.get('required', False):
                script.append("  q.setRequired(true);")
        
        elif question['type'] == 'date':
            script.append(f"  var q = form.addDateItem().setTitle('{question['title']}');")
            if question.get('required', False):
                script.append("  q.setRequired(true);")
        
        elif question['type'] == 'paragraph':
            script.append(f"  var q = form.addParagraphTextItem().setTitle('{question['title']}');")
            if question.get('required', False):
                script.append("  q.setRequired(true);")
        
        elif question['type'] == 'scale':
            scale = question['scale']
            script.append(f"  var q = form.addScaleItem().setTitle('{question['title']}');")
            script.append(f"  q.setBounds({scale['min']}, {scale['max']});")
            script.append(f"  q.setLeftLabel('{scale['labels'][0]}');")
            script.append(f"  q.setRightLabel('{scale['labels'][-1]}');")
            if question.get('required', False):
                script.append("  q.setRequired(true);")
        
        elif question['type'] == 'checkbox':
            script.append(f"  var q = form.addCheckboxItem().setTitle('{question['title']}');")
            choices = "', '".join(question['choices'])
            script.append(f"  q.setChoices(['{choices}'].map(choice => q.createChoice(choice)));")
            if question.get('required', False):
                script.append("  q.setRequired(true);")
        
        return script
    
    def generate_json_structure(self):
        """Generate JSON structure of the form for reference."""
        return {
            "title": self.form_title,
            "description": self.form_description,
            "settings": {
                "collect_email": True,
                "allow_response_edits": True,
                "accepting_responses": True
            },
            "sections": self.sections,
            "generated_on": datetime.now().isoformat()
        }
    
    def save_files(self, output_dir="."):
        """Save the generated files."""
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        # Save Google Apps Script
        script_content = self.generate_google_apps_script()
        script_file = output_path / "create_llm4chipdesign_survey.gs"
        with open(script_file, 'w', encoding='utf-8') as f:
            f.write(script_content)
        
        # Save JSON structure
        json_content = self.generate_json_structure()
        json_file = output_path / "survey_structure.json"
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(json_content, f, indent=2, ensure_ascii=False)
        
        # Save instructions
        instructions = self._generate_instructions()
        instructions_file = output_path / "GOOGLE_FORM_SETUP_INSTRUCTIONS.md"
        with open(instructions_file, 'w', encoding='utf-8') as f:
            f.write(instructions)
        
        return {
            "script_file": str(script_file),
            "json_file": str(json_file),
            "instructions_file": str(instructions_file)
        }
    
    def _generate_instructions(self):
        """Generate setup and usage instructions."""
        return f"""# LLM4ChipDesign Course Prerequisite Survey - Google Form Setup

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

The survey includes {len(self.sections)} main sections:

{self._generate_section_list()}

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

Generated on: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}
"""
    
    def _generate_section_list(self):
        """Generate a formatted list of sections for documentation."""
        sections_list = []
        for i, (key, section) in enumerate(self.sections.items(), 1):
            question_count = len(section['questions'])
            sections_list.append(f"{i}. **{section['title']}** ({question_count} questions)")
        return "\n".join(sections_list)


def main():
    """Main function to generate the Google Form creation files."""
    print("🚀 Generating LLM4ChipDesign Course Prerequisite Survey Google Form...")
    print("=" * 70)
    
    # Create generator instance
    generator = GoogleFormGenerator()
    
    # Generate and save files
    try:
        files = generator.save_files()
        print("✅ Files generated successfully!")
        print()
        
        for file_type, file_path in files.items():
            print(f"📄 {file_type.replace('_', ' ').title()}: {file_path}")
        
        print()
        print("📋 Survey Summary:")
        print(f"   - Title: {generator.form_title}")
        print(f"   - Sections: {len(generator.sections)}")
        
        total_questions = sum(len(section['questions']) for section in generator.sections.values())
        print(f"   - Total Questions: {total_questions}")
        
        print()
        print("🎯 Next Steps:")
        print("   1. Open script.google.com")
        print("   2. Create a new project")
        print("   3. Copy the content from 'create_llm4chipdesign_survey.gs'")
        print("   4. Run the 'createSurveyForm' function")
        print("   5. Check the execution log for your form URLs")
        print()
        print("📖 For detailed instructions, see: GOOGLE_FORM_SETUP_INSTRUCTIONS.md")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error generating files: {e}")
        return 1


if __name__ == "__main__":
    exit(main())