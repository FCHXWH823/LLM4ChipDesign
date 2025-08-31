#!/usr/bin/env python3
"""
LLM4Hardware Introduction Video Generator

This script generates an introduction video for the LLM4Hardware repository
based on the content from the poster and README file.
"""

import cv2
import numpy as np
import moviepy
from moviepy import ImageClip, concatenate_videoclips
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
import sys

class IntroVideoGenerator:
    def __init__(self, width=1920, height=1080, fps=30):
        self.width = width
        self.height = height
        self.fps = fps
        self.background_color = (15, 23, 42)  # Dark blue background
        self.accent_color = (59, 130, 246)    # Blue accent
        self.text_color = (255, 255, 255)    # White text
        self.highlight_color = (34, 197, 94) # Green highlight
        
    def create_text_frame(self, title, subtitle="", content="", duration=4):
        """Create a frame with title, subtitle, and content text"""
        # Create PIL image
        img = Image.new('RGB', (self.width, self.height), self.background_color)
        draw = ImageDraw.Draw(img)
        
        try:
            # Load fonts (fallback to default if not available)
            title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 72)
            subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 48)
            content_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 36)
        except:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            content_font = ImageFont.load_default()
        
        y_pos = 150
        
        # Draw title
        if title:
            # Wrap title text
            wrapped_title = textwrap.fill(title, width=30)
            for line in wrapped_title.split('\n'):
                bbox = draw.textbbox((0, 0), line, font=title_font)
                text_width = bbox[2] - bbox[0]
                x_pos = (self.width - text_width) // 2
                draw.text((x_pos, y_pos), line, fill=self.text_color, font=title_font)
                y_pos += 90
            y_pos += 50
        
        # Draw subtitle
        if subtitle:
            wrapped_subtitle = textwrap.fill(subtitle, width=40)
            for line in wrapped_subtitle.split('\n'):
                bbox = draw.textbbox((0, 0), line, font=subtitle_font)
                text_width = bbox[2] - bbox[0]
                x_pos = (self.width - text_width) // 2
                draw.text((x_pos, y_pos), line, fill=self.accent_color, font=subtitle_font)
                y_pos += 60
            y_pos += 40
        
        # Draw content
        if content:
            wrapped_content = textwrap.fill(content, width=60)
            for line in wrapped_content.split('\n'):
                bbox = draw.textbbox((0, 0), line, font=content_font)
                text_width = bbox[2] - bbox[0]
                x_pos = (self.width - text_width) // 2
                draw.text((x_pos, y_pos), line, fill=self.text_color, font=content_font)
                y_pos += 50
        
        # Add decorative elements
        self.add_decorative_elements(draw)
        
        # Convert PIL image to numpy array
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        return frame, duration
    
    def add_decorative_elements(self, draw):
        """Add decorative elements to the frame"""
        # Add top and bottom accent lines
        line_thickness = 8
        draw.rectangle([0, 50, self.width, 50 + line_thickness], fill=self.accent_color)
        draw.rectangle([0, self.height - 50 - line_thickness, self.width, self.height - 50], fill=self.accent_color)
        
        # Add corner decorations
        corner_size = 100
        # Top left
        draw.rectangle([50, 50, 50 + corner_size, 50 + line_thickness], fill=self.highlight_color)
        draw.rectangle([50, 50, 50 + line_thickness, 50 + corner_size], fill=self.highlight_color)
        
        # Top right
        draw.rectangle([self.width - 50 - corner_size, 50, self.width - 50, 50 + line_thickness], fill=self.highlight_color)
        draw.rectangle([self.width - 50 - line_thickness, 50, self.width - 50, 50 + corner_size], fill=self.highlight_color)
    
    def create_research_areas_frame(self, areas, title="Research Areas", duration=6):
        """Create a frame showing research areas"""
        img = Image.new('RGB', (self.width, self.height), self.background_color)
        draw = ImageDraw.Draw(img)
        
        try:
            title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
            area_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
        except:
            title_font = ImageFont.load_default()
            area_font = ImageFont.load_default()
        
        # Draw title
        bbox = draw.textbbox((0, 0), title, font=title_font)
        text_width = bbox[2] - bbox[0]
        x_pos = (self.width - text_width) // 2
        draw.text((x_pos, 100), title, fill=self.accent_color, font=title_font)
        
        # Draw research areas in columns
        y_start = 250
        col_width = self.width // 2
        
        for i, area in enumerate(areas):
            col = i % 2
            row = i // 2
            
            x_pos = 100 + col * col_width
            y_pos = y_start + row * 80
            
            # Draw bullet point
            draw.ellipse([x_pos - 20, y_pos + 10, x_pos - 5, y_pos + 25], fill=self.highlight_color)
            
            # Draw area text
            draw.text((x_pos + 20, y_pos), area, fill=self.text_color, font=area_font)
        
        self.add_decorative_elements(draw)
        
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        return frame, duration
    
    def generate_intro_video(self):
        """Generate the complete introduction video"""
        clips = []
        
        # Title slide
        title_frame, duration = self.create_text_frame(
            title="Generative AI for Chip Design",
            subtitle="LLM4Hardware Research Collection",
            content="Advancing Hardware Design through Large Language Models",
            duration=5
        )
        clips.append(ImageClip(title_frame, duration=duration))
        
        # Overview slide
        overview_frame, duration = self.create_text_frame(
            title="Overview",
            subtitle="Bridging AI and Hardware Design",
            content="This collection presents cutting-edge research in applying Large Language Models to various aspects of chip design, from Verilog generation to verification and security.",
            duration=6
        )
        clips.append(ImageClip(overview_frame, duration=duration))
        
        # Research areas
        research_areas = [
            "Verilog Code Generation",
            "Hierarchical Design Methods", 
            "Formal Verification Integration",
            "Testbench Generation",
            "Security Assertion Creation",
            "Software-to-Hardware Translation",
            "Circuit Optimization",
            "Hardware IP Analysis",
            "Analog Circuit Design",
            "Design Space Exploration"
        ]
        
        areas_frame, duration = self.create_research_areas_frame(research_areas, duration=8)
        clips.append(ImageClip(areas_frame, duration=duration))
        
        # Key innovations slide
        innovations_frame, duration = self.create_text_frame(
            title="Key Innovations",
            subtitle="Transforming Hardware Design",
            content="• Hierarchical prompting for complex modules\n• Reasoning-based code generation\n• CNF-guided synthesis\n• RAG-enhanced verification\n• Automated testbench creation",
            duration=7
        )
        clips.append(ImageClip(innovations_frame, duration=duration))
        
        # Applications slide
        applications_frame, duration = self.create_text_frame(
            title="Applications",
            subtitle="Real-World Impact",
            content="From simple logic gates to complex processors, our tools enable automated design, verification, and optimization across the entire hardware development lifecycle.",
            duration=6
        )
        clips.append(ImageClip(applications_frame, duration=duration))
        
        # Transition to modules slide
        transition_frame, duration = self.create_text_frame(
            title="Exploring the Research",
            subtitle="Deep Dive into Three Key Areas",
            content="Let's explore three major research directions that are revolutionizing how we approach hardware design with AI.",
            duration=5
        )
        clips.append(ImageClip(transition_frame, duration=duration))
        
        # Combine all clips
        final_video = concatenate_videoclips(clips, method="compose")
        
        return final_video

def main():
    """Main function to generate the introduction video"""
    print("Generating LLM4Hardware Introduction Video...")
    
    # Create output directory if it doesn't exist
    output_dir = "/home/runner/work/LLM4Hardware/LLM4Hardware/videos"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate video
    generator = IntroVideoGenerator()
    video = generator.generate_intro_video()
    
    # Save video
    output_path = os.path.join(output_dir, "LLM4Hardware_Introduction.mp4")
    print(f"Saving video to: {output_path}")
    
    # Write video file
    video.write_videofile(
        output_path,
        fps=30,
        codec='libx264',
        audio=False,
        temp_audiofile_path="/tmp/temp-audio.m4a",
        remove_temp=True
    )
    
    print(f"Introduction video successfully created: {output_path}")
    print(f"Duration: {video.duration:.1f} seconds")

if __name__ == "__main__":
    main()