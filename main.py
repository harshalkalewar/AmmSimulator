# main.py

import os
import argparse
from simulator import generate_random_trades, run_simulation
from amm import AMMPool
from visualizer import plot_simulation_results


def parse_arguments():
    """
    Parses command-line arguments to configure the simulation.

    Returns:
        argparse.Namespace: Contains parsed arguments.
    """
    parser = argparse.ArgumentParser(description="AMM Simulator with Fee and Zero-Fee Comparison")

    parser.add_argument('--num_trades', type=int, default=10,
                        help='Number of trades to simulate (default: 10)')
    parser.add_argument('--initial_token_a', type=float, default=100,
                        help='Initial reserve of Token A (default: 100)')
    parser.add_argument('--initial_token_b', type=float, default=200000,
                        help='Initial reserve of Token B (default: 200000)')
    parser.add_argument('--fee_percent', type=float, default=0.3,
                        help='Fee percentage for the fee simulation (default: 0.3)')

    return parser.parse_args()


def main():
    args = parse_arguments()

    print("🔄 Initializing AMM Simulator...")
    print(f"➡️ Number of Trades: {args.num_trades}")
    print(f"➡️ Initial Token A Reserve: {args.initial_token_a}")
    print(f"➡️ Initial Token B Reserve: {args.initial_token_b}")
    print(f"➡️ Fee Percentage: {args.fee_percent}%")

    output_folder = 'outputs'
    os.makedirs(output_folder, exist_ok=True)

    # Step 1: Generate Random Trades
    trades = generate_random_trades(args.num_trades)
    print(f"📈 Generated {len(trades)} random trades.")

    # Step 2: Run Simulation with Fee
    print("⚙️ Running simulation with fee...")
    pool_with_fee = AMMPool(args.initial_token_a, args.initial_token_b, fee_percent=args.fee_percent)
    results_with_fee = run_simulation(pool_with_fee, trades)
    file_with_fee = os.path.join(output_folder, 'simulation_with_fee.csv')
    results_with_fee.to_csv(file_with_fee, index=False)
    print(f"✅ Results with fee saved to: {file_with_fee}")

    # Step 3: Run Simulation with Zero Fee
    print("⚙️ Running simulation with zero fee...")
    pool_no_fee = AMMPool(args.initial_token_a, args.initial_token_b, fee_percent=0.0)
    results_no_fee = run_simulation(pool_no_fee, trades)
    file_no_fee = os.path.join(output_folder, 'simulation_no_fee.csv')
    results_no_fee.to_csv(file_no_fee, index=False)
    print(f"✅ Results with zero fee saved to: {file_no_fee}")

    # Step 4: Visualize
    print("📊 Generating comparison plots...")
    plot_simulation_results(file_with_fee, file_no_fee)

    print("🎉 Simulation and visualization complete! Check the 'outputs' folder for results and plots.")


if __name__ == '__main__':
    main()
