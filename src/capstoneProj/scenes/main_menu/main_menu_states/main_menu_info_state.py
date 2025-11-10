from __future__ import annotations

from textwrap import dedent

from capstoneProj.scenes.main_menu.main_menu_states.main_menu_states import MainMenuStates
from capstoneProj.scenes.state import State

from typing import TYPE_CHECKING

from capstoneProj.utils.rendering import render_state_transition_header
from capstoneProj.utils.user_navigation_input import (
    UserNavigationInput,
    get_user_navigation_input,
)

if TYPE_CHECKING:
    from capstoneProj.scenes.main_menu.main_menu_scene import MainMenuScene


class MainMenuInfoState(State):
    def __init__(self, scene: MainMenuScene):
        self.scene = scene
        self.display_state_transition_header = True
        self.display_info = True
        self.last_user_navigation_input: UserNavigationInput | None = None

    def handle_input(self):
        self.last_user_navigation_input = get_user_navigation_input([1])

    def update(self):
        self.display_info = False
        self.display_state_transition_header = False
        if self.last_user_navigation_input.is_valid:
            if self.last_user_navigation_input.choice == 1:
                self.scene.change_state(MainMenuStates.NAVIGATION)

    def _render_game_info(self):
        print(
            dedent(
                """
            Select a character class and face a series of tougher enemies. You type your actions freely, and a Large Language Model (LLM) will decide what happens. The LLM considers your character's class, items, and the battle contex, and then calculates how feasible your action is (how realistic in world) as well as the potential damage.

            Your character also has core attributes:
            - Attack: determines the damage you inflict
            - Defense: reduces the damage you take
            - HP: how much damage you can endure
            - Focus: controls how many letter you can type per turn

            Choose an option:
            [1] Back to main menu
            """
            )
        )

    def _render_invalid_choice(self):
        print("Invalid choice. Choose [1]")

    def render(self):
        if self.display_state_transition_header:
            render_state_transition_header(
                "Info",
            )
        if self.display_info:
            self._render_game_info()
        if (
            self.last_user_navigation_input
            and not self.last_user_navigation_input.is_valid
        ):
            self._render_invalid_choice()
