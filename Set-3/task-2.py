class ParcelTracker:
    def __init__(self):
        self.parcels = {}
        self.scans = set()

    def register(self, tracking_number, destination):
        self.parcels[tracking_number] = destination

    def lookup(self, tracking_number):
        return self.parcels.get(tracking_number)

    def scan(self, tracking_number, hub):
        if tracking_number not in self.parcels:
            return "Unknown parcel"
        key = (tracking_number, hub.upper().strip())
        if key in self.scans:
            return "Duplicate scan"
        self.scans.add(key)
        return "Scan recorded"


if __name__ == "__main__":
    tracker = ParcelTracker()
    tracker.register("TRK1001", "Chennai")
    tracker.register("TRK1002", "Delhi")
    print("Lookup TRK1001:", tracker.lookup("TRK1001"))
    print("Lookup TRK9999:", tracker.lookup("TRK9999"))
    print("TRK1001 at HYD:", tracker.scan("TRK1001", "HYD"))
    print("TRK1001 at hyd:", tracker.scan("TRK1001", "hyd"))
    print("TRK1001 at BLR:", tracker.scan("TRK1001", "BLR"))
    print("TRK9999 at HYD:", tracker.scan("TRK9999", "HYD"))
