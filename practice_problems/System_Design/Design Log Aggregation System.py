# Design the LogAggregator class:
#
# LogAggregator(int machines, int services) Initializes the object with machines and services representing the number of machines and services in the datacenter, respectively.
# void pushLog(int logId, int machineId, int serviceId, String message) Adds a log with id logId notifying that the machine machineId sent a string message while executing the service serviceId.
# List<Integer> getLogsFromMachine(int machineId) Returns a list of ids of all logs added by machine machineId.
# List<Integer> getLogsOfService(int serviceId) Returns a list of ids of all logs added while running service serviceId on any machine.
# List<String> search(int serviceId, String searchString) Returns a list of messages of all logs added while running service serviceId where the message of the log contains searchString as a substring.


class LogAggregator:
    def __init__(self, machines, services):
        self._machine_logs = [[] for _ in range(machines)]
        self._service_logs = [[] for _ in range(services)]
        self._log = {}

    def pushLog(self, logId, machineId, serviceId, message):
        self._machine_logs[machineId].append(logId)
        self._service_logs[serviceId].append(logId)
        self._log = message

    def getLogsFromMachine(self, machineId):
        return self._machine_logs[machineId]

    def getLogsOfService(self, serviceId):
        return self._service_logs[serviceId]

    def search(self, serviceId, searchString):
        logs = []
        for logId in self.getLogsOfService(serviceId):
            if searchString in self._logs[logId]:
                logs.append(self._logs[logId])
        return logs

