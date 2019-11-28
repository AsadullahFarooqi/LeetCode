class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        hash_map = {"2": ["a","b","c"],
             "3": ["d","e","f"],
             "4": ["g","h","i"],
             "5": ["j","k","l"],
             "6": ["m","n","o"],
             "7": ["p","q","r","s"],
             "8": ["t","u","v"],
             "9": ["w","x","y","z"]
            }
        ans = []

        for i in range(len(digits)):
            temp = []
            for j in hash_map[i]:
                for others in range(len(digits)):
                    if i == others: continue



if __name__ == '__main__':
    inp = "23"
    sol = Solution().letterCombinations(inp)
    print(sol)

"""
Hi, my name is Asadullah Farooqi.
As a highly motivated and dedicated developer with strong Problem solving skills, I would like to apply for this position​.
As a self-educator I have been extensively involved in development. Not to mention that i studied in a very tough environment where there was no electricity and no internet. It was very difficult to keep my self motivated and passionate.
Personal attributes that I believe make me suitable for this position include:
• Programming Languages:​ Python, JavaScript(ES6), TypeScript, C/C++
• Web: ​ Django, Flask, Apollo Client, reactjs, HTML, CSS, Bootstrap, Material-UI, AngularJS
• Tools: ​ Git, jinja2, Graphene, Pandas
• Query Language :​ GraphQL, basic MySQL
Also I am very good at algorithms and data structures.
Feel free to check out my ​Github​(https://github.com/AsadullahFarooqi/) and​ LinkedIn​(https://www.linkedin.com/in/asadullah-farooqi-0bb080111).
I am aware that you will receive a large number of applications, But I would very much appreciate the opportunity to demonstrate my skills to you in person.

Asadullah


As a highly motivated and dedicated developer with strong Problem solving skills, I would like to apply for this position​.
As a self-educator I have been extensively involved in development. I studied in a very tough environment where there was no electricity and no internet. It was very difficult to keep my self motivated and passionate.
Personal attributes that I believe make me suitable for this position include:
• Programming Languages:​ Python, JavaScript(ES6), TypeScript, C/C++
• Web: ​ Django, Flask, Apollo Client, reactjs, HTML, CSS, Bootstrap, Material-UI, AngularJS
• Tools: ​ Git, jinja2, Graphene, Pandas
• Query Language :​ GraphQL, basic MySQL
"""