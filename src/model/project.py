from enum import Enum
from typing import Optional

from src.util import env
from src.util.projecthelpers import project_name_finder


class Project(Enum):
    NAME = project_name_finder()

    @classmethod
    def _missing_(cls, value):
        raise ValueError(f"{value} is not a valid AIR project, must be one of {[p.value for p in Project]}")


class ProjectInfo:
    def __init__(
        self,
        project: Project,
        client_key_name: str,
        base_url: str = None,
    ):
        self.name: str = project.value
        self.client_key_name: str = client_key_name
        self.base_url: Optional[str] = base_url
        self.project: Project = project

    def get_client_api_key(self) -> str:
        return env.get_env_value(self.client_key_name)
