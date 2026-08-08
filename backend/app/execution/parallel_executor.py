from concurrent.futures import ThreadPoolExecutor, as_completed

from app.execution.retry_manager import RetryManager


class ParallelExecutor:

    def __init__(self):

        self.retry = RetryManager()

    def run(self, tasks):

        results = {}

        if not tasks:
            return results

        with ThreadPoolExecutor(
            max_workers=len(tasks)
        ) as executor:

            futures = {}

            for name, function in tasks.items():

                if not callable(function):

                    raise TypeError(
                        f"Task '{name}' is not callable: "
                        f"{type(function).__name__}"
                    )

                futures[
                    executor.submit(
                        self.retry.execute,
                        function,
                    )
                ] = name

            for future in as_completed(futures):

                name = futures[future]

                try:

                    results[name] = future.result()

                except Exception as error:

                    print(
                        f"❌ Task '{name}' failed "
                        f"after retries: {error}"
                    )

                    results[name] = {
                        "error": str(error),
                        "status": "failed",
                    }

        return results