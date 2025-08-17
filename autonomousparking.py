
import random
import time
import math

class AutonomousVehicle:
    def __init__(self):
        self.position = (0, 0)  # Starting position (x, y)
        self.obstacle_detected = False
        self.parked = False
        self.parking_spot = None

    def scan_for_parking_spot(self):
        """
        Simulate scanning for parking spots.
        Returns True if a parking spot is found, along with its location.
        """
        print("Scanning for parking spots...")
        time.sleep(2)
        # Randomly generate parking spot locations
        parking_spot_x = random.randint(5, 20)
        parking_spot_y = random.randint(5, 20)
        self.parking_spot = (parking_spot_x, parking_spot_y)
        print(f"Parking spot found at location {self.parking_spot}.")
        return True

    def detect_obstacle(self):
        """
        Simulate obstacle detection.
        Returns True if an obstacle is detected, False otherwise.
        """
        self.obstacle_detected = random.choice([True, False])
        if self.obstacle_detected:
            print("Obstacle detected! Re-routing...")
        return self.obstacle_detected

    def navigate_to_parking_spot(self):
        """
        Simulate navigation to the parking spot.
        Avoids obstacles along the way.
        """
        print("Navigating to the parking spot...")
        while self.position != self.parking_spot:
            if self.detect_obstacle():
                # Simulate re-routing
                time.sleep(1)
                print("Re-calculating path to avoid obstacle...")
            else:
                # Move one step closer to the parking spot
                next_x = self.position[0] + (1 if self.position[0] < self.parking_spot[0] else -1 if self.position[0] > self.parking_spot[0] else 0)
                next_y = self.position[1] + (1 if self.position[1] < self.parking_spot[1] else -1 if self.position[1] > self.parking_spot[1] else 0)
                self.position = (next_x, next_y)
                print(f"Current position: {self.position}")
            time.sleep(0.5)

    def align_and_park(self):
        """
        Simulate alignment and parking process.
        """
        print("Aligning with the parking spot...")
        time.sleep(1)
        print("Parking in progress...")
        time.sleep(2)
        self.parked = True
        print(f"Vehicle parked at location {self.position}.")

    def self_park(self):
        """
        Complete self-parking sequence.
        """
        if self.scan_for_parking_spot():
            self.navigate_to_parking_spot()
            self.align_and_park()

# Main execution
if __name__ == "__main__":
    av = AutonomousVehicle()
    print("Starting self-parking system...")
    av.self_park()
    print("Self-parking process complete.")

