from dataclasses import dataclass, asdict


@dataclass
class Task:

    id: int
    title: str
    expiration_date: str
    status: str
    user_id: int
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True

    def to_dict(self) -> dict:
        survey_dict = asdict(self)
        return survey_dict

    @classmethod
    def from_dict(cls, _dict: dict):
        return Task(
            id=_dict.get('id'),
            title=_dict.get('title'),
            expiration_date=_dict.get('expiration_date'),
            status=_dict.get('status'),
            user_id=_dict.get('user_id'),
            created_at=_dict.get('created_at'),
            updated_at=_dict.get('updated_at')
        )
    



