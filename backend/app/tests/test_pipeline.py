from app.models.report import Report
from app.services.report_service import ReportService

report = Report(
    id="1",
    image_path="pothole.jpg",
    latitude=13.34,
    longitude=74.75,
    created_at="2026-06-27T00:00:00"
)

result = ReportService.process_report(report)

print(result.model_dump())