import argparse
import os
from converter.video_to_audio import convert_video_to_audio

def main():
    parser = argparse.ArgumentParser(description="Convert video to audio (MP3).")
    parser.add_argument("video_path", help="Path to the video file")
    parser.add_argument("-o", "--output", default=".", help="Output directory (default: current directory)")

    args = parser.parse_args()

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    result = convert_video_to_audio(args.video_path, args.output)
    print(f"Output: {result}")

if __name__ == "__main__":
    main()