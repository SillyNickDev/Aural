
from helpers.logger import Logger
from manager.manager import Manager
from pycaw.pycaw import AudioUtilities

class CUI:
    def Launch(self):
        print("Launching CUI...")
        self._Start()

    def _Start(self):
        app = Application()
        app.Run()

class Application:
    def __init__(self):
        self.Width = 1280
        self.Height = 720

        self.log = Logger("Aural.CUI", "cui.log")
        self.manager = Manager.Get()

    def Run(self):
        print("Welcome to Aural CUI")
        while True:
            print("\nMain Menu:")
            print("1. List Audio Devices")
            print("2. List Audio Cables")
            print("3. Create Audio Cable")
            print("4. List Routes")
            print("5. Create Route")
            print("6. Exit")
            choice = input("Select an option: ").strip()
            if choice == "1":
                self.list_audio_devices()
            elif choice == "2":
                self.list_audio_cables()
            elif choice == "3":
                self.create_audio_cable()
            elif choice == "4":
                self.list_routes()
            elif choice == "5":
                self.create_route()
            elif choice == "6":
                break
            else:
                print("Invalid option. Please try again.")
        print("Exiting CUI...")

    def list_audio_devices(self):
        print("Listing audio devices...")
        try:
            devices = AudioUtilities.GetAllDevices()
            print("All audio devices:")
            for i, device in enumerate(devices):
                state = "Active" if device.state == 1 else "Inactive"
                print(f"{i+1}. {device.FriendlyName} - {state}")
        except Exception as e:
            print(f"Error listing devices: {e}")

    def list_audio_cables(self):
        print("Listing audio cables...")
        cables = self.manager.AudioCables().AudioCables
        if not cables:
            print("No audio cables created.")
        else:
            for i, cable in enumerate(cables):
                print(f"{i+1}. {cable.Configuration['Name']}")

    def create_audio_cable(self):
        print("Creating audio cable...")
        self.manager.AudioCables().Create()
        print("Audio cable created.")

    def list_routes(self):
        print("Listing routes...")
        routes = self.manager.Routes().Routes
        print(f"Number of routes: {len(routes)}")

    def create_route(self):
        print("Creating route...")
        self.manager.Routes().Create()
        print("Route created.")