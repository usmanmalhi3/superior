class SimpleReflexAgent:
    def __init__(self, desired_temperature):
        self.desired_temperature = desired_temperature 

    def perceive(self, current_temperature):
        return current_temperature

    def act(self, current_temperature):
        if current_temperature < self.desired_temperature:
            action = "Turn on heater"
        else:
            action = "Turn off heater"
        return action


class ModelBasedReflexAgent:
    def __init__(self, desired_temperature):
        self.desired_temperature = desired_temperature
        self.last_action = None  

    def perceive(self, current_temperature):
        return current_temperature

    def act(self, current_temperature):
        if current_temperature < self.desired_temperature:
            if self.last_action != "Turn on heater":
                action = "Turn on heater"
            else:
                action = "Heater already on, no action needed."
        else:
            if self.last_action != "Turn off heater":
                action = "Turn off heater"
            else:
                action = "Heater already off, no action needed."
        self.last_action = action  
        return action


rooms = {
    "Living Room": 18,
    "Bedroom": 22,
    "Kitchen": 20,
    "Bathroom": 24
}


desired_temperature = 22

print("Simple Reflex Agent Actions:")
simple_agent = SimpleReflexAgent(desired_temperature)
for room, temperature in rooms.items():
    action = simple_agent.act(temperature)
    print(f"{room}: Current temperature = {temperature}°C. {action}.")


print("\nModel-Based Reflex Agent Actions:")
model_based_agent = ModelBasedReflexAgent(desired_temperature)
for room, temperature in rooms.items():
    action = model_based_agent.act(temperature)
    print(f"{room}: Current temperature = {temperature}°C. {action}.")
