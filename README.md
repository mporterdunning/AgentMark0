# AgentMark0

AgentMark0 is a modular AI-driven trading bot that collects market data, analyzes trading opportunities, evaluates risks, executes trades, and monitors performance. The bot leverages tools like Telegram for notifications, PostgreSQL with pgvector for storing data, and APScheduler for job scheduling.

## Features

- **Data Collection**: Fetches live and historical data for stocks, ETFs, and cryptocurrencies.
- **Technical Analysis**: Analyzes trading signals using MACD, RSI, Bollinger Bands, and other indicators.
- **Risk Management**: Evaluates portfolio risk and ensures adherence to risk parameters.
- **Trade Execution**: Automates trade placement and sends real-time Telegram notifications.
- **Performance Monitoring**: Tracks and evaluates trading strategies for continuous improvement.

---

## Requirements

- Python 3.10+
- PostgreSQL with `pgvector` extension

### Dependencies

All dependencies are listed in `requirements.txt`. To install them, see the **Setup** section below.

---

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/mporterdunning/AgentMark0.git
cd AgentMark0