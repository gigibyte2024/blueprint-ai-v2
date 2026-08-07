from concurrent.futures import ThreadPoolExecutor


class ParallelExecutor:

    def run(self, functions):

        with ThreadPoolExecutor() as executor:

            futures = [
                executor.submit(fn)
                for fn in functions
            ]

            return [
                future.result()
                for future in futures
            ]