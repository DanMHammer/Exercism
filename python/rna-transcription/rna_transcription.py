def to_rna(dna_strand):
    '''
    Process input DNA sequence and return RNA sequence with the following changes
    `G` -> `C`
    `C` -> `G`
    `T` -> `A`
    `A` -> `U`
    '''
    #empty rna_strand
    rna_strand = ""
    #dictionary of DNA to RNA conversions
    rna_dict = {"G":"C", "C":"G", "T":"A", "A":"U"}
    #convert dna_strand to uppercase
    dna_strand = dna_strand.upper()
    #iterate through characters
    for char in dna_strand:
        #raise a descriptive ValueError if user did not enter valid bases
        if char not in ["G", "C", "T", "A"]:
            raise ValueError("You did not enter valid DNA nucleotides G, C, T, and A")
        #else append the correct nucleotide to the RNA sequence
        else:
            rna_strand += rna_dict.get(char)

    return rna_strand
