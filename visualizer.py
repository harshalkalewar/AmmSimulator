import pandas as pd
import matplotlib.pyplot as plt

def plot_simulation_results(file_with_fee, file_no_fee):

    df_fee = pd.read_csv(file_with_fee)
    df_no_fee = pd.read_csv(file_no_fee)

    trades = df_fee['Trade Number']

    # Plot Price Evolution
    plt.figure(figsize=(12, 6))
    plt.plot(trades, df_fee['New Price'], label='With Fee', marker='o')
    plt.plot(trades, df_no_fee['New Price'], label='No Fee', marker='x')
    plt.title('Price Evolution Over Trades')
    plt.xlabel('Trade Number')
    plt.ylabel('Price of Token A in terms of Token B')
    plt.legend()
    plt.grid()
    plt.savefig('outputs/price_evolution.png')
    plt.show()

    # Plot Fees Collected
    plt.figure(figsize=(12, 6))
    plt.plot(trades, df_fee['Fees Collected'], label='Cumulative Fees Collected (With Fee)', color='green', marker='o')
    plt.title('Fees Collected Over Trades')
    plt.xlabel('Trade Number')
    plt.ylabel('Fees Collected')
    plt.grid()
    plt.legend()
    plt.savefig('outputs/fees_collected.png')
    plt.show()

    # Plot Slippage
    plt.figure(figsize=(12, 6))
    plt.plot(trades, df_fee['Slippage'], label='Slippage With Fee', marker='o')
    plt.plot(trades, df_no_fee['Slippage'], label='Slippage No Fee', marker='x')
    plt.title('Slippage Comparison')
    plt.xlabel('Trade Number')
    plt.ylabel('Slippage')
    plt.legend()
    plt.grid()
    plt.savefig('outputs/slippage_comparison.png')
    plt.show()

