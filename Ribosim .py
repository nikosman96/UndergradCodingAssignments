'''----------------------------------------Ribosim 2017-----------------------------------------------'''

#Messages 
welcome_msg = 'Welcome to Ribosim 2017\n'
goodbye_msg = '\nThank you for using Ribosim2017.'
instructions = 'This a ribosome simulator that can translate your FASTA sequence of choice with 6 reading frames.'
file_error = '''Error: File name given doesn't appear to exist, please chose again.'''
general_error = 'Error: Answer not valid, please choose again.'  
number_error = 'Error: Answer given does not seem to be a number, please choose a valid sequence length.'  
separator =  '----:----|'
additional = 'Additional information about your sequence\n'
gc_rich_msg = 'G-C content/ratio percentage:\n'

print welcome_msg
print instructions

#custom error for wrong file name input
while True:
    #userinput 1: ask for sequence
    file_name = raw_input('Insert full file name including file extension: ')
    if file_name == '':
        file_name = 'myoglobin.seq'
    try:
        with open(file_name,"r") as f:
            seq = ''.join(f.read().splitlines()[1:]) #Removing first line, joining together
        break
    except IOError:
        print ('Error: File name "{}" does not appear to exist, please chose again.').format(file_name)

print ('''Opened "{}".''').format(file_name)
      
#userinput 2: ask for 1/3 code
amino_code = raw_input('Translate to 1 or 3 letter Amino Acid symbol(s)? [1/3]: ')

# creating a dictionary using custom codon table
codon_dict = {}

with open('Codon_Table_2.txt') as file:
       for c in file.readlines():
            if amino_code in ('1','one',''): #1 letter aa code is the default
                        cs = c.split()
                        codon_dict[cs[0]] = cs[1] #first and second columns used
                        s = '  ' #space in printing 
                        
            elif amino_code in ('3','three'):
                        cs = c.split()
                        codon_dict[cs[0]] = cs[2] #first and third columns used
                        s = '' #space in print
                        
            else:
                print general_error           
                amino_code = raw_input('\nTranslate to one or three letter Amino Acid symbol? [1/3]: ')

# otherwise print will say translating to null letter
if amino_code == '':
   amino_code = '1'
 


'''---------------------------------------------Functions--------------------------------------------'''
    
#Function 1: GC content    
def gc_richness(seq):
    g_content = seq.count('G')
    c_content = seq.count('C')
    a_content = seq.count('T')
    t_content = seq.count('A')
    total_content = int(g_content) + int(c_content) + int(a_content) + int(t_content)
    gc_content = int(g_content) + int(c_content)
    gc_richness =  float(gc_content) / total_content #must be a float otherwise answer truncated as integer
    gc_rich_percent = gc_richness * 100 
    gc_rich_rounded = round(gc_rich_percent) #rounding up final result

    return gc_rich_rounded

#Function 2: a function to convert RNA to DNA
def rna_converter(seq):
    DNA = seq.replace ('U','T')

    return DNA

#Function 3: Translating the sense strand
def translate(seq):
    codons = [seq[i:i+3].lower() for i in range(0, len(seq), 3)] #using range(start, stop, step) for the RFs
    amino_acids = []
    for c in codons:
        amino_acids.append(codon_dict.get(c,'-')) #if no codon is left print dash to let the user know

    return amino_acids

#keep a copy of original sequence unaltered as a string
seq_og = []
seq_og.append(seq)

seq_og = ''.join(seq_og)

# call rna_converter to convert RNA sequence if necessary
seq = rna_converter(seq)

#Function 4: Creating the complementary anti-sense strand
def make_anti_seq(seq):

    transcribe_dict = {'T':'A', 'A':'T', 'G':'C','C':'G'} # antisense

    anti_seq = []
    for a in seq: # for every character in the original string
        anti_seq.append(transcribe_dict.get(a, '-')) # if input is not ATGC show as dash

    anti_seq = ''.join(anti_seq)

    return anti_seq

