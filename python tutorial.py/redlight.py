# def redlight():
#     print("stop")
# def greenlight():
#     print("go")
# def yellowlight():
#     print("wait")
    
# redlight()
import time

class TrafficLight:
    def __init__(self):
        self.states = ["Green", "Yellow", "Red"]
        self.current_state = 0

    def change_light(self):
        self.current_state = (self.current_state + 1) % len(self.states)
        return self.states[self.current_state]

    def run(self):
        while True:
            current_light = self.states[self.current_state]
            print(f"Traffic light is {current_light}")
            
            if current_light == "Green":
                time.sleep(5)  # Green light for 5 seconds
            elif current_light == "Yellow":
                time.sleep(2)  # Yellow light for 2 seconds
            elif current_light == "Red":
                time.sleep(7)  # Red light for 7 seconds
            
            self.change_light()

traffic_light = TrafficLight()
traffic_light.run()
