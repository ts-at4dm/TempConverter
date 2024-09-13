# Program name: Temp Convertion
# Author: Terran Stone
# Description: Converts Celsius to Fahrenheit
# Date Created/Modified: 9/12/24
# Notes: Simple Temperature Conversion program
import time

def main():
    celsius = eval(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")
print(time.ctime())
main()
