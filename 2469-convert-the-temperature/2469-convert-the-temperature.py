class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = self.celsiusToKelvin(celsius)
        fahrenheit = self.celsiusToFahrenheit(celsius)
        return [kelvin, fahrenheit]
        
    def celsiusToKelvin(self, celsius: float) -> float:
        return celsius + 273.15
        
    def celsiusToFahrenheit(self, celsius: float) -> float:
        return celsius * 1.80 + 32.00