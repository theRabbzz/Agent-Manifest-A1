# Entry point CLI script
import argparse
from agent_core.llm import generate_text
from agent_core.vision import analyze_image
from agent_core.audio import transcribe_audio

def main():
    parser = argparse.ArgumentParser(description='Run the Multimodal AI Agent')
    parser.add_argument('--text', type=str, help='Text prompt for the LLM')
    parser.add_argument('--image', type=str, help='Path to image file')
    parser.add_argument('--audio', type=str, help='Path to audio file')
    args = parser.parse_args()

    if args.text:
        print(generate_text(args.text))
    if args.image:
        print(analyze_image(args.image))
    if args.audio:
        print(transcribe_audio(args.audio))

if __name__ == '__main__':
    main()
