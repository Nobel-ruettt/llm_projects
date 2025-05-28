# Setup instructions for PC

### Pre Install
1. Permissions. Please take a look at this [tutorial](https://chatgpt.com/share/67b0ae58-d1a8-8012-82ca-74762b0408b0) on permissions on Windows  
2. Anti-virus, Firewall, VPN. These can interfere with installations and network access; try temporarily disabling them as needed  
3. The evil Windows 260 character limit to filenames - here is a full [explanation and fix](https://chatgpt.com/share/67b0afb9-1b60-8012-a9f7-f968a5a910c7)! You'll need to restart after making the change.  
4. If you've not worked with Data Science packages on your computer before, you'll need to install Microsoft Build Tools. Here are [instructions](https://chatgpt.com/share/67b0b762-327c-8012-b809-b4ec3b9e7be0).     

### Part 1: Install Cursor
1. Visit cursor at https://www.cursor.com/
2. Click Sign In on the top right, then Sign Up, to create your account
3. Download and follow its instructions to install and open Cursor

After you start Cursor, you can pick the defaults for all its questions.  
When it's time to open the project in Cursor:  
1. Launch Cursor, if it's not already running  
2. File menu >> New Window  
3. Click "Open project"  
4. Navigate into the project root directory called `agents` (probably within projects) and click Open
5. When your project opens, you may be prompted to "install recommended extensions" for Python and Jupyter. If so, choose Yes! Otherwise:
- Open extensions (View >> extensions)
- Search for python, and when the results show, click on the ms-python one, and Install it if not already installed
- Search for jupyter, and when the results show, click on the Microsoft one, and Install it if not already installed


### Part 2: The amazing `uv`
Follow the instructions here to install uv - I recommend using the Standalone Installer approach at the very top:

https://docs.astral.sh/uv/getting-started/installation/

Then within Cursor, select View >> Terminal, to see a Terminal window within Cursor.  
Type `pwd` to see the current directory, and check you are in the 'agents' directory - like `C:\Users\YourUsername\Documents\Projects\agents` or similar

Start by running `uv self update` to make sure you're on the latest version of uv.

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

When you have the key, it's time to create your `.env` file:

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

2. Now go to File menu >> Save As.. and save the file in the directory called `agents` (also known as the project root directory) with the name `.env`  

Here's the thing: it **needs** to go in the directory named `agents` and it **needs** to be named precisely `.env` -- not "env" and not "env.txt" or ".env.txt" but exactly the 4 characters `.env` otherwise it won't work!! 

Hopefully you're now the proud owner of your very own `.env` file with your key inside, and you're ready for action.

**IMPORTANT: be sure to Save the .env file after you edit it.**

## And that's it!!
