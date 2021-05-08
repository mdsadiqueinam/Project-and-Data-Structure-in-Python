def repeat_to_length(s, wanted):
    return (s * (wanted//len(s) + 1))[:wanted]
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
answer = []
arranged_problems = ""
size = len(problems)
if size > 5 :
    print ("Error: Too many problems.")
for it in range(0,size) :
    steps = problems[it].split()
    if steps[1] != "+" and steps[1] != "-" :
        print ("Error: Operator must be '+' or '-'.")
    if not steps[0].isdigit() or not steps[2].isdigit() :
        print ("Error: Numbers must only contain digits.")
    length = max(len(steps[0]),len(steps[2]))
    if length > 4 :
        print ("Error: Numbers cannot be more than four digits.")
    x = int(steps[0])+int(steps[2])
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
arranged_problems += "\n"
for it in range(0,size) :
    arranged_problems = arranged_problems + answer[it]
print(arranged_problems)