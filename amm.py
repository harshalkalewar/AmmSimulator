# amm.py

import pandas as pd

class AMMPool:

    def __init__(self, token_a_reserve, token_b_reserve, fee_percent=0.3):

        self.token_a = token_a_reserve
        self.token_b = token_b_reserve
        self.fee_percent = fee_percent / 100  # convert % to decimal
        self.k = self.token_a * self.token_b  # Constant product invariant
        self.fees_collected = 0  # track total fees earned

    def get_price(self):
        # current price of Token A in terms of Token B.
        return self.token_b / self.token_a

    def swap(self, input_amount, input_token='A'):

        if input_amount <= 0:
            raise ValueError("Input amount must be greater than zero.")

        fee_multiplier = 1 - self.fee_percent
        amount_in_after_fee = input_amount * fee_multiplier

        if input_token == 'A':
            new_token_a = self.token_a + amount_in_after_fee
            new_token_b = self.k / new_token_a
            amount_out = self.token_b - new_token_b
            slippage = (self.get_price() - (amount_out / input_amount)) / self.get_price()

            # Update reserves
            self.token_a = new_token_a
            self.token_b = new_token_b

        elif input_token == 'B':
            new_token_b = self.token_b + amount_in_after_fee
            new_token_a = self.k / new_token_b
            amount_out = self.token_a - new_token_a
            slippage = ((amount_out / input_amount) - (1 / self.get_price())) / (1 / self.get_price())

            # Update reserves
            self.token_b = new_token_b
            self.token_a = new_token_a

        else:
            raise ValueError("Invalid input token type. Use 'A' or 'B'.")

        # Track total fees collected
        fees = input_amount * self.fee_percent
        self.fees_collected += fees

        return {
            'input_token': input_token,
            'input_amount': input_amount,
            'output_amount': amount_out,
            'new_token_a_reserve': self.token_a,
            'new_token_b_reserve': self.token_b,
            'current_price': self.get_price(),
            'slippage': slippage,
            'fees_collected': self.fees_collected
        }
