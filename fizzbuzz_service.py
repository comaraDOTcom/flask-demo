class FizzBuzzService:
    def validate(input_variable):
        if input_variable % 15 == 0:
            return 'FizzBuzz'

        elif input_variable % 3 == 0:
            return 'Fizz'

        elif input_variable % 5 == 0:
            return 'Buzz'
        else:
            return 'fail'
