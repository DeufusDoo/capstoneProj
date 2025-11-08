from __future__ import annotations
from typing import TYPE_CHECKING

from capstoneProj.scenes.battle.battle_scene import BattleScene
from capstoneProj.scenes.game_over.game_over_scene import GameOverScene
from capstoneProj.scenes.hero_creation.hero_creation_scene import HeroCreationScene
from capstoneProj.scenes.main_menu.main_menu_scene import MainMenuScene
from capstoneProj.scenes.resting_hub.resting_hub_scene import RestingHubScene
from capstoneProj.scenes.scene import Scene
from capstoneProj.systems.battle.enemy_generator import generate_enemy
from capstoneProj.systems.battle.enemy_scaling import scale_enemy
from capstoneProj.systems.battle.enemy import Enemy

if TYPE_CHECKING:
    from capstoneProj.game.game import Game


class SceneFactory:
    def __init__(self, game: Game):
        self.game = game

    def get_initial_scene(self) -> Scene:
        return self.get_main_menu_scene()

    def _get_enemy(self) -> Enemy:
        enemy = generate_enemy(game=self.game)

        scale_enemy(
            enemy=enemy, battles_won=self.game.battles_won, game_config=self.game.config
        )

        return enemy

    def get_battle_scene(self) -> BattleScene:
        enemy = self._get_enemy()
        return BattleScene(game=self.game, enemy=enemy)

    def get_resting_hub_scene(self) -> RestingHubScene:
        return RestingHubScene(game=self.game)

    def get_hero_creation_scene(self) -> HeroCreationScene:
        return HeroCreationScene(game=self.game)

    def get_game_over_scene(self) -> GameOverScene:
        return GameOverScene(game=self.game)

    def get_main_menu_scene(self) -> MainMenuScene:
        return MainMenuScene(game=self.game)
