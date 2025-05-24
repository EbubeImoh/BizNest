class BaseAgent:
    def __init__(self, name: str, role: str, avatar_url: str):
        self.name = name
        self.role = role
        self.avatar_url = avatar_url

    def process_command(self, command: str) -> str:
        return f"Agent {self.name} received command: {command}"

# Test instance
alex_the_accountant = BaseAgent(name="Alex", role="Accountant", avatar_url="placeholder_alex.png")
print(alex_the_accountant.process_command("summarize expenses"))
