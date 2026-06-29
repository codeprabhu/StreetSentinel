from app.agents.vision_agent import VisionAgent
from app.agents.context_agent import ContextAgent
from app.agents.impact_agent import ImpactAgent
from app.agents.duplicate_agent import DuplicateAgent
from app.agents.resolution_agent import ResolutionAgent
from app.database.firestore import save_report

class ReportService:

    @staticmethod
    def process_report(report):

        report = VisionAgent.run(report)

        report = ContextAgent.run(report)

        report = ImpactAgent.run(report)

        report = DuplicateAgent.run(report)

        report = ResolutionAgent.run(report)

        save_report(report)

        return report