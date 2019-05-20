def solution(emails):
  emails_set = set()
  for i in emails:
    local_name = i[:i.find("@")]
    domain_name = i[i.find("@"):]
    local_name = local_name.replace(".", "")
    local_name = local_name.replace(local_name[local_name.find("+"):], "")
    emails_set.add(local_name+domain_name)
  return len(emails_set)

if __name__ == '__main__':
  ls = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
  print(solution(ls))

"""
"test.email+alex@leetcode.com"
"test.e.mail+bob.cathy@leetcode.com",
"testemail+david@lee.tcode.com"

"testemail@leetcode.com"
"testemail@lee.tcode.com"
"""