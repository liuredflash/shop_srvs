import requests
import consul
from common.register.base import BaseConsul

class ConsulRegister(BaseConsul):

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._consul = consul.Consul(host=host, port=port)

    def register(self, name, id, service_address, service_port, tags, check=None):
        if not check:
            check = {
                "GRPC": f"{service_address}:{service_port}",
                "GRPCUseTLS": False,
                "Timeout": "5s",
                "Interval": "5s",
                "DeregisterCriticalServiceAfter": "15s"
            }

        success = self._consul.agent.service.register(
            name=name,
            service_id=id,
            address=service_address,
            port=int(service_port),
            tags=tags,
            check=check
        )
        return success
    
    def deregister(self, service_id):
        return self._consul.agent.service.deregister(service_id)

    def get_all_service(self):
        return self._consul.agent.services()

    def filter_service(self, filter_name):
        url = f"http://{self.host}:{self.port}/v1/agent/services"
        params = {
            "filter": f'Service == "{filter_name}"'
         }
        return requests.get(url=url, params=params).json()


