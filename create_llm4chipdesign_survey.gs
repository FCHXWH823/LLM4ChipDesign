/**
 * LLM4ChipDesign Course Prerequisite Survey - Google Form Creator
 * Generated on: September 03, 2025
 * 
 * Instructions:
 * 1. Open Google Apps Script (script.google.com)
 * 2. Create a new project
 * 3. Replace the default code with this script
 * 4. Run the 'createSurveyForm' function
 * 5. Check your Google Drive for the created form
 */

function createSurveyForm() {
  // Create the form
  var form = FormApp.create('LLM4ChipDesign Course Prerequisite Survey');
  form.setDescription(`Welcome to the LLM4ChipDesign course! This course explores the intersection of Large Language Models (LLMs) and chip design, covering topics such as automated Verilog generation, testbench creation, SystemVerilog assertions, and hardware-software co-design using AI.

To ensure you have the necessary background knowledge and to tailor the course content to your experience level, please complete this prerequisite assessment survey. Your responses will help us understand your current knowledge and provide appropriate support during the course.

Please answer all questions honestly. This survey is for assessment purposes only and will not affect your grade.`);
  
  // Configure form settings
  form.setCollectEmail(true);
  form.setAllowResponseEdits(true);
  form.setAcceptingResponses(true);
  
  // Add sections and questions

  // Student Information Section
  var section = form.addPageBreakItem().setTitle('Student Information');
  var q = form.addTextItem().setTitle('Name');
  q.setRequired(true);
  var q = form.addTextItem().setTitle('Student ID');
  q.setRequired(true);
  var q = form.addTextItem().setTitle('Email');
  q.setRequired(true);
  var q = form.addTextItem().setTitle('Academic Year/Level');
  q.setRequired(true);
  var q = form.addTextItem().setTitle('Major/Program');
  q.setRequired(true);
  var q = form.addDateItem().setTitle('Date');
  q.setRequired(true);

  // Prerequisite Course Assessment Section
  var section = form.addPageBreakItem().setTitle('Prerequisite Course Assessment');
  section.setHelpText(`Please indicate your experience level with the following subject areas that are fundamental to this course. Rate your experience using the scale:
• No Experience (0): Never studied or worked with this area
• Basic (1): Introductory course or minimal exposure
• Intermediate (2): One or more courses with practical experience
• Advanced (3): Extensive coursework and/or professional experience
• Expert (4): Teaching/research level knowledge`);
  var q = form.addScaleItem().setTitle('Digital Logic Design & Boolean Algebra');
  q.setBounds(0, 4);
  q.setLeftLabel('No Experience');
  q.setRightLabel('Expert');
  q.setRequired(true);
  var q = form.addScaleItem().setTitle('Computer Architecture & Organization');
  q.setBounds(0, 4);
  q.setLeftLabel('No Experience');
  q.setRightLabel('Expert');
  q.setRequired(true);
  var q = form.addScaleItem().setTitle('Hardware Description Languages (Verilog/SystemVerilog)');
  q.setBounds(0, 4);
  q.setLeftLabel('No Experience');
  q.setRightLabel('Expert');
  q.setRequired(true);
  var q = form.addScaleItem().setTitle('Programming Languages (Python, C/C++)');
  q.setBounds(0, 4);
  q.setLeftLabel('No Experience');
  q.setRightLabel('Expert');
  q.setRequired(true);
  var q = form.addScaleItem().setTitle('Data Structures & Algorithms');
  q.setBounds(0, 4);
  q.setLeftLabel('No Experience');
  q.setRightLabel('Expert');
  q.setRequired(true);
  var q = form.addScaleItem().setTitle('Machine Learning & Artificial Intelligence');
  q.setBounds(0, 4);
  q.setLeftLabel('No Experience');
  q.setRightLabel('Expert');
  q.setRequired(true);
  var q = form.addScaleItem().setTitle('Natural Language Processing (NLP)');
  q.setBounds(0, 4);
  q.setLeftLabel('No Experience');
  q.setRightLabel('Expert');
  q.setRequired(true);
  var q = form.addScaleItem().setTitle('Formal Verification & Model Checking');
  q.setBounds(0, 4);
  q.setLeftLabel('No Experience');
  q.setRightLabel('Expert');
  q.setRequired(true);
  var q = form.addScaleItem().setTitle('Electronic Design Automation (EDA) Tools');
  q.setBounds(0, 4);
  q.setLeftLabel('No Experience');
  q.setRightLabel('Expert');
  q.setRequired(true);
  var q = form.addScaleItem().setTitle('FPGA/ASIC Design Flow');
  q.setBounds(0, 4);
  q.setLeftLabel('No Experience');
  q.setRightLabel('Expert');
  q.setRequired(true);
  var q = form.addScaleItem().setTitle('High-Level Synthesis (HLS)');
  q.setBounds(0, 4);
  q.setLeftLabel('No Experience');
  q.setRightLabel('Expert');
  q.setRequired(true);
  var q = form.addScaleItem().setTitle('Hardware-Software Co-design');
  q.setBounds(0, 4);
  q.setLeftLabel('No Experience');
  q.setRightLabel('Expert');
  q.setRequired(true);
  var q = form.addScaleItem().setTitle('Computer Systems & Operating Systems');
  q.setBounds(0, 4);
  q.setLeftLabel('No Experience');
  q.setRightLabel('Expert');
  q.setRequired(true);
  var q = form.addScaleItem().setTitle('Software Engineering & Version Control');
  q.setBounds(0, 4);
  q.setLeftLabel('No Experience');
  q.setRightLabel('Expert');
  q.setRequired(true);
  var q = form.addScaleItem().setTitle('Mathematics (Linear Algebra, Statistics)');
  q.setBounds(0, 4);
  q.setLeftLabel('No Experience');
  q.setRightLabel('Expert');
  q.setRequired(true);

  // Specific Course Experience Section
  var section = form.addPageBreakItem().setTitle('Specific Course Experience');
  section.setHelpText(`Please list any specific courses you have completed in the following areas (include course names/codes if possible):`);
  var q = form.addParagraphTextItem().setTitle('Digital Circuit Design / Logic Design');
  var q = form.addParagraphTextItem().setTitle('Computer Architecture');
  var q = form.addParagraphTextItem().setTitle('Verilog/VHDL/SystemVerilog');
  var q = form.addParagraphTextItem().setTitle('Machine Learning / AI');
  var q = form.addParagraphTextItem().setTitle('Programming (Python/C/C++)');
  var q = form.addParagraphTextItem().setTitle('Formal Methods / Verification');
  var q = form.addParagraphTextItem().setTitle('Embedded Systems');
  var q = form.addParagraphTextItem().setTitle('Other Relevant Courses');

  // Tools and Software Experience Section
  var section = form.addPageBreakItem().setTitle('Tools and Software Experience');
  section.setHelpText(`Please indicate your familiarity with the following tools and software (check all that apply):`);
  var q = form.addCheckboxItem().setTitle('EDA Tools');
  q.setChoices(['Vivado (Xilinx)', 'Quartus (Intel)', 'ModelSim/QuestaSim', 'Synopsys Tools', 'Cadence Tools', 'Verilator', 'GTKWave'].map(choice => q.createChoice(choice)));
  var q = form.addCheckboxItem().setTitle('Programming Tools');
  q.setChoices(['Python', 'C/C++', 'MATLAB', 'Git/GitHub', 'Jupyter Notebooks', 'Linux/Unix', 'Command Line'].map(choice => q.createChoice(choice)));
  var q = form.addCheckboxItem().setTitle('AI/ML Frameworks');
  q.setChoices(['TensorFlow', 'PyTorch', 'OpenAI API', 'Hugging Face', 'scikit-learn', 'NLTK/spaCy', 'Google Colab'].map(choice => q.createChoice(choice)));

  // Project Experience Section
  var section = form.addPageBreakItem().setTitle('Project Experience');
  var q = form.addParagraphTextItem().setTitle('Have you worked on any hardware design projects? If yes, please describe briefly:');
  var q = form.addParagraphTextItem().setTitle('Have you used any AI/ML tools or APIs in your projects? If yes, please describe:');
  var q = form.addParagraphTextItem().setTitle('Have you written Verilog or VHDL code before? What was the complexity level?');
  var q = form.addParagraphTextItem().setTitle('Have you used any LLMs (ChatGPT, Claude, etc.) for coding assistance? Please describe your experience:');

  // Learning Goals and Expectations Section
  var section = form.addPageBreakItem().setTitle('Learning Goals and Expectations');
  var q = form.addParagraphTextItem().setTitle('What specific aspects of LLM-based chip design are you most interested in learning?');
  var q = form.addParagraphTextItem().setTitle('Do you have any specific career goals related to hardware design or AI?');
  var q = form.addParagraphTextItem().setTitle('What challenges do you expect to face in this course?');
  var q = form.addParagraphTextItem().setTitle('How do you prefer to learn new technical concepts? (hands-on, theory-first, examples, etc.)');

  // Additional Information Section
  var section = form.addPageBreakItem().setTitle('Additional Information');
  var q = form.addParagraphTextItem().setTitle('Please provide any additional information about your background, interests, or concerns that might be relevant to this course:');

  // Set confirmation message
  form.setConfirmationMessage(
    'Thank you for completing the LLM4ChipDesign Course Prerequisite Survey! ' +
    'This information will help us provide the best possible learning experience ' +
    'tailored to your background and goals.'
  );
  
  // Log the form URL
  var formUrl = form.getPublishedUrl();
  Logger.log('Form created successfully!');
  Logger.log('Form URL: ' + formUrl);
  Logger.log('Edit URL: ' + form.getEditUrl());
  
  // Also display in console
  console.log('Form created successfully!');
  console.log('Form URL: ' + formUrl);
  console.log('Edit URL: ' + form.getEditUrl());
  
  return {
    formUrl: formUrl,
    editUrl: form.getEditUrl(),
    formId: form.getId()
  };
}