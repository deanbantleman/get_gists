# Overview
Code that will list Github Gists

# Environment
This code was executed on a Windows 10 machine and the Windows Subsystem for Linux (WSL) was used to host an Ubuntu 20.04.6 execution environment.

# Setup your local environment

1. Clone the repo to your local system:

```
  git clone git@github.com:deanbantleman/get_gists.git
```

2. Change directory into the source code directory:

```
  cd get_gists
```

3. Create a local python environment:

```
  virtualenv env
```

4. Source the virtual environment:

```
  . env/bin/activate
```

5. Check you are executing the correct Python:

```
   which python
```

6. Install libraries:

```
  pip install pprintpp
  pip install requests
```

# Running the code

```
python3 get_gist.py <username>
# Where <username> is a valid GitHub username.
# Example: python3 get_gist.pydeanbantleman
```
