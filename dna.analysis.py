sequence = "ATGCGTAGCTAGCTAGCTAG"

sequence = sequence.upper()

length = len(sequence)

A = sequence.count("A")
T = sequence.count("T")
G = sequence.count("G")
C = sequence.count("C")

gc_content = ((G + C) / length) * 100
at_content = ((A + T) / length) * 100

print("DNA Sequence Analysis")
print("---------------------")
print("Sequence:", sequence)
print("Sequence Length:", length)
print("A:", A)
print("T:", T)
print("G:", G)
print("C:", C)
print("GC Content: {:.2f}%".format(gc_content))
print("AT Content: {:.2f}%".format(at_content))