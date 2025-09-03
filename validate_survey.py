#!/usr/bin/env python3
"""
LLM4ChipDesign Survey Validation Script
This script validates that the generated Google Form structure matches the original survey content.
"""

import json
from pathlib import Path


def validate_survey_structure():
    """Validate the generated survey structure against requirements."""
    print("🔍 Validating LLM4ChipDesign Survey Structure...")
    print("=" * 60)
    
    # Load the generated structure
    try:
        with open('survey_structure.json', 'r') as f:
            survey = json.load(f)
    except FileNotFoundError:
        print("❌ Error: survey_structure.json not found!")
        print("   Please run create_google_form.py first.")
        return False
    
    # Validation tests
    tests_passed = 0
    total_tests = 0
    
    # Test 1: Basic structure
    total_tests += 1
    if all(key in survey for key in ['title', 'description', 'settings', 'sections']):
        print("✅ Test 1: Basic JSON structure is complete")
        tests_passed += 1
    else:
        print("❌ Test 1: Missing required JSON fields")
    
    # Test 2: Required sections
    total_tests += 1
    required_sections = [
        'student_info', 'prerequisite_assessment', 'specific_courses',
        'tools_experience', 'project_experience', 'learning_goals', 'additional_info'
    ]
    
    if all(section in survey['sections'] for section in required_sections):
        print("✅ Test 2: All required sections are present")
        tests_passed += 1
    else:
        missing = [s for s in required_sections if s not in survey['sections']]
        print(f"❌ Test 2: Missing sections: {missing}")
    
    # Test 3: Question count validation
    total_tests += 1
    expected_counts = {
        'student_info': 6,
        'prerequisite_assessment': 15,
        'specific_courses': 8,
        'tools_experience': 3,
        'project_experience': 4,
        'learning_goals': 4,
        'additional_info': 1
    }
    
    counts_correct = True
    for section_key, expected_count in expected_counts.items():
        if section_key in survey['sections']:
            actual_count = len(survey['sections'][section_key]['questions'])
            if actual_count != expected_count:
                print(f"❌ Section '{section_key}': Expected {expected_count} questions, got {actual_count}")
                counts_correct = False
    
    if counts_correct:
        print("✅ Test 3: All sections have correct question counts")
        tests_passed += 1
    
    # Test 4: Prerequisite subjects validation
    total_tests += 1
    expected_subjects = [
        "Digital Logic Design & Boolean Algebra",
        "Computer Architecture & Organization", 
        "Hardware Description Languages (Verilog/SystemVerilog)",
        "Programming Languages (Python, C/C++)",
        "Data Structures & Algorithms",
        "Machine Learning & Artificial Intelligence",
        "Natural Language Processing (NLP)",
        "Formal Verification & Model Checking",
        "Electronic Design Automation (EDA) Tools",
        "FPGA/ASIC Design Flow",
        "High-Level Synthesis (HLS)",
        "Hardware-Software Co-design",
        "Computer Systems & Operating Systems",
        "Software Engineering & Version Control",
        "Mathematics (Linear Algebra, Statistics)"
    ]
    
    prereq_questions = survey['sections']['prerequisite_assessment']['questions']
    prereq_titles = [q['title'] for q in prereq_questions]
    
    if all(subject in prereq_titles for subject in expected_subjects):
        print("✅ Test 4: All prerequisite subjects are included")
        tests_passed += 1
    else:
        missing_subjects = [s for s in expected_subjects if s not in prereq_titles]
        print(f"❌ Test 4: Missing prerequisite subjects: {missing_subjects}")
    
    # Test 5: Tools categories validation
    total_tests += 1
    tools_section = survey['sections']['tools_experience']['questions']
    tool_categories = [q['title'] for q in tools_section]
    expected_categories = ["EDA Tools", "Programming Tools", "AI/ML Frameworks"]
    
    if all(cat in tool_categories for cat in expected_categories):
        print("✅ Test 5: All tool categories are included")
        tests_passed += 1
    else:
        missing_cats = [c for c in expected_categories if c not in tool_categories]
        print(f"❌ Test 5: Missing tool categories: {missing_cats}")
    
    # Summary
    print("\n" + "=" * 60)
    print(f"📊 Validation Summary: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("🎉 All validation tests passed! The survey structure is correct.")
        return True
    else:
        print("⚠️  Some validation tests failed. Please review the issues above.")
        return False


def display_survey_overview():
    """Display an overview of the survey structure."""
    try:
        with open('survey_structure.json', 'r') as f:
            survey = json.load(f)
    except FileNotFoundError:
        print("❌ Error: survey_structure.json not found!")
        return
    
    print("\n📋 Survey Overview:")
    print("=" * 60)
    print(f"📝 Title: {survey['title']}")
    print(f"📊 Total Sections: {len(survey['sections'])}")
    
    total_questions = sum(len(section['questions']) for section in survey['sections'].values())
    print(f"❓ Total Questions: {total_questions}")
    
    print("\n📑 Section Breakdown:")
    for i, (key, section) in enumerate(survey['sections'].items(), 1):
        question_count = len(section['questions'])
        print(f"   {i}. {section['title']}: {question_count} questions")
        
        # Show question types for each section
        question_types = {}
        for question in section['questions']:
            q_type = question['type']
            question_types[q_type] = question_types.get(q_type, 0) + 1
        
        type_summary = ", ".join([f"{count} {qtype}" for qtype, count in question_types.items()])
        print(f"      └─ Types: {type_summary}")
    
    print(f"\n⚙️  Form Settings:")
    settings = survey['settings']
    for setting, value in settings.items():
        print(f"   - {setting.replace('_', ' ').title()}: {value}")


def main():
    """Main validation function."""
    print("🔬 LLM4ChipDesign Survey Validation Tool")
    print("=" * 60)
    
    # Check if required files exist
    required_files = [
        'survey_structure.json',
        'create_llm4chipdesign_survey.gs',
        'GOOGLE_FORM_SETUP_INSTRUCTIONS.md'
    ]
    
    missing_files = [f for f in required_files if not Path(f).exists()]
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        print("\n💡 Please run 'python3 create_google_form.py' first to generate all files.")
        return 1
    
    print("✅ All required files are present")
    
    # Run validation
    validation_passed = validate_survey_structure()
    
    # Display overview
    display_survey_overview()
    
    if validation_passed:
        print("\n🚀 Ready for Google Form Creation!")
        print("   Next steps:")
        print("   1. Open script.google.com")
        print("   2. Create a new project")
        print("   3. Copy content from 'create_llm4chipdesign_survey.gs'")
        print("   4. Run the script to create your form")
        print("\n📖 See GOOGLE_FORM_SETUP_INSTRUCTIONS.md for detailed instructions.")
        return 0
    else:
        print("\n⚠️  Please fix the validation issues before proceeding.")
        return 1


if __name__ == "__main__":
    exit(main())