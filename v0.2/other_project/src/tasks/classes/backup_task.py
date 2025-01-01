class BackupTask:
    def __init__(self, parameters):
        self.parameters = parameters

    def execute(self):
        print(f"Backing up database to {self.parameters['path']} (compress: {self.parameters['compress']})")

