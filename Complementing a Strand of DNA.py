s = "CTAGTCAATTAGTTTTATTTATCGGACTCCCAGGGGGTTTCCATTCACTAGGCAAATCCATGGAAGAGGAGATTCTTACGTAAAGCCAATCATGAGCCACGATTGGTGCTCGAGGGTGTAAATACCCGCAATGACTCAGAGCCCCTATTTCAAGACCGTTGTCCCAGAGATGGAGGCTAGATTGTATCGAGTTGACTTTGATGAACTTACTGCAGAACGCCTAAATTAAACCTGAGGTCTCATTCTGAGCGGCTTGGTTCGGCGGTCAGAAACATTTATCTATTGGTGATTATTAGTTGACGTACTTTAATGTTCTTCGCCGCACGCATAATAGTGCTTACTACGGACAAGCTGGTCAGCGGTCTCGCCCAACAGATCCAAATAGCCATCATAAAAACTATCTCTAGCAATGCCCCCATGGTGGAGAGGCACGGTACTACCTCGTTACGCCTAAAGCTCTCGTGCCGAGATTTTCCGTTGGAACCTAGGCAGTGCCTGCACAGCTTAGACACAGCCTCCGACCGCGGGACCTACAAATCCCCATGACCAGCAGTAGCTAATCCGACGACTTACACCGATCAGCGCGCGTCCTTTCGTCCCTAGGACGGAAATTTCAACTCCGTTGGTGAGCTCTCCGCGGCATATGGTCGTTTCCAGACAGGCACGACATACGCACTCTAGGAGCGCACGTTATGTTACGAACTAATGGGTAGTCTTACAGCCCGCCGACCGTCTTTCGTTTCGGCGTCATTTACCCATCATGAAAGCGAGCCAAAACAGGGCTGTGCCCATGCGAATGCAGGAGCCAGGAAATCGATTTCCTCTCTTCACTTACAAACTTACACCACGTGTGGGAGCGAGTTCCGATACTTGCACCGGATCAGAGCTCCCGTCTCCGCCCGGAGAATCAGGAAAATATGTGATGTTTCCTCCTGCCAGACGTGTGAAACCAAATGGCGCCTCTACT"

sc = s.replace("A","X")
sc = sc.replace("T","A")
sc = sc.replace("X","T")

sc = sc.replace("C","X")
sc = sc.replace("G","C")
sc = sc.replace("X","G")

sc = sc[::-1]

print sc
