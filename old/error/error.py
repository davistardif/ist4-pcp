import itertools

class Code:
    def __init__(self, words_in):
        """
        words_in is a list of binary strings
        """
        self.words = words_in
        self.n = len(words_in)
        self.l = len(words_in[0])
    def __str__(self):
        """
        returns the list of codewords in code
        """
        return str(self.words)
    def delete(self, d):
        """
        d: a list of n indices
        deletes the d[i]-th entry from all the code words
        """
        new_words = [self.words[i][:d[i]] + self.words[i][d[i]+1:] for i in \
            range(0, self.n)]
        return new_words
    def single_deletion_correcting(self, show_work):
        """
        show_work is a boolean whether to show work or not
        checks if the code is single deletion correcting
        """
        if show_work: print "checking", str(self) + ":"
        for subset in itertools.product(range(0,self.l), repeat=self.n):
            if show_work:
                print "-deletion of", subset, "th entries", \
                    self.delete(subset)
            if len(set(self.delete(subset))) != self.n:
                return False
        return True
    def single_insertion_correcting(self, show_work):
        """
        show_work is a boolean whether to show work or not
        same as single_deletion_correcting by iff
        """
        return self.single_deletion_correcting(show_work)

def gen_codes(l, n):
    """
    l is length of each words
    n is how many words
    """
    code_words = [bin(i)[2:] for i in range(2**(l-1)+1,2**l)]
    codes = []
    for subset in itertools.combinations(code_words, n):
        codes.append(Code(list(subset)))
    return codes



code_f_i_1 = Code(['101','111'])
code_f_i_2 = Code(['000','101'])
codes_f_i = gen_codes(3,3)



code_f_ii = Code(['0000','0110','1010'])
codes_f_ii = gen_codes(4,4)

code_f_iii = Code(['00000','10001','01010','11100','00111'])
codes_f_iii = gen_codes(5,6)

print
print
print
print "part (f)(i)"
print "Is {101,111} a single deletion correcting code?"
print code_f_i_1.single_deletion_correcting(True)
print "Is {000,101} a single deletion correcting code?"
print code_f_i_2.single_deletion_correcting(True)
print "Is there a length 3 code with more than 2 codewords?"
print True in [code.single_deletion_correcting(True) for code in codes_f_i]
print
print
print
print "part (f)(ii)"
print "Is {0000,0110,1010} a single deletion correcting code?"
print code_f_ii.single_deletion_correcting(True)
print "Is there a single deletion correcting code of length 4 with 4 " + \
    "codewords?"
results = [code.single_deletion_correcting(False) for code in codes_f_ii]
print True in results
print "(done computationally, the full computation will not be printed)"
print
print
print
print "part (f)(iii)"
print "Is {00000,10001,01010,11100,00111} a single deletion correcting code?"
print code_f_iii.single_deletion_correcting(False)
print "(done computationally, the full computation will not be printed)"
print "Is there a single deletion correcting code of length 5 with 6 " + \
    "codewords?"
results = [code.single_deletion_correcting(False) for code in codes_f_iii]
print True in results
print "(done computationally, the full computation will not be printed)"
print
print
print
