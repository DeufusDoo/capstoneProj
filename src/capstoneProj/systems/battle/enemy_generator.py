from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict
from capstoneProj.systems.battle.enemy import Enemy, EnemyArchetypes

if TYPE_CHECKING:
    from capstoneProj.game.game import Game


@dataclass
class BaseEnemyInfo:
    name: str
    description: str
    archetype: EnemyArchetypes
    ascii_render: str


rat = BaseEnemyInfo(
    name="Rat",
    description="A small, scurrying rodent with sharp teeth and a quick bite",
    archetype=EnemyArchetypes.ATTACKER,
    ascii_render= r"""
   (\_/)
   (o o)
   /\./\
  ( )"( )
  /\| |/\   )
 (  " "  ) /
  \ /~\ /\(_
   \| |/  \_)
   "   "  
""",
)

system_error = BaseEnemyInfo(
    name="SYSTEM ERROR",
    description="Rouge AI born from a failed defense protocol",
    archetype=EnemyArchetypes.TANK,
    ascii_render= r"""
                  ,--.    ,--.
                 ((O ))--((O ))
               ,'_`--'____`--'_`.
              _:  ____________  :_
             | | ||::::::::::|| | |
             | | ||::::::::::|| | |
             | | ||::::::::::|| | |
             |_| |/__________\| |_|
               |________________|
            __..-'            `-..__
         .-| : .----------------. : |-.
       ,\ || | |\______________/| | || /.
      /`.\:| | ||  __  __  __  || | |;/,'\
     :`-._\;.| || '--''--''--' || |,:/_.-':
     |    :  | || .----------. || |  :    |
     |    |  | || '----SSt---' || |  |    |
     |    |  | ||   _   _   _  || |  |    |
     :,--.;  | ||  (_) (_) (_) || |  :,--.;
     (`-'|)  | ||______________|| |  (|`-')
      `--'   | |/______________\| |   `--'
             |____________________|
              `.________________,'
               (_______)(_______)
               (_______)(_______)
               (_______)(_______)
               (_______)(_______)
              |        ||        |
              '--------''--------'
""",
)

haunted_vroom_vroom = BaseEnemyInfo(
    name="Haunted Vroom Vroom",
    description="No driver. No mercy. Just engine",
    archetype=EnemyArchetypes.TANK,
    ascii_render= r"""
                                    _..-------++._
                             _.-'/ |      _||  \"--._
                       __.--'`._/_\j_____/_||___\    `----.
                  _.--'_____    |          \     _____    /
                _j    /,---.\   |        =o |   /,---.\   |_
               [__]==// .-. \\==`===========/==// .-. \\=[__]
                 `-._|\ `-' /|___\_________/___|\ `-' /|_.'     
                       `---'                     `---'
    """,
)


ursa = BaseEnemyInfo(
    name="Ursa",
    description="Apex predator build in a lab to end you",
    archetype=EnemyArchetypes.DEFENDER,
    ascii_render= r"""
    
 .'"'.        ___,,,___        .'``.
: (\  `."'"```         ```"'"-'  /) ;
 :  \                         `./  .'
  `.                            :.'
    /        _         _        \
   |         0}       {0         |
   |         /         \         |
   |        /           \        |
   |       /             \       |
    \     |      .-.      |     /
     `.   | . . /   \ . . |   .'
       `-._\.'.(     ).'./_.-'
           `\'  `._.'  '/'
             `. --'-- .'
               `-...-'
""",
)


mek = BaseEnemyInfo(
    name="Mek",
    description="Just a huge mech",
    archetype=EnemyArchetypes.DEFENDER,
    ascii_render= r"""
             //                                               \\
           /'/                                                 \`\
         [\_/                                                   \_/]
         I  |..,                                             ...|  I
         [__]-~                                               ~-[__]
         || H                                                   H ||
         || ||                    _________                    || ||
         ||  ||                  /  _   _  \                  ||  ||
         ||  ||                 | |(_) (_)| |                 ||  ||
          L| /\                 | |__   __| |                 /\ L|
 _________|/'_ \________________|___]___[___|________________/ _`\|_________
          | (_) |------[ ______               ______ ]------| (_) |
 ---...___I     `\______\ ._ ```---.__ __.---''' _. /______/'     I___...---
          ~~~~----'~~~~/_\  ^\_       ~       _/^  /_\~~~~`----~~~~
                           \  ~-.           .-~  /
                          /_\    \         /    /_\
                              \    \     /    /
                             /_\     \_/     /_\
                                \___________/
                                / /       \ \
                              /' /         \ `\
                            /'  /           \  `\
                        __/____/__         __\____\__
                        \  (_)  /           \  (_)  /
                         |\   /               \   /|
                         ||\/||               ||\/||
                         ||  ||               ||  ||
                         ||  ||               ||  ||
                         |H  H|               |H  H|
                      .---H--H---.         .---H--H---.
                     /^\__|__|__/^\       /^\__|__|__/^\
                     |/'   \/   `\|       |/'   \/   `\|       

    """,
)

