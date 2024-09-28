class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        for number in range(1, n+1):
            fizz_buzz_str = ""
            if number % 3 == 0:
                fizz_buzz_str += "Fizz"
            if number % 5 == 0:
                fizz_buzz_str += "Buzz"
            if not fizz_buzz_str:
                fizz_buzz_str = str(number)
            result.append(fizz_buzz_str)
        return result
