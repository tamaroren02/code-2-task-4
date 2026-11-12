import random
#functions#
def rand_seq(length,group_amino_acids):
    list_of_amino_acids=[]
    for i in range(length):
        placement=random.randrange(0,len(group_amino_acids))
        list_of_amino_acids.append(group_amino_acids[placement])
    return list_of_amino_acids

def random_seq(num_of_seq,file_seq):
    counter=0
    for i in range(num_of_seq):
        counter+=1
        #hydrophobic amino acids
        hydrophobic_options=["A", "V", "L", "I", "P", "F", "M", "W", "G", "C"]
        hydrophobic_length=74 #metionin is also included so we will use 74 insted pf 75
        hydrophobic_sequence=rand_seq(hydrophobic_length,hydrophobic_options)

        #polar amino acids
        polar_options=["N", "Q", "S", "T", "Y"]
        polar_length=45
        polar_sequence=rand_seq(polar_length,polar_options)

        #positively charged amino acids
        positively_charged_options=["K", "R", "H"]
        positively_charged_length=15
        positively_charged_sequence=rand_seq(positively_charged_length,positively_charged_options)

        #negatively charged amino acids
        negatively_charged_options=["D", "E"]
        negatively_charged_length=15
        negatively_charged_sequence=rand_seq(negatively_charged_length,negatively_charged_options)

        #final amino acid sequence
        metionin=["M"]
        unshuffled_seq=negatively_charged_sequence+positively_charged_sequence+polar_sequence+hydrophobic_sequence
        random.shuffle(unshuffled_seq)
        final_seq=metionin+unshuffled_seq
        file_seq.write(">Rand_Prot"+str(counter)+"\n"+"".join(final_seq)+"\n"+"\n")
    return file_seq

#####main program######
x=int(input("Please indicate how many random protein sequences you need (1-1000)"))
Out_RandProtSeq = open('results/Out_RandProtSeq.txt', 'w')
user_random_seq=random_seq(x,Out_RandProtSeq)
Out_RandProtSeq.close()