the_hollow_man = BaseEnemyInfo(
    name="The Hollow Man",
    description="Skeleton wanting destruction",
    archetype=EnemyArchetypes.TANK,
    ascii_render= r"""
                  .7
                .'/
               / /
              / /
             / /
            / /
           / /
          / /
         / /         
        / /          
      __|/
    ,-\__\
    |f-"Y\|
    \()7L/
     cgD                            __ _
     |\(                          .'  Y '>,
      \ \                        / _   _   \
       \\\                       )(_) (_)(|}
        \\\                      {  4A   } /
         \\\                      \uLuJJ/\l
          \\\                     |3    p)/
           \\\___ __________      /nnm_n//
           c7___-__,__-)\,__)(".  \_>-<_/D
                      //V     \_"-._.__G G_c__.-__<"/ ( \
                             <"-._>__-,G_.___)\   \7\
                            ("-.__.| \"<.__.-" )   \ \
                            |"-.__"\  |"-.__.-".\   \ \
                            ("-.__"". \"-.__.-".|    \_\
                            \"-.__""|!|"-.__.-".)     \ \
                             "-.__""\_|"-.__.-"./      \ l
                              ".__""|>G>-.__.-">       .--,_
                                  ""  G,      
""",
)

door = BaseEnemyInfo(
    name="Door",
    description="It's a door......doOr is it?",
    archetype=EnemyArchetypes.DEFENDER,
    ascii_render= r"""
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________|
""",
)

conspiracy_theorist = BaseEnemyInfo(
    name="Conspiracy Theorist",
    description="Doesn't believe in anything, even in his own mortality",
    archetype=EnemyArchetypes.ATTACKER,
    ascii_render= r"""
        .-"      "-.
       /            \
      |              |
      |,  .-.  .-.  ,|
      | )(_o/  \o_)( |
      |/     /\     \|
      (_     ^^     _)
       \__|IIIIII|__/
        | \IIIIII/ |
        \          /
         `--------`
       / ~~~~~~~~ \
      / | | | | | | \
     /  | | | | | |  \
     \  | | | | | |  /
      `~~~~~~~~~~~~`

     "They're watching us..."
""",
)


zephyros = BaseEnemyInfo(
    name="Zephyros",
    description="A cunning and ancient dragon with scales that shimmer like the night sky",
    archetype=EnemyArchetypes.ATTACKER,
    ascii_render= r"""
                      ___====-_  _-====___
                _--^^^#####//      \\#####^^^--_
             _-^##########// (    ) \\##########^-_
            -############//  |\^^/|  \\############-
          _/############//   (@::@)   \\############\_
         /#############((     \\//     ))#############
        -###############\\    (oo)    //###############-
       -#################\\  / "" \  //#################-
      -###################\\/  .  \//###################-
     _#/|##########/\######(   )######/\##########|\#_
    |/ |#/\#/\#/\/  \#/\#|/\#|/\#  /\#/\#/\#/\| \|/|/
    / / _/ /_/ |   |_/_/__/___/_/ | /_/ /_/ // //\ 
    \/\/\/_/ |_/  _/ /_/ \__/  | /_/ /_/ /_/ /_/
            /_/ |_/ /_/  /_/ | /_/ /_/ /_/ /_/ /
           (_/   /_/ |_/(_/  /_/ /_/  /_/ /_/
           (_/   (_/ (_/   (_/  (_/ (_/
""",
)

battles_won_to_enemies_mapping: Dict[int, BaseEnemyInfo] = {
    0: rat,
    1: system_error,
    2: haunted_vroom_vroom,
    3: ursa,
    4: mek,
    5: the_hollow_man,
    6: door,
    7: conspiracy_theorist,
    8: zephyros,
}


def generate_enemy(game: Game) -> Enemy:
    battles_won = game.battles_won
    enemy_info = battles_won_to_enemies_mapping[battles_won]
    return Enemy(
        name=enemy_info.name,
        description=enemy_info.description,
        level=1,
        base_stats=game.config.base_enemy_stats,
        llm=game.llm,
        enemy_next_action_prompt=game.config.enemy_next_action_prompt,
        archetype=enemy_info.archetype,
        ascii_render=enemy_info.ascii_render,
    )
