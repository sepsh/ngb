from sqlmodel.orm.session import Session

from src.application.dto import GameDTO
from src.data.models import Game


class GameService:

    @staticmethod
    def create_game(game: GameDTO, session: Session) -> int:
        game_entity = Game(title=game.title, description=game.description, type_=game.type_)
        with session as session:
            session.add(game_entity)
            session.commit()
            session.flush()
            session.refresh(game_entity)
            session.expunge_all()
        return game_entity.id
