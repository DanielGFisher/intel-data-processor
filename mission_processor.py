class MissionProcessor:
    def load_mission_data(self):
        """Sample mission data"""
        return [
            {"id": "M001", "location": "Kabul", "status": "Complete", "priority": "High"},
            {"id": "M002", "location": "Baghdad", "status": "Active", "priority": "Medium"},
            {"id": "M003", "location": "Damascus", "status": "Pending", "priority": "High"},
            {"id": "M004", "location": "Tehran", "status": "Complete", "priority": "Low"}
        ]

    def filter_by_status(self,missions, status):
        """Filter missions by status"""
        return [m for m in missions if m["status"] == status]

    def count_by_priority(self,missions):
        """Count missions by priority level"""
        counts = {"High": 0, "Medium": 0, "Low": 0}
        for mission in missions:
            if mission["priority"] in counts:
                counts[mission["priority"]] += 1
        return counts
