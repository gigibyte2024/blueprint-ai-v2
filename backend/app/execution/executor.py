from app.agents.planning_agent import PlanningAgent
from app.agents.prd_agent import PRDAgent
from app.agents.technical_agent import TechnicalAgent
from app.agents.api_agent import APIAgent
from app.agents.database_agent import DatabaseAgent
from app.agents.roadmap_agent import RoadmapAgent
from app.agents.ui_agent import UIAgent
from app.agents.reflection_agent import ReflectionAgent

from app.execution.parallel_executor import ParallelExecutor
from app.execution.retry_manager import RetryManager
from app.execution.telemetry import Telemetry


class ExecutionEngine:

    def __init__(self):

        self.parallel = ParallelExecutor()
        self.retry = RetryManager()
        self.telemetry = Telemetry()

        self.agents = {
            "planning": PlanningAgent,
            "prd": PRDAgent,
            "technical": TechnicalAgent,
            "api": APIAgent,
            "database": DatabaseAgent,
            "roadmap": RoadmapAgent,
            "ui": UIAgent,
            "reflection": ReflectionAgent,
        }

    def update_progress(self, state, stage, status):

        progress = state.setdefault(
            "execution_progress",
            []
        )

        progress.append(
            {
                "stage": stage,
                "status": status,
            }
        )

        print(
            f"📡 {stage}: {status}"
        )

    def process_results(self, state, results):

        for name, result in results.items():

            if not isinstance(result, dict):
                continue

            if result.get("status") == "failed":

                self.update_progress(
                    state,
                    name,
                    "failed",
                )

                print(
                    f"⚠️ {name} failed, "
                    "continuing with remaining modules."
                )

                continue

            state.update(result)

        return state

    def create_task(self, name, state):

        agent_class = self.agents.get(name)

        if not agent_class:
            return None

        agent = agent_class()

        return lambda agent=agent: (
            agent.execute(state.copy())
        )

    def execute(self, state):

        self.update_progress(
            state,
            "Execution Engine",
            "started",
        )

        print(
            "\n🚀 EXECUTION ENGINE STARTED\n"
        )

        execution_plan = state.get(
            "execution_plan",
            {}
        )

        parallel_groups = execution_plan.get(
            "parallel_groups",
            []
        )

        requested_modules = state.get(
            "requested_modules",
            []
        )
        # These modules are handled directly
# by the LangGraph workflow.
        execution_modules = [
            module
            for module in requested_modules
            if module not in {"planning", "reflection"}
        ]

        # Fallback if planner did not
        # provide parallel groups.

        if not parallel_groups:

            parallel_groups = [
                execution_modules
            ]

        # -------------------------
        # Execute planner groups
        # -------------------------

        for index, group in enumerate(
            parallel_groups,
            start=1,
        ):

            tasks = {}

            valid_modules = []

            for module in group:

                if module not in execution_modules:
                    continue

                if module not in self.agents:
                    continue

                valid_modules.append(
                    module
                )

                task = self.create_task(
                    module,
                    state,
                )

                if task:
                    tasks[module] = task

            if not tasks:
                continue

            group_name = (
                "Group "
                f"{index}: "
                f"{', '.join(valid_modules)}"
            )

            self.update_progress(
                state,
                group_name,
                "running",
            )

            print(
                f"\n⚡ Running {group_name}\n"
            )

            results = self.parallel.run(
                tasks
            )

            self.process_results(
                state,
                results,
            )

            self.update_progress(
                state,
                group_name,
                "completed",
            )

        self.update_progress(
            state,
            "Execution Engine",
            "completed",
        )

        print(
            "\n✅ EXECUTION ENGINE COMPLETE\n"
        )

        state["execution_logs"] = (
            self.telemetry.get_logs()
        )

        return state