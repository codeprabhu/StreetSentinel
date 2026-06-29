class VisionAgent:

    @staticmethod
    def run(report):
        report.issue_type = "Pothole"
        report.description = "Large pothole detected"

        return report
