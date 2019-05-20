def most_common_word(paragraph, banned):
      d = {}

      for i in 
      paragraph = paragraph.split()
      banned = [b.lower() for b in banned]
      for i in paragraph:
          i = i.lower().strip()
          if i in banned:
              continue
          if i not in d:
              d[i] = 1
              continue
          d[i] += 1

      m_k = None
      m_v = float("-inf")
      for k, v in d.items():
          if v > m_v:
              m_v = v
              m_k = k
      return m_k

if __name__ == '__main__':
    p = "Bob hit a ball, the hit BALL flew far after it was hit."
    b = ["hit"]
    print(most_common_word(p, b))
