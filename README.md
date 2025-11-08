# capstoneProj

capstoneProj is a role-playing game project that leverages large language models (LLMs) to create dynamic gameplay experiences. This fork currently supports character creation and a battle system, and includes modifications from the original LLM-RPG project, such as renaming "Hero" to "Character."

## Current / Future Features

- **Dynamic Battles**: Engage in battles where both characters and enemies use AI to determine actions and effects.  
- **Character Customization**: Define your character's stats, class, and abilities.  
- **AI-Powered Creativity**: Use creative language to influence battle outcomes.  

## Installation

1. Clone your forked repository:

```bash
git clone https://github.com/yourusername/capstoneProj.git
cd capstoneProj
```

2. Install dependencies using Poetry:

   ```bash
   poetry install
   ```

3. Make Environment variable. Need to set the 'GROQ_API_KEY' to use the GroqLLM model. To do this create a '.env.secret' file in the 'config' direcotry:

    ```plaintext
    GROQ_API_KEY=your_api_key
    ```
To get API key you can go [here](https://groq.com/). This should generate a key and give you free tokens each day :)

## Play

4. To start the game just run this command:

```bash
poetry run python -m capstoneProj
```
