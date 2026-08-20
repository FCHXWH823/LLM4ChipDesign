# GUIDE: GenAI Units In Digital Design Education

## Abstract
GenAI Units In Digital Design Education (GUIDE) is an open, modular platform for GenAI-driven digital design education. Each unit provides slides, a short video, a runnable lab, and related papers. Instructors can select units to build courses for instructional use. Students can also learn from the units and develop new solutions through projects, competitions, and research. Before a solution becomes a new GUIDE unit, its end-to-end workflow must be evaluated using open-source EDA tools and open-source hardware benchmarks to make sure it runs successfully.

![GUIDE architecture, educational uses, and evaluation flow](overview_new.png)

## Shared Open-Source EDA Tools

GUIDE uses open-source EDA tools so students can run hardware-design and verification workflows without depending on commercial tool licenses. A GUIDE unit may use one or more of the following tools.

| Tool | Simple explanation |
|------|--------------------|
| [Icarus Verilog](https://github.com/steveicarus/iverilog) | Compiles and simulates Verilog designs and testbenches. |
| [Yosys](https://github.com/YosysHQ/yosys) | Synthesizes RTL and reports the resulting hardware structure and design statistics. |
| [cocotb](https://github.com/cocotb/cocotb) | Lets students write Python testbenches that run with HDL simulators. |
| [Verilator](https://github.com/verilator/verilator) | Checks, compiles, and simulates Verilog and SystemVerilog designs at high speed. |
| [SymbiYosys](https://github.com/YosysHQ/sby) | Runs open-source formal-verification flows for proving hardware properties. |

## Shared Open-Source Hardware Benchmarks

The [`benchmark/`](benchmark/) folder contains the benchmark repositories as Git submodules. These benchmarks provide common tasks and test cases for GUIDE units. They are also used to evaluate a proposed unit before it is contributed to GUIDE.

| Benchmark | Simple explanation |
|-----------|--------------------|
| [VerilogEval](benchmark/VerilogEval) ([upstream](https://github.com/NVlabs/verilog-eval)) | Tests how well LLMs generate functionally correct Verilog RTL from natural-language design problems. |
| [ChipBench](benchmark/ChipBench) ([upstream](https://github.com/zhongkaiyu/ChipBench)) | Tests repository-level RTL generation, debugging, and verification with complete design files and tool-backed workflows. |
| [FVEval](benchmark/FVEval) ([upstream](https://github.com/NVlabs/FVEval)) | Tests how well LLMs generate and verify SystemVerilog assertions from natural-language properties and RTL designs. |
| [Trust-Hub](benchmark/Trust-Hub) ([canonical site](https://trust-hub.org/), [Git mirror](https://github.com/UFESL/Trusthub-Trojans)) | Provides hardware designs with inserted Trojans for studying and evaluating hardware-security methods. |

Clone GUIDE together with every benchmark and unit submodule:

```bash
git clone --recurse-submodules https://github.com/GUIDE-EDA/guide.git
```

If GUIDE has already been cloned, initialize and update its submodules with:

```bash
git submodule update --init --recursive
```

---

## Taxonomy: Topic, Subtopic, Unit

| Topic | Subtopic | Unit | Description |
|-------|----------|------|-------------|
| **LLM-aided RTL Generation** | RTL Generation from Natural Language | AutoChip | Generate Verilog from a prompt and testbench plus iterative compilation/simulation feedback. |
| | | ROME | Uses hierarchical prompting to decompose complex designs so smaller open-source LLMs can generate larger Verilog systems with better quality and lower cost. |
| | | Veritas | Has an LLM generate CNF clauses as a formal functional specification and deterministically converts CNF to Verilog for correctness by construction. |
| | | PrefixLLM | Represents prefix-adder synthesis as structured text (SPCR) and performs iterative LLM-guided design space exploration to optimize area and delay. |
| | | VeriDispatcher | Dispatch RTL tasks to LLMs using pre-inference difficulty prediction to improve quality and reduce LLM use cost. |
| | Finetuned LLMs for RTL Generation | VGen | Fine-tune pre-trained LLMs on Verilog code from GitHub and textbooks and evaluates them with syntax and testbench-based functional checks. |
| | | VeriThoughts | Provides a formal-verification-based pipeline to build a reasoning-oriented Verilog dataset and to fine-tune LLMs for high-accuracy Verilog generation. |
| | | VeriReason | A DeepSeek-R1-inspired RTL generation framework that combines supervised fine-tuning with GRPO reinforcement learning and feedback-driven rewards. |
| | | VeriContaminated | Analyzes data contamination in Verilog benchmarks (VerilogEval, RTLLM) to assess the validity and fairness of SOTA LLM code generation evaluations. |
| **LLM-aided RTL Verification** | Simulation-based Verification | Testbench Generation | Given the RTL under test and a natural-language description of the golden RTL, it generates comprehensive test patterns and then refines them using feedback from EDA tools to improve coverage and expose bugs. |
| | | Enhanced Testbench Generation | Starting from the RTL under test and its natural-language description, generate a comprehensive testbench, build a Python golden model to compute outputs, insert self-checking logic, and run simulation end-to-end. |
| | Formal Verification | RAG-based SVA Generation | Builds a knowledge base from OpenTitan documentation and uses retrieval-augmented generation to produce context-aware SVAs for IP blocks. |
| | | NSFPG | Security property generator based on natural language processing (NLP). |
| | | SV Assertions | Utilizing LLMs to generate SystemVerilog assertions from design documentation. |
| | | Assert-O | Optimization of SystemVerilog assertions using LLMs. |
| | | Hybrid-NL2SVA | A RAG framework for NL2SVA and a fine-tuning pipeline with a synthetic dataset to train lightweight LLMs to translate natural-language properties into SVAs. |
| **LLM-aided Hardware Security** | Hardware Attacks | LLMPirate | LLM-driven rewriting to thwart piracy-detection tools. |
| | | ATTRITION | A reinforcement-learning-based framework that models a realistic adversary to systematically evaluate and evade prior hardware-Trojan detection methods, showing dramatically higher attack success than random-insertion assumptions. |
| | | GHOST | An automated LLM-based attack framework that generates and inserts stealthy, synthesizable Hardware Trojans into HDL designs, enabling rapid Trojan creation and highlighting detection risks in modern hardware security flows. |
| | | RTL-Breaker | A framework assessing backdoor attacks on LLM-based HDL generation, analyzing trigger mechanisms and their impact on code quality and security. |
| | Hardware Defenses | Security Assertions | LLM-generated security assertions from natural-language prompts/comments. |
| | | NOODLE | A multimodal, risk-aware Trojan detection unit that addresses limited Trojan benchmarks by using GAN-based data augmentation and a multimodal deep learning detector with uncertainty estimates for decision making. |
| | | TrojanLoC | Use RTL-finetuned LLM embeddings plus lightweight classifiers to detect Trojans, predict types, and localize suspicious lines using TrojanInS dataset. |
| | | LockForge | A multi-agent LLM framework that automates the translation of logic locking schemes from research papers into executable, validated code. |
| | | SALAD | An assessment framework using machine unlearning to remove sensitive IP, contaminated benchmarks, and malicious patterns from LLMs without full retraining. |

---

## Table of Contents
- [Shared Open-Source EDA Tools](#shared-open-source-eda-tools)
- [Shared Open-Source Hardware Benchmarks](#shared-open-source-hardware-benchmarks)
- [AutoChip to Generate Functional Verilog](#autochip-to-generate-functional-verilog)
- [VeriThoughts: Enabling Automated Verilog Code Generation using Reasoning and Formal Verification](#verithoughts-enabling-automated-verilog-code-generation-using-reasoning-and-formal-verification)
- [Rome was Not Built in a Single Step: Hierarchical Prompting for LLM-based Chip Design](#rome-was-not-built-in-a-single-step-hierarchical-prompting-for-llm-based-chip-design)
- [Veritas: Deterministic Verilog Code Synthesis from LLM-Generated Conjunctive Normal Form](#veritas-deterministic-verilog-code-synthesis-from-llm-generated-conjunctive-normal-form)
- [PrefixLLM: LLM-aided Prefix Circuit Design](#prefixllm-llm-aided-prefix-circuit-design)
- [LLM-aided Testbench Generation and Bug Detection for Finite-State Machines](#llm-aided-testbench-generation-and-bug-detection-for-finite-state-machines)
- [Hybrid-NL2SVA: LLM-based Natural Language to SystemVerilog Assertion](#hybrid-nl2sva-llm-based-natural-language-to-systemverilog-assertion)
- [Security Assertions by Large Language Models](#security-assertions-by-large-language-models)
- [OpenTitan RAG SVA Generator](#opentitan-rag-sva-generator)
- [LLMPirate: LLMs for Black-box Hardware IP Piracy](#llmpirate-llms-for-black-box-hardware-ip-piracy)
- [C2HLSC: Use LLM to Bridge the Software-to-Hardware Design Gap](#c2hlsc--llms-can-bridge-the-software-to-hardware-design-gap)
- [Masala-CHAI: A Large-Scale SPICE Netlist Dataset for Analog Circuits by Harnessing AI](#masala-chai-a-large-scale-spice-netlist-dataset-for-analog-circuits-by-harnessing-ai)
- [VeriContaminated: Assessing LLM-Driven Verilog Coding for Data Contamination](#vericontaminated-assessing-llm-driven-verilog-coding-for-data-contamination)
- [SALAD: Systematic Assessment of Machine Unlearning on LLM-Aided Hardware Design](#salad-systematic-assessment-of-machine-unlearning-on-llm-aided-hardware-design)
- [LockForge: Automating Paper-to-Code for Logic Locking with Multi-Agent Reasoning LLMs](#lockForge-automating-paper-to-code-for-logic-locking-with-multi-agent-reasoning-llms)
- [VeriDispatcher: Multi-Model Dispatching through Pre-Inference Difficulty Prediction for RTL Generation Optimization](#veridispatcher-multi-model-dispatching-through-pre-inference-difficulty-prediction-for-rtl-generation-optimization)
- [Benchmarking Large Language Models for Automated Verilog RTL Code Generation](#benchmarking-large-language-models-for-automated-verilog-rtl-code-generation)
- [VeriReason: Reinforcement Learning with Testbench Feedback for Reasoning-Enhanced Verilog Generation](#verireason-reinforcement-learning-with-testbench-feedback-for-reasoning-enhanced-verilog-generation)
- [Unleashing GHOST: An LLM-Powered Framework for Automated Hardware Trojan Design](#unleashing-ghost-an-llm-powered-framework-for-automated-hardware-trojan-design)
- [ATTRITION: Attacking Static Hardware Trojan Detection Techniques Using Reinforcement Learning](#attrition-attacking-static-hardware-trojan-detection-techniques-using-reinforcement-learning)
- [NOODLE: Uncertainty-Aware Hardware Trojan Detection Using Multimodal Deep Learning](#noodle-uncertainty-aware-hardware-trojan-detection-using-multimodal-deep-learning)
- [Course Project: LLM-Based Verilog Adder Generation and Verification](#course-project-llm-based-verilog-adder-generation-and-verification)
- [Git Submodules (Add / Update / Delete)](#git-submodules-add--update--delete)

---

## AutoChip to Generate Functional Verilog 
**Key Idea:**  
AutoChip generates functional Verilog modules from an initial design prompt and testbench using a selected large language model. Errors from compilation and simulation are fed back into the LLM for repair.

- 📄 **Paper:** https://arxiv.org/abs/2311.04887  
- 💻 **Code:** https://github.com/shailja-thakur/AutoChip.git
- 📑 **Slides:** https://github.com/FCHXWH823/LLM4Hardware/blob/main/slides/ETS%202025%20Tutorial.pptx

---

## VeriThoughts: Automated Verilog Code Generation using Reasoning and Formal Verification
**Key Idea:**  
VeriThoughts is a novel dataset designed for reasoning-based Verilog code generation. We establish a new benchmark framework grounded in formal verification methods to evaluate the quality and correctness of generated hardware descriptions. Additionally, it presents a suite of specialized small-scale models optimized specifically for Verilog generation. Our work addresses the growing need for automated hardware design tools that can produce verifiably correct implementations from high-level specifications, potentially accelerating the hardware development process while maintaining rigorous correctness guarantees.

- 📄 **Paper:** https://arxiv.org/abs/2505.20302  
- 💻 **Code:** https://github.com/wilyub/VeriThoughts

---

## Hierarchical Prompting for LLM-based Hierarchical Verilog Generation
**Key Idea:**  
This tool supports hierarchical Verilog generation for complex hardware modules that standard flat prompting methods cannot achieve. This allows smaller open-source LLMs to compete with large proprietary models. Hierarchical prompting reduces verilig generation time and yields savings on compute costs. This module will detail which LLMs are capable of which applications, and how to apply hierarchical methods in various modes. We will explore case studies of generating complex cores using automatic scripted hierarchical prompts.

- 📄 **Paper:** [https://arxiv.org/abs/2407.18276 ](https://arxiv.org/abs/2407.18276) 
- 💻 **Code:** [https://github.com/ajn313/ROME-LLM/tree/main](https://github.com/ajn313/ROME-LLM/tree/main)
- 📄 **Slides:** [https://github.com/FCHXWH823/LLM4Hardware/blob/main/slides/MLCAD%20ROME%20Presentation.pptx](https://github.com/FCHXWH823/LLM4Hardware/blob/main/slides/MLCAD%20ROME%20Presentation.pptx)

---
## DAVE: Deriving Automatically Verilog from English specifications
**Key Idea:**  
DAVE uses a fine-tuned GPT-2 model to automatically translate English specifications into Verilog hardware code. Achieving 94.8% accuracy, the model successfully handles both simple and abstract digital design tasks. 


---

## Veritas: Verilog Code Generation from LLM-Generated Conjunctive Normal Form
**Key Idea:**  
Veritas introduces a novel conjunctive normal form (CNF)-guided verilog synthesis methodology. The idea is to have an LLM generate CNF clauses, a format widely used for formal verification and synthesis validation in hardware design. veritas uses it to formally describe the desired circuit functionality. The generated CNF specifications are deterministically converted into Verilog, ensuring correctness by construction.  

- 📄 **Paper:** https://arxiv.org/pdf/2506.00005v1
- 💻 **Code:** [https://github.com/PrithwishBasuRoy/Veritas.git](https://github.com/PrithwishBasuRoy/Veritas.git)
- 📄 **Slides:** [https://github.com/FCHXWH823/LLM4Hardware/blob/main/slides/Veritas-Presentations.pptx](https://github.com/FCHXWH823/LLM4Hardware/blob/main/slides/Veritas-Presentations.pptx)

---

## PrefixLLM: LLM-aided Verilog Generation for Prefix Adder Circuit Design
**Key Idea:**  
Prefix circuits are fundamental components in digital adders, widely used in digital systems due to their efficiency in calculating carry signals. Synthesizing prefix circuits with minimized area and delay is crucial for enhancing the performance of modern computing systems. PrefixLLM transforms the prefix circuit synthesis task into a structured text generation problem, termed the Structured Prefix Circuit Representation (SPCR), and introduces an iterative framework to automatically and accurately generate valid SPCRs. PrefixLLM further presents a design space exploration (DSE) framework that uses LLMs to iteratively search for area- and delay-optimized prefix circuits.

- 📄 **Paper:** https://arxiv.org/abs/2412.02594  
- 💻 **Code:** https://github.com/FCHXWH823/PrefixGPT

---

## LLM-aided Testbench Generation and Bug Detection for Finite-State Machines
**Key Idea:**  
A key aspect of chip design is functional testing, which relies on testbenches to evaluate the functionality and coverage of Verilog designs. This LL-based tool aims to enhance testbench generation by incorporating feedback from commercial-grade Electronic Design Automation tools. Through iterative feedback from these tools, it refines the testbenches to achieve improved test coverage.

- 📄 **Paper:** https://arxiv.org/html/2406.17132v1  
- 🔗 **Code:** https://github.com/jitendra-bhandari/LLM-Aided-Testbench-Generation-for-FSM/

---

## LLM-based Natural Language to SystemVerilog Assertion
**Key Idea:**  
Assertion-based verification is a popular verification technique that involves capturing design intent in a set of assertions that can be used in formal verification or testing-based checking.  However, writing security-centric assertions is a challenging task. This tool helps LLM generate SystemVerilog assertions from natural language input.

- 📄 **Paper:** https://arxiv.org/pdf/2506.21569  
- 💻 **Code:** https://github.com/FCHXWH823/RAG-aided-Assertion-Generation
- 📄 **Slides:** https://github.com/FCHXWH823/LLM4Hardware/blob/main/slides/MLCAD25-Hybrid-NL2SVA.pptx

---

## (Security) Assertions by Large Language Models
**Key Idea:** This tool investigates the use of LLMs for code generation in hardware assertion generation for security, where primarily natural language prompts, such as those one would see as code comments in assertion files, are used to produce SystemVerilog assertions.
- 📄 **Paper:** https://arxiv.org/abs/2306.14027
- 📄 **Slides:** https://github.com/FCHXWH823/LLM4Hardware/blob/main/slides/llm_assertion_slides.pptx

---

## RAG-based SVA Generator for OpenTitan
**Key Idea:** This system combines web scraping, semantic search, and LLMs to generate high-quality SystemVerilog assertions for OpenTitan hardware IP blocks. It downloads documentation from the OpenTitan website, processes it into a searchable knowledge base, and uses AI to generate contextually relevant SVA properties.
- 💻 **Code:** https://github.com/AnandMenon12/OpenTitan_RAG_SVAGEN

---

## LLMPirate: LLMs for Black-box Hardware IP Piracy
**Key Idea:** LLMs are increasingly adopted in hardware design and verification, but their powerful generative capabilities also create new security risks. One unexplored threat vector is intellectual property (IP) piracy: rewriting hardware designs to evade piracy detection tools. LLMPirate that generates pirated circuit design variations capable of consistently bypassing state-of-the-art detection methods. LLMPirate addresses challenges in integrating LLMs with hardware circuit descriptions, scaling to large designs, and ensuring practical efficiency, resulting in an end-to-end automated pipeline.
- 📄 **Paper:** https://arxiv.org/abs/2411.16111
- 📄 **Slides:** https://github.com/FCHXWH823/LLM4Hardware/blob/main/slides/LLMPirate_slides.pptx

---

## C2HLSC:  LLMs can Bridge the Software-to-Hardware Design Gap
**Key Idea:**  
We present a case study using an LLM to rewrite C code for NIST 800-22 randomness tests, a QuickSort algorithm, and AES-128 into HLS-synthesizable C. The LLM iteratively transforms the C code guided by the system prompt and tool's feedback, implementing functions like streaming data and hardware-specific signals. With the hindsight obtained from the case study, we implement a fully automated framework (C2HLSC) to refactor C code into HLS-compatible formats using LLMs. To tackle complex designs, we implement a preprocessing step that breaks down the hierarchy in order to approach the problem in a divide-and-conquer bottom-up way.

- 📄 **Paper:** https://arxiv.org/abs/2412.00214  
- 💻 **Code:** https://github.com/Lucaz97/c2hlsc
- 📄 **Slides:** https://github.com/FCHXWH823/LLM4Hardware/blob/main/slides/C2HLSC%20-%20Neurips%20Tutorial.pptx

---

## Masala-CHAI: A Large-Scale SPICE Netlist Dataset for Analog Circuits by Harnessing AI
**Key Idea:**  
Masala-CHAI is a fully automated framework leveraging large language models (LLMs) to generate Simulation Programs with Integrated Circuit Emphasis (SPICE) netlists. It addresses a long-standing challenge in circuit design automation: automating netlist generation for analog circuits. Automating this workflow could accelerate the creation of fine-tuned LLMs for analog circuit design and verification. In this work, we identify key challenges in automated netlist generation and evaluate multimodal capabilities of state-of-the-art LLMs, particularly GPT-4, in addressing them. 

- 📄 **Paper:** https://arxiv.org/abs/2411.14299  
- 💻 **Code:** https://github.com/jitendra-bhandari/Masala-CHAI

---

## VeriContaminated: Assessing LLM-Driven Verilog Coding for Data Contamination
**Key Idea:**  
We present the first systematic analysis of data contamination in LLM-based Verilog code generation. Using CCD and Min-K% Probability on VerilogEval and RTLLM, we evaluate major models including CodeGen2.5, Mistral 7B, Phi-4 Mini, LLaMA-{1,2,3.1}, GPT-{2,3.5,4o}, DeepSeek-Coder, CodeQwen 1.5, and fine-tuned variants RTLCoder and Verigen. Our results expose significant contamination risks, calling into question current benchmark validity. We further discuss mitigation strategies and quality–fairness trade-offs toward more reliable Verilog LLM evaluation.

- 📄 **Paper:** https://arxiv.org/abs/2503.13572
- 💻 **Code:** https://github.com/DfX-NYUAD/VeriContaminated

---

## SALAD: Systematic Assessment of Machine Unlearning on LLM-Aided Hardware Design
**Key Idea:**  
We present SALAD, the first comprehensive framework for safeguarding LLM-driven hardware design automation. While Large Language Models (LLMs) excel at Verilog code generation, they also introduce data security risks such as benchmark contamination, intellectual property (IP) leakage, and malicious Verilog generation. SALAD employs machine unlearning to selectively remove contaminated datasets, sensitive design artifacts, and harmful code patterns from pre-trained models—without full retraining. Through targeted case studies, we show that unlearning can effectively mitigate security risks while preserving model utility for trustworthy, contamination-free Verilog generation.

- 📄 **Paper:** https://arxiv.org/abs/2506.02089
- 💻 **Code:** https://github.com/DfX-NYUAD/SALAD

---

## LockForge: Automating Paper-to-Code for Logic Locking with Multi-Agent Reasoning LLMs
**Key Idea:**  
We present LockForge, a first-of-its-kind, multi-agent large language model (LLM) framework that turns LL descriptions in papers into executable and tested code. LockForge provides a carefully crafted pipeline realizing forethought, implementation, iterative refinement, and a multi-stage validation, all to systematically bridge the gap between prose and practice for complex LL schemes. For validation, we devise (i) an LLM-as-Judge stage with a scoring system considering behavioral checks, conceptual mechanisms, structural elements, and reproducibility on benchmarks, and (ii) an independent LLM-as-Examiner stage for ground-truth assessment.

- 📄 **Paper:** https://arxiv.org/abs/2511.18531
- 💻 **Code:** https://github.com/codesanonymousgit-sudo/LockForge

---

## VeriDispatcher: Multi-Model Dispatching through Pre-Inference Difficulty Prediction for RTL Generation Optimization
**Key Idea:**  
Prior work mainly prompts or finetunes a single model. What remains not well studied is how to coordinate multiple different LLMs so they jointly improve RTL quality while also reducing cost, instead of running all models and choosing the best output. We define this as the multi-LLM RTL generation problem. We propose VeriDispatcher, a multi-LLM RTL generation framework that dispatches each RTL task to suitable LLMs based on pre-inference difficulty prediction. For each model, we train a compact classifier over semantic embeddings of task descriptions, using difficulty scores derived from benchmark variants that combine syntax, structural similarity, and functional correctness. At inference, VeriDispatcher uses these predictors to route tasks to a selected subset of LLMs.

- 📄 **Paper:** https://www.arxiv.org/abs/2511.22749
- 💻 **Code:** https://github.com/zwangsyc/VeriOracle/tree/main

---

## Benchmarking Large Language Models for Automated Verilog RTL Code Generation
**Key Idea:**  
We characterize the ability of LLMs to generate useful Verilog. For this, we fine-tune pre-trained LLMs on Verilog datasets collected from GitHub and Verilog textbooks. We construct an evaluation framework comprising test-benches for functional analysis and a flow to test the syntax of Verilog code generated in response to problems of varying difficulty.

- 📄 **Paper:** https://arxiv.org/abs/2212.11140
- 💻 **Code:** https://github.com/shailja-thakur/VGen

---

## VeriReason: Reinforcement Learning with Testbench Feedback for Reasoning-Enhanced Verilog Generation
**Key Idea:**  
Inspired by DeepSeek-R1, we introduce VeriReason, a framework integrating supervised fine-tuning with Guided Reward Proximal Optimization (GRPO) reinforcement learning for RTL generation. Using curated training examples and a feedback-driven reward model, VeriReason combines testbench evaluations with structural heuristics while embedding self-checking capabilities for autonomous error correction.

- 📄 **Paper:** https://arxiv.org/abs/2505.11849
- 💻 **Code:** https://github.com/NellyW8/VeriReason

---

## Unleashing GHOST: An LLM-Powered Framework for Automated Hardware Trojan Design
**Key Idea:**  
This paper addresses these challenges by proposing GHOST (Generator for Hardware-Oriented Stealthy Trojans), an automated attack framework that leverages Large Language Models (LLMs) for rapid HT generation and insertion.

- 📄 **Paper:** https://arxiv.org/abs/2412.02816
- 💻 **Code:** https://github.com/NMSU-PEARL/GHOST_benchmarks

---

## ATTRITION: Attacking Static Hardware Trojan Detection Techniques Using Reinforcement Learning
**Key Idea:**  
We play the role of a realistic adversary and question the efficacy of HT detection techniques by developing an automated, scalable, and practical attack framework, ATTRITION, using reinforcement learning (RL).

- 📄 **Paper:** https://arxiv.org/abs/2208.12897
- 💻 **Code:** https://github.com/gohil-vasudev/ATTRITION

---

## NOODLE: Uncertainty-Aware Hardware Trojan Detection Using Multimodal Deep Learning
**Key Idea:**  
We first employ generative adversarial networks to amplify our data in two alternative representation modalities, a graph and a tabular, ensuring that the dataset is distributed in a representative manner. Further, we propose a multimodal deep learning approach to detect hardware Trojans and evaluate the results from both early fusion and late fusion strategies. We also estimate the uncertainty quantification metrics of each prediction for risk-aware decision-making.

- 📄 **Paper:** https://arxiv.org/abs/2401.09479
- 💻 **Code:** https://github.com/cars-lab-repo/NOODLE?tab=readme-ov-file

---

## NSPG: Natural language Processing-based Security Property Generator for Hardware Security Assurance
**Key Idea:**  
We, for the first time, propose a novel and automated Natural Language Processing (NLP)-based Security Property Generator (NSPG). Specifically, our approach utilizes hardware documentation in order to propose the first hardware security-specific language model, HS-BERT, for extracting security properties dedicated to hardware design. It is capable of phasing a significant amount of hardware specification, and the generated security properties can be easily converted into hardware assertions, thereby reducing the manual effort required for hardware verification.

- 📄 **Paper:** https://dl.acm.org/doi/10.1145/3649329.3656255
- 💻 **Code:** https://github.com/TIES-Lab/NSPG/tree/main

---

## Course Project: LLM-Based Verilog Adder Generation and Verification 
**Project Overview** 

This project is designed to explore the capabilities and limitations of Large Language Models (LLMs) in hardware design, specifically in generating and verifying Verilog code for digital adder circuits. The project consists of two interconnected parts that demonstrate the complete workflow from design generation to verification.

**Project Objectives**
- Understand how LLMs can interpret/generate H/W description language (HDL) code
- Practice reverse engineering Verilog designs into natural language specifications
- Evaluate the accuracy of LLM-generated Verilog code against golden reference designs
- Learn to leverage LLMs for automated testbench generation
- Gain hands-on experience with hardware simulation tools (Iverilog)
- Develop critical analysis skills for comparing synthesizable Verilog architectures
  
**Learning Outcomes**
- Ability to analyze and describe digital circuit architectures in natural language
- Understanding of different adder architectures and their trade-offs
- Proficiency in using LLM tools (ChipChat/AutoChip) for hardware design
- Skills in manual code review and verification of HDL designs
- Experience with testbench development and internal signal verification
- Competence in using Iverilog for RTL simulation and debugging

**Project Tutorial:** 
- https://github.com/GUIDE-EDA/guide/blob/main/FinalProjects/Verilog%20Adder%20Generation.pdf 
---

## Git Submodules (Add / Update / Delete)

> This repo uses Git submodules for some components. Use the commands below to add a new submodule, pull updates from its original repo, or remove it.

### Add a submodule
```bash
git submodule add -b <branch_name> <repository_url> <path/to/submodule>
git submodule init
git submodule update
git add .
git commit -m "add <your/module/name>"
git push origin main
```

#### 📌 After adding a new submodule  

Please **also update this README** by adding a new section for the submodule with:  

- **Title** (project name)  
- **Motivation** (short description of its purpose)  
- **Original GitHub repo** (link to the repo)  

This keeps the documentation consistent for future contributors.  

### Update a submodule
```bash
cd <your/module/path>
git fetch
git checkout main
git pull origin main
cd ..
git add <your/module/path>
git commit -m "update <your/module/name>"
git push origin main
```

### Delete a submodule
```bash
git rm <your/module/path>
git commit -m "delete <your/module/name>"
```
