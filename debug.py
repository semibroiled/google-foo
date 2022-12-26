def solution(pegs):
    #Update: Corrected for first gear calculation, 2* ans in bracket
    #Update 2: Trial and error corrected for hidden test, gear check was invalid
    #Update 3: Simplify code by taking out a core math expression outside of if blocks
    #Update 4: simplify var names? No bueno
    #Update 5: Check for r=a/b was flawed. I was checking for less than 0 as plausability check. i guess aufgabestellung meant a/b
    #Update 6: Found a sol just like mine.- plagiarism grounds? Mightve searched possible sol and took note subconsly

    #Calculating distance from peg position, and separating into cases with even and odd pegs
    #We get a sequence of linear pattern
    #odd pegs are +tiv, even pegs are -tiv, multiplioed by 2, exluding 0th peg, which is outside parameter bracket subtracted from this
    #last peg is always outside eq as added or subtractefd for even or odd number of pegs

    seq_core = 2*(sum(pegs[1::2]) - sum(pegs[::2])) + pegs[0]
    num_pegs = len(pegs) # number of pegs
    no_ans = [-1,-1] #return this in case there is no answer
    ans = None 

    # #we need at least 2 gears for a valid calculation
    # if num_pegs < 3:
    #     return no_ans    

    #in case of even number of pegs
    if  num_pegs% 2 == 0:
        seq_even = 2*(seq_core - pegs[-1])

        #for all 3 cases...with seq = 3*last gear radius
        if seq_even/3 < 1:
            return no_ans #gear radius starts from 1
        if seq_even % 3 == 0:
            ans = [seq_even/3, 1] # simplified if divisible
        else:
            ans = [seq_even, 3] #already in simplified form
    #for odd number of pegs
    if num_pegs%2==1:
        seq_odd = 2*(seq_core +pegs[-1])
        
        #for all 3 cases...with seq = last gear radius
        if seq_odd < 1:
            return no_ans
        else:

            ans = [seq_odd, 1]
            
    r_n = ans[0]/ans[1] #r=a/b
    #check that radius does not exceed distance between pegs at any point bzw. that succesive inclusion of positve radius is possible
    # ie check for physical viability
    for i in range(len(pegs)-1):
        r_n = pegs[i+1]-pegs[i] - r_n
        if r_n < 1:
            return no_ans
    return ans



