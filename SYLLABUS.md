# Course Syllabus: Generative AI for Chip Design

## Course Overview
This 14-week course provides comprehensive coverage of Large Language Model (LLM) applications in chip design, from basic Verilog generation to advanced hardware verification and synthesis. Each module follows a 2-week structure focusing on both theoretical understanding and practical implementation.

## Course Structure
- **Total Duration:** 14 weeks
- **Module Format:** 2 weeks per module (7 modules total)
- **Week 1 of each module:** Introduction to concepts, theory, and homework assignment
- **Week 2 of each module:** Hands-on homework solution sessions and practical exercises

---

## Module Schedule

### **Module 1: AutoChip - Functional Verilog Generation (Weeks 1-2)**

**Week 1: Introduction and Theory**
- **Learning Objectives:**
  - Understand LLM-based Verilog generation fundamentals
  - Learn about error feedback and iterative design repair
  - Explore testbench-driven development

- **Topics Covered:**
  - Introduction to AutoChip framework
  - LLM prompt engineering for hardware design
  - Compilation and simulation feedback loops
  - Error analysis and automated repair strategies

- **Homework Assignment:**
  - Set up AutoChip environment
  - Generate a simple multiplexer using AutoChip
  - Document compilation errors and LLM responses
  - Compare generated code with hand-written implementation

**Week 2: Hands-on Workshop**
- Review homework solutions
- Troubleshoot common AutoChip issues
- Live demonstration of complex module generation
- Group exercise: Generate and debug a finite state machine

**Resources:**
- 📄 Paper: https://arxiv.org/abs/2311.04887
- 💻 Code: https://github.com/shailja-thakur/AutoChip.git
- 📊 Tutorial: `colab-scripts/AutoChip_Tutorial.ipynb`

---

### **Module 2: Hierarchical Prompting with ROME (Weeks 3-4)**

**Week 1: Introduction and Theory**
- **Learning Objectives:**
  - Master hierarchical design decomposition
  - Understand the limitations of flat prompting
  - Learn ROME methodology for complex designs

- **Topics Covered:**
  - Hierarchical vs. flat prompting strategies
  - Design decomposition techniques
  - ROME framework architecture
  - Cost-benefit analysis of hierarchical approaches

- **Homework Assignment:**
  - Implement a 16-to-1 multiplexer using hierarchical prompting
  - Compare results with flat prompting approach
  - Analyze generation time and code quality metrics
  - Document the hierarchical design process

**Week 2: Hands-on Workshop**
- Homework solution walkthrough
- Advanced ROME techniques
- Case study: Processor core generation
- Team project: Design a simple ALU hierarchically

**Resources:**
- 📄 Paper: https://arxiv.org/abs/2407.18276
- 💻 Code: https://github.com/ajn313/ROME-LLM/tree/main
- 📊 Tutorial: `colab-scripts/ROME_demo.ipynb`

---

### **Module 3: VeriThoughts - Reasoning-Based Generation (Weeks 5-6)**

**Week 1: Introduction and Theory**
- **Learning Objectives:**
  - Understand reasoning-based code generation
  - Learn formal verification integration
  - Master quality assessment metrics

- **Topics Covered:**
  - Reasoning methodologies in hardware design
  - Formal verification principles
  - VeriThoughts dataset and benchmarks
  - Quality metrics and correctness guarantees

- **Homework Assignment:**
  - Use VeriThoughts to generate a counter with enable
  - Apply formal verification to validate the design
  - Compare reasoning-based vs. direct generation approaches
  - Analyze the verification results and fix any issues

**Week 2: Hands-on Workshop**
- Homework review and discussion
- Advanced reasoning techniques
- Formal verification tools hands-on
- Project: Design and verify a shift register

**Resources:**
- 📄 Paper: https://arxiv.org/abs/2505.20302
- 💻 Code: https://github.com/wilyub/VeriThoughts
- 📊 Tutorial: `colab-scripts/VeriThoughts_Tutorial.ipynb`

---

### **Module 4: Veritas - CNF-Guided Synthesis (Weeks 7-8)**

**Week 1: Introduction and Theory**
- **Learning Objectives:**
  - Understand CNF (Conjunctive Normal Form) in hardware design
  - Learn deterministic synthesis methodologies
  - Master correctness-by-construction principles

- **Topics Covered:**
  - CNF fundamentals and applications
  - LLM-generated CNF specifications
  - Deterministic Verilog synthesis
  - Correctness guarantees and validation

- **Homework Assignment:**
  - Generate CNF specifications for a 4-bit adder
  - Convert CNF to Verilog using Veritas
  - Validate the generated design
  - Compare with traditional design approaches

**Week 2: Hands-on Workshop**
- CNF-to-Verilog conversion practice
- Homework solution review
- Advanced Veritas features
- Lab: Design a priority encoder using CNF

**Resources:**
- 📄 Paper: https://arxiv.org/pdf/2506.00005v1
- 💻 Code: https://github.com/PrithwishBasuRoy/Veritas.git
- 📊 Tutorial: `colab-scripts/Veritas_tutorial.ipynb`

---

### **Module 5: LLM-Aided Testbench Generation (Weeks 9-10)**

