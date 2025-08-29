# Poster PPTX Generation

This directory contains tools to convert the HTML poster (`poster.html`) to PowerPoint format (`poster.pptx`).

## Generated Files

- `poster.pptx` - PowerPoint presentation containing a single slide with the same content as poster.html
- `html_to_pptx_converter.py` - Python script that converts HTML to PPTX
- `verify_pptx.py` - Verification script to check PPTX content

## Features

The generated PPTX file contains:

- **Single slide layout** matching the HTML poster design
- **All text content** from the original HTML poster
- **Color-coded sections** matching the HTML design:
  - Green for LLM4Verilog Generation (#4CAF50)
  - Red for LLM4Security (#FF5722) 
  - Blue for LLM4C2HLS (#2196F3)
- **Proper formatting** with emojis, bullet points, and hierarchy
- **Background design** approximating the HTML gradient and layout

## Content Included

1. **Header**: Title and subtitle with blue gradient background
2. **Repository Info**: GitHub repository link
3. **Featured Submodules**: AutoChip, Security Assertions, C2HLSC
4. **Three Main Sections**:
   - 🔧 LLM4Verilog Generation (5 projects)
   - 🛡️ LLM4Security (5 projects)
   - ⚡ LLM4C2HLS (3 projects)
5. **Statistics**: Project counts and key metrics

## Usage

To regenerate the PPTX file:

```bash
python3 html_to_pptx_converter.py
```

To verify the content:

```bash
python3 verify_pptx.py
```

## Dependencies

- python-pptx
- beautifulsoup4

The generated `poster.pptx` file can be opened in Microsoft PowerPoint, Google Slides, or any compatible presentation software.