import time


class Telemetry:

    def __init__(self):
        self.logs = []

    def start(self, agent):

        return time.time()

    def end(self, agent, start):

        self.logs.append(
            {
                "agent": agent,
                "duration": round(
                    time.time() - start,
                    2,
                ),
            }
        )

    def get_logs(self):

        return self.logs