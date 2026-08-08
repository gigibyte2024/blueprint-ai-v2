import time


class RetryManager:

    def __init__(
        self,
        max_retries=3,
        base_delay=1,
    ):
        self.max_retries = max_retries
        self.base_delay = base_delay

    def execute(self, function):

        last_error = None

        for attempt in range(
            self.max_retries + 1
        ):

            try:
                return function()

            except Exception as error:

                last_error = error

                if attempt >= self.max_retries:
                    break

                delay = self.base_delay * (
                    2 ** attempt
                )

                print(
                    f"⚠️ Retry {attempt + 1}/"
                    f"{self.max_retries} "
                    f"after {delay}s: {error}"
                )

                time.sleep(delay)

        raise last_error