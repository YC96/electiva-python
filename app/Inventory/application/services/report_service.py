from sqlmodel import Session
from commands.generate_inventory_report_command import execute_generate_inventory_report_command
from datetime import datetime

class ReportService:
    def __init__(self, session: Session):
        self.session = session

    def generate_inventory_report(self, start_date: datetime, end_date: datetime) -> str:
        """
        Genera un reporte del inventario entre dos fechas y devuelve la ruta del archivo generado.
        """
        report_path = execute_generate_inventory_report_command(
            start_date=start_date,
            end_date=end_date,
            session=self.session
        )
        return report_path
