digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open('1/input.txt') as f:
    lines = f.readlines()
    all_digits_found = []
    somme = 0
    for line in lines:
        line_formated = line
        digits_found = []
        for s in range(len(line_formated)):
            for l in range(len(line_formated)):
                if line_formated[s:s+l] in digits:
                    digits_found.append(int(digits.index(line_formated[s:s+l])+1))
                elif str.isnumeric(line_formated[s:s+l]):
                    digits_found.append(int(line_formated[s:s+l]))
        
        all_digits_found.append(digits_found)
    print(all_digits_found)
    somme = sum([int(str(digits_found[0]) + str(digits_found[-1])) for digits_found in all_digits_found])
    print(somme)
                    
                    
            
        