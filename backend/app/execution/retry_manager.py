class RetryManager:

    def execute(self, fn, retries=2):

        for _ in range(retries):

            try:
                return fn()

            except Exception:
                pass

        return fn()