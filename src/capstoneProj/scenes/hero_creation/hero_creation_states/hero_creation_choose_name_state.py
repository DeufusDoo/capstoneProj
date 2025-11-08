from __future__ import annotations
from dataclasses import dataclass

from capstoneProj.scenes.hero_creation.hero_creation_states.hero_creation_states import (
    CharacterCreationStates,
)
from capstoneProj.scenes.state import State

from typing import TYPE_CHECKING

from capstoneProj.utils.rendering import render_state_transition_header

if TYPE_CHECKING:
    from capstoneProj.scenes.hero_creation.hero_creation_scene import CharacterCreationScene


@dataclass
class ChosenName:
    name: str
    is_valid: bool


class CharacterCreationChooseNameState(State):
    def __init__(self, scene: CharacterCreationScene):
        self.scene = scene
        self.display_state_transition_header = True
        self.display_name_prompt = True
        self.chosen_name: ChosenName | None = None

    def _get_name(self) -> ChosenName:
        name = input()
        if len(name) > 10:
            return ChosenName(name=name, is_valid=False)
        return ChosenName(name=name, is_valid=True)

    def handle_input(self):
        self.chosen_name = self._get_name()

    def update(self):
        self.display_name_prompt = False
        self.display_state_transition_header = False
        if self.chosen_name and self.chosen_name.is_valid:
            self.scene.game.hero.name = self.chosen_name.name
            self.scene.change_state(CharacterCreationStates.CHOOSE_CLASS)

    def _ask_for_name(self):
        print("Please enter a name for your character (max 10 characters):")

    def render(self):
        if self.display_state_transition_header:
            render_state_transition_header(
                "Character Creation: Name",
            )
        if self.display_name_prompt:
            self._ask_for_name()
        if self.chosen_name and not self.chosen_name.is_valid:
            print(f"Name {self.chosen_name.name} is too long.")
            print("Please enter a name for your character (max 10 characters): ")
