from __future__ import annotations

from typing import TYPE_CHECKING

from capstoneProj.scenes.hero_creation.hero_creation_states.hero_creation_choose_class_state import (
    CharacterCreationChooseClassState,
)
from capstoneProj.scenes.hero_creation.hero_creation_states.hero_creation_choose_name_state import (
    CharacterCreationChooseNameState,
)
from capstoneProj.scenes.hero_creation.hero_creation_states.hero_creation_states import (
    CharacterCreationStates,
)
from capstoneProj.scenes.scene import Scene


if TYPE_CHECKING:
    from capstoneProj.game.game import Game


class CharacterCreationScene(Scene):
    def __init__(self, game: Game):
        super().__init__(game=game)
        self.current_state = CharacterCreationChooseNameState(self)

    def change_state(self, new_state: CharacterCreationStates):
        if new_state == CharacterCreationStates.CHOOSE_CLASS:
            self.current_state = CharacterCreationChooseClassState(self)
        elif new_state == CharacterCreationStates.CHOOSE_NAME:
            self.current_state = CharacterCreationChooseNameState(self)
        else:
            raise ValueError(f"Invalid state: {new_state}")
