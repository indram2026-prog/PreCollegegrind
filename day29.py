import os

def transcribe_dna_to_rna(dna_sequence: str) -> str:
    """
    Transcribes a DNA sequence into an RNA sequence by replacing 
    all instances of Thymine (T) with Uracil (U).
    Accommodates both uppercase and lowercase sequences.
    """
    # Hardcoded direct character mapping for the replacement
    return dna_sequence.replace('T', 'U').replace('t', 'u')

def process_dna_file(input_filename: str, output_filename: str) -> None:
    """
    Day 6 Feature: Reads DNA sequences from a file, validates them,
    transcribes them to RNA, and writes the results to an output file.
    Handles key edge cases such as missing files, empty files, and invalid characters.
    """
    # --- Edge Case 1: Missing Input File ---
    if not os.path.exists(input_filename):
        print(f"Error: The input file '{input_filename}' does not exist.")
        return

    try:
        with open(input_filename, 'r') as infile:
            # Read lines and strip trailing/leading whitespaces/newlines
            lines = [line.strip() for line in infile.readlines()]

        # --- Edge Case 2: Empty Input File ---
        if not lines or all(not line for line in lines):
            print(f"Warning: The input file '{input_filename}' is empty. Nothing to transcribe.")
            return

        valid_dna_chars = set("ATCGatcg")
        output_lines = []

        for index, line in enumerate(lines, start=1):
            # Skip empty lines within the file smoothly
            if not line:
                continue
            
            # --- Edge Case 3: Invalid Characters (Non-DNA Data) ---
            # Checks if any character in the line is not A, T, C, or G
            if not set(line).issubset(valid_dna_chars):
                print(f"Skipping Line {index}: Contains invalid DNA characters -> '{line}'")
                output_lines.append(f"Line {index} Error: Invalid DNA sequence.")
                continue

            # If valid, perform the transcription
            rna_sequence = transcribe_dna_to_rna(line)
            output_lines.append(rna_sequence)

        # Write the transcribed results to the output file
        with open(output_filename, 'w') as outfile:
            for line in output_lines:
                outfile.write(line + '\n')
        
        print(f"Success! Transcribed sequences saved to '{output_filename}'.")

    except IOError as e:
        print(f"An I/O error occurred while handling the files: {e}")


# --- Test Cases ---
if __name__ == "__main__":
    print("--- Running Original String Tests ---")
    # Test 1: Standard uppercase sequence
    dna_sample_1 = "ATGCGTACGTAACGTT"
    rna_result_1 = transcribe_dna_to_rna(dna_sample_1)
    print(f"DNA Input  1: {dna_sample_1}")
    print(f"RNA Output 1: {rna_result_1}\n")

    # Test 2: Standard lowercase sequence
    dna_sample_2 = "atgcgtacgtaacgtt"
    rna_result_2 = transcribe_dna_to_rna(dna_sample_2)
    print(f"DNA Input  2: {dna_sample_2}")
    print(f"RNA Output 2: {rna_result_2}\n")


    print("--- Running Day 6 File I/O & Edge Case Tests ---")
    
    # Setup filenames for testing
    test_input = "sample_dna.txt"
    test_output = "output_rna.txt"

    # Creating a dummy input file with valid strings, blank lines, and an invalid string
    print(f"Creating a temporary test file: {test_input}...")
    with open(test_input, 'w') as f:
        f.write("GATTACA\n")          # Valid Uppercase
        f.write("atgcatgc\n")         # Valid Lowercase
        f.write("\n")                 # Edge Case: Blank line
        f.write("ATGCXYZGATTACA\n")   # Edge Case: Invalid characters (X, Y, Z)

    # Run the file processing function
    process_dna_file(test_input, test_output)

    # Test Case: Missing file scenario
    print("\nTesting missing file edge case:")
    process_dna_file("non_existent_file.txt", "should_not_exist.txt")