#Function 5: Creating the anti-sense strand if RNA
def rna_antiseq(seq_og):
    rna_dict = {'A':'U','U':'A', 'G':'C','C':'G'} # antisense

    anti_seq = []
    for b in seq_og: # for every character in the original string
        anti_seq.append(rna_dict.get(b, '-')) 

    anti_seq = ''.join(anti_seq)

    return anti_seq


#User input 3: ask if DNA or RNA to know which codon dictionary to use
dna_or_rna = raw_input('Translate a DNA or RNA sequence? [D/r]:').lower()

#reverse for backwards frames
anti_seq_reversed = (make_anti_seq(seq)[::-1]) #instead of reading backwards, reverse complement  and read forwards

#anti_seq_reversed is the same no matter which outcome (DNA or RNA)

# While loop with if statement depending on raw_input
while True:
    if dna_or_rna in ('d','dna',''):
        dna_or_rna = 'DNA'
         # call anti_seq to create anti sense strand
        anti_seq = make_anti_seq(seq) 
        break
    elif dna_or_rna in ('r','rna'):
        dna_or_rna = 'RNA'
        anti_seq = rna_antiseq(seq_og) #calling rna_abtiseq to create anti sense rna strand
        break
    else:
        print general_error
        dna_or_rna = raw_input('Translate a DNA or RNA sequence? [D/r]:').lower()

#Function 7: create foreward RF  
def FRF_maker(seq): 
#calling translate and modifying it for each reading frame on SENSE
    RF1 = translate(seq) #translates entire sequence from character 0
    RF2 = translate(seq[1:]) #translate from character 1 (second letter) and on
    RF3 = translate(seq[2:]) #from character 2

    return RF1, RF2, RF3

#Function 8: create backward RF
def BRF_maker(anti_seq_reversed): 
#calling translate and modifying it for each reading frame on ANTI sense
    RF6 = translate(anti_seq_reversed[2:])[::-1] # [::-1] inverses the sequence
    RF5 = translate(anti_seq_reversed[1:])[::-1] 
    RF4 = translate(anti_seq_reversed)[::-1]  
    
    return RF6, RF5, RF4

#Default labels for print output
F1 = 'F1'
F2 = 'F2'
F3 = 'F3'
F6 = 'F6'
F5 = 'F5'
F4 = 'F4'

                     
#While loop offers user choice on length of sequence
while True:
    entire = raw_input('Read entire sequence [Y/n]:').lower() #user input 4: read all or no?
    if entire in ('yes','y',''): #User reads entire sequence

        length = len(seq)
        break
    
#User specifies desired base length    
    elif entire in ('no','n'): 
        while True:
            length = raw_input('Number of base pairs to read [e.g. 60]:') #user input 5: how long?
            #custom error if not a number
            try:
                length = int(length)
                break
            except ValueError:       
                print number_error
# length = raw_input('Number of base pairs to read [e.g. 60]:')
        
#for loop with two ranges: one for the Reading Frames output and one for the actual sequence output 
#Amino acid output must be in steps of 20, length of user's choice
#Sequence output must be in steps of 60, length of user's choice

        for i, j in zip(range(0,len(translate(seq[0:int(length)])),20), range(0,len(seq[0:int(length)]),60)):

#modifications for shortened sequences
            seq_og = seq_og[0:int(length)] #slice until length desired
            anti_seq = anti_seq[0:int(length)] 
                        
#Redifining seq and anti_seq_reversed
            anti_seq_reversed = anti_seq_reversed[0:int(length)] 
            seq = seq[0:int(length)]
        break

    else:
        print general_error

'''----------------------------------------Reading Frames----------------------------------------------------'''
 

