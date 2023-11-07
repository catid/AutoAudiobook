import os, argparse, json, shutil

def cast_actors(args):
    characters = []

    for filename in os.listdir(args.assigned_folder):
        if filename.endswith('.json'):
            with open(os.path.join(args.assigned_folder, filename), 'r') as file:

                try:
                    content = file.read()

                    passage = json.loads(content)

                    for quote in passage:
                        name = quote["name"].lower()
                        characters.append(name)

                except Exception as e:
                    print(f"Failed to process {filename}: {e}")

    unique_characters = list(set(characters))

    actors = ['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer']

    casting = []
    for i, character in enumerate(unique_characters):
        actor = actors[i % len(actors)]
        casting.append({'character': character, 'actor': actor})

    with open(args.casting_file, 'w', encoding='utf-8') as casting_file:
        casting_file.write(json.dumps(casting))


def main():
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="Get the cast of characters.")
    parser.add_argument(
        '--assigned-folder', 
        type=str,
        nargs='?',  # Indicates the argument is optional
        default='assigned',  # Default folder name
        help="Folder of assigned JSON files."
    )
    parser.add_argument(
        '--casting_file', 
        type=str,
        nargs='?',  # Indicates the argument is optional
        default='casting.json',
        help="Casting file."
    )

    # Parse the command line arguments
    args = parser.parse_args()

    cast_actors(args)

if __name__ == "__main__":
    main()
