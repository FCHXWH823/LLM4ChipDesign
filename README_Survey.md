# LLM4ChipDesign Prerequisite Survey - Google Forms Setup

This directory contains everything needed to create a comprehensive prerequisite survey for the LLM4ChipDesign course/workshop using Google Forms.

## Files Overview

### 📋 `LLM4ChipDesign_Prerequisite_Survey.md`
Complete survey with 32 questions covering:
- Personal information and educational background
- Hardware design experience (HDLs, EDA tools, digital circuits)
- Verification and testing knowledge
- Programming and software development
- Machine Learning and LLM experience
- Specific knowledge areas (CNF, FSMs, prefix circuits, etc.)
- Research background and security awareness
- Learning goals and expectations

### 🔧 `google_forms_structure.json`
Structured JSON configuration containing:
- Form metadata (title, description, settings)
- Question definitions with types and options
- Section organization
- Implementation instructions

### 🐍 `create_google_form.py`
Python script for automated form creation:
- Uses Google Forms API (requires authentication)
- Creates form from JSON configuration
- Includes manual fallback instructions
- Generates helpful templates

## Quick Start (Manual Creation)

### Option 1: Manual Creation (Recommended)
1. Go to [Google Forms](https://forms.google.com)
2. Click "Blank" to create new form
3. Copy questions from `LLM4ChipDesign_Prerequisite_Survey.md`
4. Follow the detailed instructions in the markdown file
5. Configure settings as specified

### Option 2: Automated Creation (Advanced)
1. Install Python dependencies:
   ```bash
   pip install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2
   ```
2. Set up Google Cloud Console:
   - Create project
   - Enable Google Forms API
   - Create OAuth 2.0 credentials
   - Download `credentials.json`
3. Run the script:
   ```bash
   python create_google_form.py
   ```

## Survey Features

### 📊 Question Types
- **Multiple Choice**: Experience levels, background areas
- **Checkboxes**: Multiple selections (tools, languages, frameworks)
- **Short Answer**: Basic information (name, institution)
- **Paragraph**: Open-ended responses (goals, projects)

### 🎯 Coverage Areas
- **Hardware Design**: Verilog, SystemVerilog, VHDL, EDA tools
- **Verification**: SVA, UVM, formal verification, testbenches
- **Programming**: C/C++, Python, HLS, software development
- **AI/ML**: LLMs, frameworks, code generation experience
- **Specialized Topics**: All areas covered in the repository

### ⚙️ Configuration
- Email collection enabled
- One response per person
- Response editing allowed
- Progress bar shown
- Logical question flow maintained

## Data Collection

### 📈 Response Analysis
Responses automatically save to Google Sheets with:
- Individual response tracking
- Automatic summary charts
- Export capabilities (CSV, Excel)
- Real-time response monitoring

### 🔍 Expected Insights
- Participant experience distribution
- Knowledge gaps identification
- Course content customization data
- Prerequisites validation

## Usage Scenarios

### 🎓 Course Planning
- **Before Course**: Assess prerequisite knowledge
- **Content Adaptation**: Tailor material to audience level
- **Group Formation**: Balance teams by experience

### 🔬 Research Applications
- **Baseline Assessment**: Measure starting knowledge
- **Demographics**: Understand participant background
- **Follow-up Studies**: Track learning progression

## Customization

### ✏️ Modifying Questions
1. Edit `LLM4ChipDesign_Prerequisite_Survey.md`
2. Update `google_forms_structure.json` if using automation
3. Test changes before deployment

### 🎨 Branding
- Add institution logo to Google Form
- Customize colors and themes
- Include contact information

## Best Practices

### 📋 Before Deployment
- [ ] Review all questions for clarity
- [ ] Test form functionality
- [ ] Set up response notifications
- [ ] Prepare data analysis plan

### 📊 During Collection
- [ ] Monitor response rates
- [ ] Address participant questions
- [ ] Check for technical issues
- [ ] Send reminders if needed

### 📈 After Collection
- [ ] Export data for analysis
- [ ] Generate summary reports
- [ ] Share insights with instructors
- [ ] Archive responses securely

## Support

### 🐛 Troubleshooting
- **Form not working**: Check question requirements and logic
- **API issues**: Verify credentials and permissions
- **Data problems**: Check export format and encoding

### 📞 Getting Help
- Google Forms Help Center
- Repository maintainers
- Course organizers

## Privacy and Security

### 🔒 Data Protection
- Only collect necessary information
- Secure response storage
- Clear data retention policies
- Participant consent obtained

### 📝 Compliance
- Follow institutional IRB requirements
- Respect privacy regulations
- Maintain data confidentiality
- Provide opt-out mechanisms

---

**Note**: This survey is designed to be comprehensive while remaining manageable for participants (estimated completion time: 10-15 minutes). Adjust questions based on your specific needs and audience.