# Multi-Gate Stock Transformer
NYCU Deep Learning Final Project - Multi-Gate Stock Transformer

This project implements a modified version of the AAAI-2024 paper [MASTER: Market-Guided Stock Transformer for Stock Price Forecasting](https://ojs.aaai.org/index.php/AAAI/article/view/27767), aiming to improve stock price prediction by incorporating richer market information and additional gating mechanisms.  


## Project Overview
The original MASTER model uses market prices and volumes but struggles with insufficient market info, poor gating, and suboptimal feature scaling. 

Our modifications:  
1. **Expanding Market Features** – Including additional market indicators beyond prices and volumes  
2. **Industry Gate** – Introducing industry-specific gating for better feature differentiation  
3. **News Features** – Integrating market news data to enrich input information  

<img width="1531" height="609" alt="image" src="https://github.com/user-attachments/assets/ce580989-882b-4e68-9f7b-f4f791d0538c" />

## Experimental Setup
- **Stocks**: 8 firms × 9 industries = 72 stocks from S&P 500 constituents
- **Dataset Splits**:  
  1. **Full period (following MASTER paper)**  
     - Training: 2008–2022  
     - Testing: 2023  
  2. **Pre-COVID-19 period**  
     - Training: 2008–2017  
     - Testing: 2018  


## Results
### Full Period (2008–2023)  

| Metric | No Trick | All Tricks | Trick 1 | Trick 2 | Trick 3 |
|--------|----------|------------|---------|---------|---------|
| RMSE   | 0.0196   | **0.0184**     | 0.0186  | 0.0196  | 0.0185  |
| MAE    | 0.0143   | **0.0130**     | 0.0134  | 0.0142  | 0.0131  |

### Pre-COVID-19 Period (2008–2018)  

| Metric | No Trick | All Tricks | Trick 1 | Trick 2 | Trick 3 |
|--------|----------|------------|---------|---------|---------|
| RMSE   | 0.0180   | **0.0168**     | 0.0169  | 0.0174  | 0.0175  |
| MAE    | 0.0129   | **0.0120**     | 0.0122  | 0.0125  | 0.0126  |

### Performance Improvement:  
- 5–6% RMSE reduction observed in both 2018 and 2023 testing periods 
