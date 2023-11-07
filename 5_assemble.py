import os, argparse

from pydub import AudioSegment


def generate_audiobook(args):
    combined = AudioSegment.empty()

    for filename in os.listdir(args.speech_folder):
        if filename.endswith('.mp3'):
            print(f"Adding: {filename}")
            audio_segment = AudioSegment.from_mp3(os.path.join(args.speech_folder, filename))
            combined += audio_segment

    combined.export(args.output_audiobook, format="mp3")

    print(f"Output file: {args.output_audiobook}")


def main():
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="Get the cast of characters.")
    parser.add_argument(
        '--speech-folder', 
        type=str,
        nargs='?',  # Indicates the argument is optional
        default='speech',  # Default folder name
        help="Folder of output speech mp3."
    )
    parser.add_argument(
        '--output-audiobook', 
        type=str,
        nargs='?',  # Indicates the argument is optional
        default="output_audiobook.mp3",
        help="Output file."
    )

    # Parse the command line arguments
    args = parser.parse_args()

    generate_audiobook(args)

if __name__ == "__main__":
    main()
