from datetime import date

from pydantic import BaseModel, ConfigDict


class EntrySchema(BaseModel):
    """
    Schema for a single report entry.

    Corresponds to the Java Entry model:
      start (Date), end (Date), title (String)
    """

    model_config = ConfigDict(populate_by_name=True)

    start: date
    end: date
    title: str


class ReportSchema(BaseModel):
    """
    Schema for report response (GET /report/, GET /report/room/{id}).

    Corresponds to the Java Report model:
      report (List<Entry>)
    """

    model_config = ConfigDict(populate_by_name=True)

    report: list[EntrySchema]
