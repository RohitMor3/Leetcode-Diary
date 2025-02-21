class Solution:
    def fizzBuzz(self, n: int) -> list[str]: # Changed List to list (lowercase)
        result = []
        for i in range (1, n+1):
            output = ""
            if (i % 3 ==0):
                output += "Fizz"
            if (i %  5 == 0):
                output += "Buzz"
            if (output ==""):
                output = str(i)
            result.append(output)
        return result
        