from src.main.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator_4:
    def calculator_average(self, numbers: list) -> dict:
            
            if not numbers or not all(isinstance(number, (int, float)) for number in numbers):
                    raise HttpUnprocessableEntityError ('Lista de números não econtrada!')
            
            average = sum(numbers) / len(numbers)
            response = self.__format_response(average)

            return response
    
    def __format_response(self, average: float) -> dict:
        return {
            "data": {
                "Calculator": 4,
                "average": average
            }
        }
     
        

