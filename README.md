# Generative AI for Chip Design 

## AutoChip to Generate Functional Verilog 
**Motivation:**  
AutoChip is designed to generate functional Verilog modules from an initial design prompt and testbench using a selected large language model. Errors from compilation and simulation are fed back into the LLM for repair.

- 📄 **Paper:** https://arxiv.org/abs/2311.04887  
- 💻 **Code:** https://github.com/shailja-thakur/AutoChip.git

---

## VeriThoughts: Enabling Automated Verilog Code Generation using Reasoning and Formal Verification
**Motivation:**  
VeriThoughts is a novel dataset designed for reasoning-based Verilog code generation. We establish a new benchmark framework grounded in formal verification methods to evaluate the quality and correctness of generated hardware descriptions. Additionally, we present a suite of specialized small-scale models optimized specifically for Verilog generation. Our work addresses the growing need for automated hardware design tools that can produce verifiably correct implementations from high-level specifications, potentially accelerating the hardware development process while maintaining rigorous correctness guarantees.

- 📄 **Paper:** https://arxiv.org/abs/2505.20302  
- 💻 **Code:** https://github.com/wilyub/VeriThoughts

---

## PrefixLLM: LLM-aided Prefix Circuit Design
**Motivation:**  
Prefix circuits are fundamental components in digital adders, widely used in digital systems due to their efficiency in calculating carry signals. Synthesizing prefix circuits with minimized area and delay is crucial for enhancing the performance of modern computing systems. Recently, large language models (LLMs) have demonstrated a surprising ability to perform text generation tasks. We propose PrefixLLM, which leverages LLMs for prefix circuit synthesis. PrefixLLM transforms the prefix circuit synthesis task into a structured text generation problem, termed the Structured Prefix Circuit Representation (SPCR), and introduces an iterative framework to automatically and accurately generate valid SPCRs. We further present a design space exploration (DSE) framework that uses LLMs to iteratively search for area- and delay-optimized prefix circuits.

- 📄 **Paper:** https://arxiv.org/abs/2412.02594  
- 💻 **Code:** https://github.com/FCHXWH823/PrefixGPT

---

## LLM-aided Testbench Generation and Bug Detection for Finite-State Machines
**Motivation:**  
A key aspect of chip design is functional testing, which relies on testbenches to evaluate the functionality and coverage of Register-Transfer Level (RTL) designs. We aim to enhance testbench generation by incorporating feedback from commercial-grade Electronic Design Automation (EDA) tools into LLMs. Through iterative feedback from these tools, we refine the testbenches to achieve improved test coverage.

- 📄 **Paper:** https://arxiv.org/html/2406.17132v1  
- 🔗 **Link:** https://github.com/jitendra-bhandari/LLM-Aided-Testbench-Generation-for-FSM/

---

## Hybrid-NL2SVA: LLM-based Natural Language to SystemVerilog Assertion
**Motivation:**  
To enhance LLM performance in NL2SVA, we propose a customized retrieval-augmented generation (RAG) framework and a synthetic fine-tuning dataset that together improve LLM’s performance. Our RAG framework (i) constructs a context-preserving database via dynamic splitting technique, (ii) combines global semantic retrieval with keyword-guided retrieval to extract SVA operator-related contexts via HybridRetrieval, and (iii) validates and corrects the use of SVA operators in LLM-generated SVAs via SVA operator-based rechecking. To further improve lightweight models over NL2SVA, our fine-tuning dataset provides prompt-guided explanations that teach LLMs the layer-by-layer construction process of concurrent SVAs, enabling supervised fine-tuning that greatly improves syntax and functionality accuracy.

- 📄 **Paper:** https://arxiv.org/pdf/2506.21569  
- 💻 **Code:** https://github.com/FCHXWH823/RAG-aided-Assertion-Generation

---

## C2HLSC: Use LLM to Bridge the Software-to-Hardware Design Gap
**Motivation:**  
We present a case study using an LLM to rewrite C code for NIST 800-22 randomness tests, a QuickSort algorithm, and AES-128 into HLS-synthesizable C. The LLM iteratively transforms the C code guided by the system prompt and tool's feedback, implementing functions like streaming data and hardware-specific signals. With the hindsight obtained from the case study, we implement a fully automated framework to refactor C code into HLS-compatible formats using LLMs. To tackle complex designs, we implement a preprocessing step that breaks down the hierarchy in order to approach the problem in a divide-and-conquer bottom-up way.

- 📄 **Paper:** https://arxiv.org/abs/2412.00214  
- 💻 **Code:** https://github.com/Lucaz97/c2hlsc

---

## Masala-CHAI: A Large-Scale SPICE Netlist Dataset for Analog Circuits by Harnessing AI
**Motivation:**  
Masala-CHAI is a fully automated framework leveraging large language models (LLMs) to generate Simulation Programs with Integrated Circuit Emphasis (SPICE) netlists. It addresses a long-standing challenge in circuit design automation: automating netlist generation for analog circuits. Automating this workflow could accelerate the creation of fine-tuned LLMs for analog circuit design and verification. In this work, we identify key challenges in automated netlist generation and evaluate multimodal capabilities of state-of-the-art LLMs, particularly GPT-4, in addressing them. We propose a three-step workflow to overcome existing limitations: labeling analog circuits, prompt tuning, and netlist verification. This approach enables end-to-end SPICE netlist generation from circuit schematic images, tackling the persistent challenge of accurate netlist generation.

- 📄 **Paper:** https://arxiv.org/abs/2411.14299  
- 💻 **Code:** https://github.com/jitendra-bhandari/Masala-CHAI

---

## LLMPirate: LLMs for Black-box Hardware IP Piracy
Large language models (LLMs) are increasingly adopted in hardware design and verification, but their powerful generative capabilities also create new security risks. One unexplored threat vector is intellectual property (IP) piracy: rewriting hardware designs to evade piracy detection tools. LLMPirate is the first LLM-based framework that generates pirated circuit design variations capable of consistently bypassing state-of-the-art detection methods. LLMPirate addresses challenges in integrating LLMs with hardware circuit descriptions, scaling to large designs, and ensuring practical efficiency, resulting in an end-to-end automated pipeline.
- 📄 **Paper:** https://arxiv.org/abs/2411.16111

---

## (Security) Assertions by Large Language Models
Assertion-based verification is a popular verification technique that involves capturing design intent in a set of assertions that can be used in formal verification or testing-based checking. However, writing security-centric assertions is a challenging task. In this work, we investigate the use of emerging large language models (LLMs) for code generation in hardware assertion generation for security, where primarily natural language prompts, such as those one would see as code comments in assertion files, are used to produce SystemVerilog assertions.
- 📄 **Paper:** https://arxiv.org/pdf/2306.14027

---

