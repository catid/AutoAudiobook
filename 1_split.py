import os, shutil, argparse, unicodedata

def chunk_book(args):
    chunks = []
    current_chunk = ''
    
    with open(args.file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        # Check if the line is a new paragraph
        if line.startswith(('   ', '\t')) or (current_chunk.endswith('\n\n') and not line.startswith(' ')):
            if len(current_chunk) >= args.max_split_size:
                chunks.append(current_chunk)
                current_chunk = line
            else:
                current_chunk += line
        else:
            current_chunk += line

    # Add the last chunk if it's not empty
    if current_chunk:
        chunks.append(current_chunk)

    if os.path.exists(args.output_folder):
        shutil.rmtree(args.output_folder)
    os.makedirs(args.output_folder)

    for i, chunk in enumerate(chunks):
        chunk_filename = os.path.join(args.output_folder, f'chunk_{i+1}.txt')
        with open(chunk_filename, 'w', encoding='utf-8') as chunk_file:
            chunk_file.write(chunk)
            print(f"Chunk written: {len(chunk)} characters")
    return chunks

def main():
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="Split a book into sections based on paragraph breaks.")
    parser.add_argument(
        'file_path', 
        type=str, 
        nargs='?',  # Indicates the argument is optional
        default='book.txt',  # Default file name
        help="The file path of the book text to chunk. Defaults to 'book.txt'."
    )
    parser.add_argument(
        '--output-folder', 
        type=str, 
        nargs='?',  # Indicates the argument is optional
        default='splits',  # Default folder name
        help="The text splits from the input book."
    )
    parser.add_argument(
        '--max-split-size', 
        type=int,
        nargs='?',  # Indicates the argument is optional
        default=4000,  # Default file name
        help="Size of splits in characters."
    )

    # Parse the command line arguments
    args = parser.parse_args()

    # Chunk the book and print the number of chunks
    book_chunks = chunk_book(args)
    print(f"Number of chunks created: {len(book_chunks)}")

if __name__ == "__main__":
    main()
