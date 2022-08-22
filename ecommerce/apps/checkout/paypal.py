import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AY63T0Qrifl5ODt4PW5oSTWttFH-F9vvIVX-rEdLxCtiNtKTE6DqFUTde09aYwX3DZDPFeAddyPiJH8e"
        self.client_secret = "EHNOLJ7p-8FTO5OUv31OVuXuF5EfRIQlhv8Fc-2sJRUDXLYEmiYFyqr5OX8cUed8dZ5z7IXSTu0fWm1Z"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)