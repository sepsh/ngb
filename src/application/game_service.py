from sqlalchemy.orm import Session

from src.application.dto import GameDTO
from src.data.models import Game


class GameService:

    @staticmethod
    def create_game(game: GameDTO, session: Session) -> int:
        game_entity = Game(title=game.title, description=game.description, type_=game.type_)

        session.add(game_entity)
        session.commit()  # Commit ensures the ID is generated
        session.refresh(game_entity)  # Ensures latest DB state

        return game_entity.id