**Week 1: Introduction and Theory**
- **Learning Objectives:**
  - Master testbench generation principles
  - Understand coverage-driven verification
  - Learn EDA tool integration strategies

- **Topics Covered:**
  - Functional testing fundamentals
  - Coverage metrics and analysis
  - EDA tool feedback integration
  - Iterative testbench refinement

- **Homework Assignment:**
  - Generate comprehensive testbenches for a finite state machine
  - Analyze coverage reports and identify gaps
  - Use LLM feedback to improve test coverage
  - Document the iterative improvement process

**Week 2: Hands-on Workshop**
- Testbench evaluation and improvement
- Coverage analysis techniques
- EDA tool integration practice
- Project: Complete verification of a FIFO design

**Resources:**
- 📄 Paper: https://arxiv.org/html/2406.17132v1
- 💻 Code: https://github.com/jitendra-bhandari/LLM-Aided-Testbench-Generation-for-FSM/
- 📊 Tutorial: `colab-scripts/LLM_Aided_Testbench_Generation_for_FSM.ipynb`

---

### **Module 6: SystemVerilog Assertion Generation (Weeks 11-12)**

**Week 1: Introduction and Theory**
- **Learning Objectives:**
  - Understand assertion-based verification
  - Master natural language to SVA conversion
  - Learn security-centric assertion design

- **Topics Covered:**
  - SystemVerilog Assertion (SVA) fundamentals
  - Natural language processing for hardware specs
  - Security assertion patterns
  - Formal verification with assertions

- **Homework Assignment:**
  - Convert natural language security specifications to SVA
  - Implement assertions for a simple processor interface
  - Test assertions using formal verification tools
  - Analyze assertion coverage and effectiveness

**Week 2: Hands-on Workshop**
- Assertion writing best practices
- Security assertion patterns
- Formal verification with SVA
- Final project: Secure communication protocol assertions

**Resources:**
- 📄 Paper: https://arxiv.org/pdf/2506.21569
- 💻 Code: https://github.com/FCHXWH823/RAG-aided-Assertion-Generation
- 📊 Tutorial: `colab-scripts/Hybrid_NL2SVA.ipynb`

---

### **Module 7: C2HLSC - Software to Hardware Bridge (Weeks 13-14)**

**Week 1: Introduction and Theory**
- **Learning Objectives:**
  - Master C-to-HLS code transformation
  - Understand software-hardware design gaps
  - Learn automated refactoring techniques

- **Topics Covered:**
  - High-Level Synthesis (HLS) fundamentals
  - C code refactoring for hardware synthesis
  - Streaming interfaces and hardware optimizations
  - Automated framework design

- **Homework Assignment:**
  - Refactor a C implementation of AES encryption for HLS
  - Apply C2HLSC framework to convert software algorithms
  - Analyze synthesis results and optimization opportunities
  - Compare software vs. hardware implementations

**Week 2: Hands-on Workshop**
- HLS optimization techniques
- Advanced C2HLSC features
- Performance analysis and comparison
- Capstone project: End-to-end software-to-hardware design flow

**Resources:**
- 📄 Paper: https://arxiv.org/abs/2412.00214
- 💻 Code: https://github.com/Lucaz97/c2hlsc
- 📊 Tutorial: `colab-scripts/C2HLSC_Tutorial.ipynb`

---

## Assessment Structure

### Weekly Homework (50%)
- Week 1 of each module: Theoretical understanding and setup (25%)
- Week 2 of each module: Practical implementation and analysis (25%)

### Module Projects (30%)
- Mid-term project (Week 7): Integration of Modules 1-3
- Final project (Week 14): Comprehensive design using multiple tools

### Participation and Labs (20%)
- In-class workshop participation
- Peer code reviews
- Discussion forum contributions

## Prerequisites
- Basic understanding of digital logic design
- Familiarity with Verilog/SystemVerilog
- Python programming experience
- Access to EDA tools (simulation and synthesis)

## Required Software
- Python 3.8+
- ModelSim/QuestaSim or equivalent simulator
- Synthesis tools (Vivado, Quartus, or equivalent)
- Git for version control
- Jupyter Notebook environment
- LLM API access (OpenAI, Anthropic, or equivalent)

## Learning Outcomes
By the end of this course, students will be able to:
1. Apply LLMs effectively for hardware design automation
2. Implement hierarchical design methodologies
3. Generate and verify hardware designs using AI tools
4. Create comprehensive testbenches and assertions
5. Bridge software and hardware design domains
6. Evaluate and compare different AI-driven design approaches
7. Integrate multiple tools for complete design flows

## Additional Resources
- **Videos:** Course video materials in `/videos` directory
- **Slides:** Lecture presentations in `/slides` directory
- **Code Examples:** Hands-on tutorials in `/colab-scripts` directory
- **Reference Papers:** Links provided in each module section

## Support and Office Hours
- Instructor office hours: TBD
- TA sessions: TBD
- Online discussion forum: TBD
- Technical support: Course GitHub repository issues

---

*This syllabus provides a structured 14-week journey through the cutting-edge intersection of AI and chip design, preparing students for the future of hardware engineering.*