while True: #User input 6: which frames to translate
    RF = raw_input('Number of reading frames [A/b/c]?\n(A) All\n(B) F1-F3\n(C) F4-F6\n: ').lower() 
    if RF in ('a','all',''): #use all reading frames
        RF = 'F1-F6'
        RF1, RF2, RF3 = FRF_maker(seq) #calling FRF maker
        RF6, RF5, RF4 = BRF_maker(anti_seq_reversed) #calling BRF maker

        #Reading Frame labels remain unchanged
        
        break
    elif RF in ('b','f1-f3'):
        RF = 'F1-F3'
        RF1, RF2, RF3 = FRF_maker(seq) #call FRF make
        RF6, RF5, RF4 = BRF_maker('') #but BRF should not translate anything / should not appear at all
        
        F6 = '' # and its labels should be null
        F5 = ''
        F4 = ''
        
        break
    
    elif RF in ('c','f4-f6'): #vice versa
        RF = 'F4-F6'
        RF1, RF2, RF3 = FRF_maker('')
        RF6, RF5, RF4 = BRF_maker(anti_seq_reversed)
        
        F1 = ''
        F2 = ''
        F3 = ''
       
        break
    else:
        print general_error
   #     RF = raw_input('Number of reading frames?\n[A All/B F1-F3/C F4-F6]: ')
   #     RF = RF.lower()
        

                 
'''-------------------------------Printing Output and Writing in new File ----------------------------------------'''

for i, j in zip(range(0,len(translate(seq[0:int(length)])),20), range(0,len(seq[0:int(length)]),60)):
    row_length = len(seq_og[j:j+60])
    row_length_end = j + int(row_length)
    #RF 1,2,3
    print '  {}{}{}'.format(s.join(RF1[i:i+20]), ' '*7,F1) #join amino acid output in steps of 20
    print '   {}{}{}'.format(s.join(RF2[i:i+20]),' '*6,F2)
    print '    {}{}{}'.format(s.join(RF3[i:i+20]),' '*5,F3)
    print '{} {} {}'.format(str(j+1),seq_og[j:j+60],row_length_end) #print numbering of SENSE sequence at beginning of row, the sequence itself in steps of 20, and length at the end of the row
    print '   '+separator*(row_length/10)
    #RF -1,-2,-3
    print '{} {} {}'.format(str(j+1),anti_seq[j:j+60],row_length_end) #for ANTI sense
    print '     {}{}{}'.format(s.join(RF6[i:i+20]),' '*5,F6)
    print '    {}{}{}'.format(s.join(RF5[i:i+20]),' '*6,F5)
    print '   {}{}{}'.format(s.join(RF4[i:i+20]),' '*7,F4)
    print '\n\n\n' # 3 prints after each set
   
    
print ('{} sequence of length {} bp was translated to {} letter amino acid symbol(s), using reading frames {}.\n').format(dna_or_rna, length, amino_code, RF)
print ('Your sequence has been successfully translated and saved as: {}_bp_translated_{} in the same directory as your original file.\n').format(length, file_name)
print additional
print gc_rich_msg
print gc_richness(seq)
print goodbye_msg
      
with open('{}_bp_translated_{}'.format(length, file_name)
, 'w') as f:
    for i, j in zip(range(0,len(translate(seq[0:int(length)])),20), range(0,len(seq[0:int(length)]),60)):
        row_length = len(seq_og[j:j+60])
        row_length_end = j + int(row_length)

        f.write('  {}{}{}\n'.format(s.join(RF1[i:i+20]), ' '*7,F1))
        f.write( '   {}{}{}\n'.format(s.join(RF2[i:i+20]),' '*6,F2))
        f.write( '    {}{}{}\n'.format(s.join(RF3[i:i+20]),' '*5,F3))
        f.write( '{} {} {}\n'.format(str(j+1),seq_og[j:j+60],row_length_end))
        f.write( '   '+separator*(row_length/10)+'\n')
        #RF -1,-2,-3
        f.write( '{} {} {}\n'.format(str(j+1),anti_seq[j:j+60],row_length_end))
        f.write( '    {}{}{}\n'.format(s.join(RF6[i:i+20]),' '*5,F6))
        f.write( '   {}{}{}\n'.format(s.join(RF5[i:i+20]),' '*6,F5))
        f.write( '  {}{}{}\n'.format(s.join(RF4[i:i+20]),' '*7,F4))
        f.write( '\n\n\n') # 3 prints after each set

                  
'''----------------------------------------------------- Fin --------------------------------------------------'''

#Acknowledgements: 
#I would like to thank Laurence, Graeme, and Sarah.
#Check out other cool software by nam36: Snailsim2017    

    