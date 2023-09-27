from dataclasses import dataclass, asdict


@dataclass
class User:

    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    is_active: bool
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True

    def to_dict(self) -> dict:
        survey_dict = asdict(self)
        print(survey_dict)
        return survey_dict

    @classmethod
    def from_dict(cls, _dict: dict):
        return User(
            id=_dict.get('id'),
            username=_dict.get('username'),
            email=_dict.get('email'),
            first_name=_dict.get('first_name'),
            last_name=_dict.get('last_name'),
            is_active=_dict.get('is_active'),
            created_at=_dict.get('created_at'),
            updated_at=_dict.get('updated_at')
        )
    



