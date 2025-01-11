import sys
import os
import argparse
import time  # For the scheduler to keep running
import signal  # For handling Ctrl+C
from tools.telegram_toolkit import TelegramToolkit
from utils.utils import error_handler
from utils.knowledge_base import knowledge_base
from utils.logger import logger
from utils.scheduler import setup_scheduler, scheduler
from agents.data_collection import create_data_collection_agent
from agents.analysis import create_technical_analysis_agent
from agents.risk_management import create_risk_management_agent
from agents.execution import create_execution_agent
from agents.monitoring import create_performance_monitoring_agent

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
telegram_toolkit = TelegramToolkit()


# Create agents
data_collection_agent = create_data_collection_agent()
technical_analysis_agent = create_technical_analysis_agent(knowledge_base)
risk_management_agent = create_risk_management_agent()
execution_agent = create_execution_agent()
performance_monitoring_agent = create_performance_monitoring_agent()



def collect_data():
    logger.info("Collecting market data...")
    data_collection_agent.print_response("Fetch data for AAPL, BTC, and SPY.")

def analyze_trades():
    logger.info("Analyzing trade opportunities...")
    technical_analysis_agent.print_response("Analyze trade opportunities for collected data.")

def evaluate_risk():
    logger.info("Evaluating risk...")
    risk_management_agent.print_response("Evaluate risk for identified trade opportunities.")

def execute_trades():
    logger.info("Executing trades...")
    execution_agent.print_response("Execute trade opportunities stored in memory.")

def monitor_performance():
    logger.info("Monitoring performance...")
    performance_monitoring_agent.print_response("Analyze the performance of executed trades.")

def main_workflow():
    try:
        collect_data()
    except Exception as e:
        logger.error(f"Error during data collection: {e}")
    
    try:
        analyze_trades()
    except Exception as e:
        logger.error(f"Error during trade analysis: {e}")
    
    try:
        evaluate_risk()
    except Exception as e:
        logger.error(f"Error during risk evaluation: {e}")
    
    try:
        execute_trades()
    except Exception as e:
        logger.error(f"Error during trade execution: {e}")
    
    try:
        monitor_performance()
    except Exception as e:
        logger.error(f"Error during performance monitoring: {e}")


def shutdown_gracefully(signum, frame):
    logger.info("Received shutdown signal. Stopping scheduler...")
    scheduler.shutdown(wait=False)
    logger.info("Scheduler stopped. Exiting...")
    sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the workflow or start the scheduler.")
    parser.add_argument("--run-workflow", action="store_true", help="Run the main workflow directly.")
    args = parser.parse_args()

    if args.run_workflow:
        logger.info("Running main workflow directly...")
        main_workflow()
    else:
        # Add jobs to the scheduler
        scheduler.add_job(collect_data, "interval", minutes=5, id="collect_data_job", replace_existing=True)
        scheduler.add_job(analyze_trades, "interval", minutes=10, id="analyze_trades_job", replace_existing=True)
        scheduler.add_job(evaluate_risk, "interval", minutes=15, id="evaluate_risk_job", replace_existing=True)
        scheduler.add_job(execute_trades, "interval", minutes=20, id="execute_trades_job", replace_existing=True)
        scheduler.add_job(monitor_performance, "interval", minutes=30, id="monitor_performance_job", replace_existing=True)

        # Register signal handler for Ctrl+C
        signal.signal(signal.SIGINT, shutdown_gracefully)

        try:
            scheduler.start()
            logger.info("Scheduler started. Press Ctrl+C to exit.")
            while True:
                time.sleep(1)  # Keep the script alive
        except (KeyboardInterrupt, SystemExit):
            shutdown_gracefully(None, None)