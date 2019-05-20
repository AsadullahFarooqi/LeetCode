def main(words):
    alpha_code_dictionary = {}
    code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    alph = list('abcdefghijklmnopqrstuvwxyz')
    
    for x in range(len(code)):
        alpha_code_dictionary[alph[x]] = code[x]
    print(alpha_code_dictionary)
    s = set()
    for i in words:
        temp = "".join([alpha_code_dictionary[j] for j in i])
        s.add(temp)

    return len(s)

if __name__ == '__main__':
    words = ["gin", "zen", "gig", "msg"]
    main(words)