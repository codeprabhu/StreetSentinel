class ImpactAgent:

    @staticmethod
    def run(report):
        report.impact_score = 75
        report.severity = "High"

        return report