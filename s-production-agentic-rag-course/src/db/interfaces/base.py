from abc import ABC, abstractmethod
from typing import Any, ContextManager, Dict, List, Optional
from sqlalchemy.orm import Session

class BaseDatabase(ABC):
    """Base class for database."""

    @abstractmethod
    def startup(self) -> None:
        """ initialize the database connection """

    @abstractmethod
    def teardown(self) -> None:
        """ close the database connection """

    @abstractmethod
    def get_session(self) -> ContextManager[Session]:
        """ get the database session """

class BaseRepository(ABC):
    """Base class for repository."""
    def __init__(self, session: Session) -> None:
        self.session = session

    @abstractmethod
    def create(self, data: Dict[str, Any]) -> Any:
        """ create a new model """

    @abstractmethod
    def get_by_id(self, record_id: Any) -> Optional[Any]:
        """ get a model by its id """

    @abstractmethod
    def update(self, record_id: Any, data: Dict[str,Any]) -> Optional[Any]:
        """ update a record by ID """

    @abstractmethod
    def delete(self, record_id: Any) -> bool:
        """ delete a record by its id """

    @abstractmethod
    def list(self, limit: int = 100, offset: int = 0) -> List[Any]:
        """ list all records """


