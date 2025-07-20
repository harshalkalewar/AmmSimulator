# AMM Simulator

This project simulates an **Automated Market Maker (AMM)** based on the **constant product formula** `x * y = k`, similar to Uniswap v2.

It models:
- **Liquidity pools with and without trading fees**
- Multiple random swaps on both versions
- Tracking of price, slippage, fees collected, and LP (Liquidity Provider) value
- Visualization of outcomes to compare both models

---

## ✅ **Project Features**

- Simulate **Token A ↔ Token B swaps** via the AMM formula
- Support for configurable **fee percentage** (e.g., 0.3%)
- Run simulations on:
  - **Fee model** (e.g., Uniswap-like with 0.3% fee)
  - **Zero-Fee model** 
- Output simulation data to CSV
- Generate visualizations for:
  - **Price evolution over trades**
  - **Fees collected (cumulative)**
  - **Slippage comparison**

---

## 🗂 **Project Structure**

````
AMM_Simulator/
│
├── amm.py # AMM core logic: swap mechanics, fee handling
├── simulator.py # Simulation engine: generate trades, run swaps
├── visualize.py # Plotting utilities for results
├── main.py # Unified entry-point with CLI configuration
├── requirements.txt # Dependencies
├── outputs/ # Stores generated CSVs and plots
└── README.md # Project documentation

````


---

## 🚀 **How to Run**

### 1️⃣ **Install Dependencies**

```bash
  pip install -r requirements.txt
```

### 2️⃣ Run Simulation

#### Run with default settings:
```
python main.py
```
##### Or customize parameters:

```
python main.py --num_trades 20 --initial_token_a 150 --initial_token_b 300000 --fee_percent 0.5
```


#### Available Arguments:

````
Argument	       Description	                     Default
--num_trades	   Number of trades to simulate	10
--initial_token_a  Initial reserve for Token A	100
--initial_token_b  Initial reserve for Token B	200000
--fee_percent	   Fee percentage for simulation	0.3

````

### 3️⃣ View Results


    Outputs:

        outputs/simulation_with_fee.csv

        outputs/simulation_no_fee.csv

    Plots:

        outputs/price_evolution.png

        outputs/fees_collected.png

        outputs/slippage_comparison.png

### 📊 Example Plots & Screenshots 
#### ( These are for 20 Trades with a fee percentage of 0.5 and reserves as 150 and 300000 for token A & B respectively. )
#### 📈 1. Price Evolution Over Trades
![](outputs/price_evolution1.png)

#### 💰 2. Fees Collected Over Trades
![](outputs/fees_collected1.png)

#### 📉 3. Slippage Comparison
![](outputs/slippage_comparison1.png)

## 📈 Visualizations

    Price Evolution: Compare how price changes between fee vs no-fee models.

    Fees Collected: Total fees accrued in the fee model.

    Slippage Comparison: Slippage per trade under both models.

## 🔧 Future Improvements

    LP value growth over time

    Impermanent Loss tracking

    Config file support (.yaml/.json)

    Save and replay predefined trade sets    

## 🤝 Contributing

    Feel free to open issues or pull requests to improve or extend the simulation.


## 📄 License
    MIT License

## 🙌 Author
    Harshal Kalewar