def q2(inputs):
#question 2
#GUOLIANG LIU
    results = []

    for input in inputs:
        lcount = 0
        rcount = 0

        for ch in input:
            if ch == '(':
                lcount += 1
            elif ch == ')':
              if lcount > 0:
                   lcount -= 1
                else:
                 rcount += 1

        results.append(input)

        if rcount > 0 or lcount > 0:
            idc = ''
             idc += '?' * rcount
              idc += 'x' * lcount
               results.append(idc)
        else:
            results.append("")  
             
       return results
     
if __name__ == "__main__":
    inputs = [
        "bge)))))))))",
        "((IIII)))))",
        "()()()()(uuu",
        "))))UUUU((()"
       ]

    outputs = q2(inputs)
    for output in outputs:
        print(output)
