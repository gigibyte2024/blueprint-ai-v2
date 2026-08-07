from app.execution.telemetry import Telemetry
from app.execution.retry_manager import RetryManager


class ExecutionEngine:

    def __init__(self):

        self.telemetry = Telemetry()
        self.retry = RetryManager()

    def execute(self, execution_plan, state):

        print("\n========== EXECUTION PLAN ==========\n")
        print(execution_plan)
        print("\n====================================\n")

        for tool in execution_plan.get("tools", []):

            print(f"🔧 Tool: {tool}")

        for group in execution_plan.get("parallel_groups", []):

            print(f"⚡ Parallel Group: {group}")

        return state