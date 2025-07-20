# simulator.py

import random
import pandas as pd
from amm import AMMPool

def generate_random_trades(num_trades, min_amount=1, max_amount=10):

    trades = []
    for _ in range(num_trades):
        amount = random.uniform(min_amount, max_amount)
        input_token = random.choice(['A', 'B'])
        trades.append({'input_amount': amount, 'input_token': input_token})
    return trades

def run_simulation(pool, trades):

    history = []

    for i, trade in enumerate(trades):
        result = pool.swap(trade['input_amount'], trade['input_token'])
        history.append({
            'Trade Number': i+1,
            'Input Token': trade['input_token'],
            'Input Amount': trade['input_amount'],
            'Output Amount': result['output_amount'],
            'New Price': result['current_price'],
            'Token A Reserve': result['new_token_a_reserve'],
            'Token B Reserve': result['new_token_b_reserve'],
            'Fees Collected': result['fees_collected'],
            'Slippage': result['slippage']
        })

    return pd.DataFrame(history)

