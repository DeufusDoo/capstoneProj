from dotenv import load_dotenv

from capstoneProj.game.game import RPGGame
from capstoneProj.game.game_config import RPGConfig

env_files = [
    "config/.env.secret",
]

for env_file in env_files:
    load_dotenv(env_file)

if __name__ == "__main__":
    game = RPGGame(config=RPGConfig("config/game_config.yaml"))
    game.run()
