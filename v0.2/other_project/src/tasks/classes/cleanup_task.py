class CleanupTask:
    def __init__(self, parameters):
        self.parameters = parameters

    def execute(self):
        print(f"Cleaning files older than {self.parameters['age']} in {self.parameters['location']}")
