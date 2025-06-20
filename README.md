# Setup instructions for PC

### Pre Install
1. Permissions. Please take a look at this [tutorial](https://chatgpt.com/share/67b0ae58-d1a8-8012-82ca-74762b0408b0) on permissions on Windows  
2. Anti-virus, Firewall, VPN. These can interfere with installations and network access; try temporarily disabling them as needed  
3. The evil Windows 260 character limit to filenames - here is a full [explanation and fix](https://chatgpt.com/share/67b0afb9-1b60-8012-a9f7-f968a5a910c7)! You'll need to restart after making the change.  
4. If you've not worked with Data Science packages on your computer before, you'll need to install Microsoft Build Tools. Here are [instructions](https://chatgpt.com/share/67b0b762-327c-8012-b809-b4ec3b9e7be0).     

### Part 1: Install Cursor or Visual Studio Code
1. Visit the cursor at https://www.cursor.com/
2. Click Sign In on the top right, then Sign Up, to create your account
3. Download and follow its instructions to install and open Cursor

I used Visual Studio Code because I can utilize the free GitHub Copilot for code completion, and it's similar to the cursor functionality.


### Part 2: The amazing `uv`
Follow the instructions here to install uv - I recommend using the Standalone Installer approach at the very top:

https://docs.astral.sh/uv/getting-started/installation/

Go to terminal of the current project directory

Start by running `uv self update` to ensure you're on the latest version of UV.

One thing to watch for: if you've used Anaconda before, make sure that your Anaconda environment is deactivated   
`conda deactivate`  
And if you still have any problems with conda and python versions, it's possible that you will need to run this too:  
`conda config --set auto_activate_base false`  

And now simply run:  
`uv sync`  
And marvel at the speed and reliability! If necessary, uv should install python 3.12, and then it should install all the packages.  
If you get an error about "invalid certificate" while running `uv sync`, then please try this instead:  
`uv --native-tls sync`  
And also try this instead:  
`uv --allow-insecure-host github.com sync`

Finally, run these commands to be ready to use CrewAI:  
`uv tool install crewai`   
Followed by:  
`uv tool upgrade crewai`  

Checking that everything is set up nicely:  
1. Confirm that you now have a folder called '.venv' in your project root directory (agents)
2. If you run `uv python list` you should see a Python 3.12 version in your list (there might be several)
3. If you run `uv tool list` you should see crewai as a tool

Just FYI on using uv:  
With uv, you do a few things differently:  
- Instead of `pip install xxx` you do `uv add xxx` - it gets included in your `pyproject.toml` file and will be automatically installed next time you need it  
- Instead of `python my_script.py` you do `uv run my_script.py` which updates and activates the environment and calls your script  
- You don't actually need to run `uv sync` because uv does this for you whenever you call `uv run`  
- It's better not to edit pyproject.toml yourself, and definitely don't edit uv.lock. If you want to upgrade all your packages, run `uv lock --upgrade`
- uv has really terrific docs [here](https://docs.astral.sh/uv/) - well worth a read!

### Part 3: The `.env` file

you have to create a file name '.env' in the root directory for all the credentials. where you will save the OPENAI_API_KEY and other api keys 
this are the environment variables which can be accessed in the code.

1. In Cursor, go to the File menu and select "New Text File".

Type the following, being SUPER careful that you get this exactly right:

`OPENAI_API_KEY=`

And then after the equals sign, paste in your key from OpenAI. So after you've completed this, it should look like this:

`OPENAI_API_KEY=sk-proj-lots_of_characters_here`

But obviously the stuff to the right of the equals sign needs to match your key exactly.

Some people have got stuck because they've mistyped the start of the key as OPEN_API_KEY (missing the letters AI) and some people have the value as `sk-proj-sk-proj-...`.

If you have other keys, you can add them too, or come back to this in future weeks:  
```
GOOGLE_API_KEY=xxxx
ANTHROPIC_API_KEY=xxxx
DEEPSEEK_API_KEY=xxxx
```


### CrewAi Commands:

1. Create your crew by using cmd crewai create crew latest-ai-development
2. Run Crew by using cmd crewai run

When running the crew remember you are in the crew project folder where the crew was created

## And that's it!!
