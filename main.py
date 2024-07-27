from DataFetcher import NucleotideQuery

if __name__ == '__main__':

    NQ = NucleotideQuery(gene_id="NM_005228.4")
    NQ.fetch_gene()
    NQ.print_sequence()
    NQ.count_codons()
