def transcribe_dna_to_rna(dna_sequence: str) -> str:
    """
    Transcribes a DNA sequence into an RNA sequence by replacing 
    all instances of Thymine (T) with Uracil (U).
    Accommodates both uppercase and lowercase sequences.
    """
    # Hardcoded direct character mapping for the replacement
    return dna_sequence.replace('T', 'U').replace('t', 'u')

# --- Test Cases ---
if __name__ == "__main__":
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

    # Test 3: Complex mixed strand
    dna_sample_3 = "GATTACA"
    rna_result_3 = transcribe_dna_to_rna(dna_sample_3)
    print(f"DNA Input  3: {dna_sample_3}")
    print(f"RNA Output 3: {rna_result_3}")