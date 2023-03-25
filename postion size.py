# maths function
import math

Account_value = float(input("Enter the account value"))
Risk_percent = float(input("Enter the risk per trade(%)")) / 100
stoploss = float(input("Enter the stoploss amount"))
risk_amount = Account_value * Risk_percent
position_size = math.floor(risk_amount / stoploss)
print("Risk amount", risk_amount)
print("Position size", position_size)
