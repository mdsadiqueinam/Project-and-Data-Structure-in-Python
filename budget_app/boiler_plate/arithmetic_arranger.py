def repeat_to_length(s, wanted):
    return (s * (wanted//len(s) + 1))[:wanted]

def arithmetic_arranger(problems, condition=False):
    arranged_problems = ""
    answer = []
    size = len(problems)
    if size > 5 :
        return ("Error: Too many problems.")
    for it in range(0,size) :
        steps = problems[it].split()
        if not steps[0].isdigit() or not steps[2].isdigit() :
            return ("Error: Numbers must only contain digits.")
        length = max(len(steps[0]),len(steps[2]))
        if length > 4 :
            return ("Error: Numbers cannot be more than four digits.")
        if steps[1] == "+" :
            x = int(steps[0])+int(steps[2])        
        elif steps[1] == "-" :
            x = int(steps[0])-int(steps[2])
        else :
            return ("Error: Operator must be '+' or '-'.")
        x = str(x)
        answer.append(x)
        steps[0] = steps[0].rjust(length)
        steps[2] = steps[2].rjust(length)
        problems[it] = steps[1]+" "+steps[2]
        arranged_problems = arranged_problems + "  " + steps[0]
        if it < (size-1) :
            arranged_problems = arranged_problems + "    "
    arranged_problems += "\n"
    for it in range(0,size) :
        arranged_problems = arranged_problems + problems[it]
        problems[it] = repeat_to_length('-',len(problems[it]))
        answer[it] = answer[it].rjust(len(problems[it]))
        if it < (size-1) :
            arranged_problems += "    "
            problems[it] += "    "
            answer[it] += "    "
    arranged_problems += "\n"
    for it in range(0,size) :
        arranged_problems = arranged_problems + problems[it]
    if not condition :
        return arranged_problems
    arranged_problems += "\n"
    for it in range(0,size) :
        arranged_problems = arranged_problems + answer[it]
    return arranged_problems