class Solution:
    @staticmethod
    def reverse(x: int) -> int:

       foob = str(x)[::-1] 
       if foob[-1] == '-':
           foob = foob[:-1] 
           foob = '-' + foob
       return foob


if __name__ == '__main__':
    print(Solution.reverse(-321))