# LLM4ChipDesign Course Prerequisite Survey Form

## Overview
This directory contains a comprehensive prerequisite survey form for students interested in taking the LLM4ChipDesign course. The survey helps instructors assess student backgrounds and tailor the course content accordingly.

## Files
- `LLM4ChipDesign_Prerequisite_Survey.docx` - The main survey form in Microsoft Word format
- `generate_survey_form.py` - Python script used to generate the survey form
- `SURVEY_README.md` - This documentation file

## Survey Form Content

The survey form covers the following areas essential for the LLM4ChipDesign course:

### Prerequisites Assessed
1. **Digital Logic Design & Boolean Algebra** - Fundamental logic concepts
2. **Computer Architecture & Organization** - Understanding of computer systems
3. **Hardware Description Languages** - Verilog/SystemVerilog experience
4. **Programming Languages** - Python, C/C++ proficiency
5. **Data Structures & Algorithms** - Programming fundamentals
6. **Machine Learning & Artificial Intelligence** - AI/ML background
7. **Natural Language Processing** - NLP concepts for LLM understanding
8. **Formal Verification & Model Checking** - Verification methodologies
9. **Electronic Design Automation (EDA) Tools** - Industry tools experience
10. **FPGA/ASIC Design Flow** - Hardware implementation knowledge
11. **High-Level Synthesis (HLS)** - C-to-hardware concepts
12. **Hardware-Software Co-design** - Interface understanding
13. **Computer Systems & Operating Systems** - Systems knowledge
14. **Software Engineering & Version Control** - Development practices
15. **Mathematics** - Linear algebra, statistics for ML

### Survey Sections
1. **Student Information** - Basic demographic and academic information
2. **Prerequisite Course Assessment** - Rating system for each subject area
3. **Specific Course Experience** - Detailed course background
4. **Tools and Software Experience** - EDA tools, programming environments, AI frameworks
5. **Project Experience** - Practical application of knowledge
6. **Learning Goals and Expectations** - Student objectives and preferences
7. **Additional Information** - Open-ended feedback section

## Usage Instructions

### For Instructors
1. Distribute the `LLM4ChipDesign_Prerequisite_Survey.docx` file to prospective students
2. Have students complete and return the survey before course enrollment
3. Use responses to:
   - Identify students who may need additional preparation
   - Form study groups with complementary skills
   - Adjust course pacing and content depth
   - Prepare targeted review materials

### For Students
1. Download and open the survey form
2. Complete all sections honestly and thoroughly
3. Provide specific examples where requested
4. Submit the completed form as instructed by your instructor

## Course Rationale

This survey is designed specifically for the LLM4ChipDesign course based on the repository content, which covers:

- **Automated Verilog Generation** using LLMs (AutoChip, VeriThoughts, Veritas)
- **Testbench Generation** for hardware verification
- **SystemVerilog Assertion Generation** from natural language
- **High-Level Synthesis** with AI assistance (C2HLSC)
- **Hardware Security** and IP protection
- **SPICE Netlist Generation** for analog circuits
- **Hierarchical Design** methodologies

## Technical Requirements

The survey form is generated using Python with the `python-docx` library and is compatible with:
- Microsoft Word 2007 and later
- LibreOffice Writer
- Google Docs
- Most modern word processors

## Regenerating the Survey

If you need to modify the survey form:

1. Install required dependencies:
   ```bash
   pip install python-docx
   ```

2. Run the generation script:
   ```bash
   python3 generate_survey_form.py
   ```

3. The updated survey will be saved as `LLM4ChipDesign_Prerequisite_Survey.docx`

## Contact Information

For questions about the survey or course prerequisites, please contact the course instructor or refer to the main repository documentation.