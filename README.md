# NotesCli
Take note from cli using tag

## Installation
You need to create new environment variable NOTES_PATH with the folder where you want to put your notes. 

Create folder
```
mkdir ~/.notes
```
Insert variable into your .bash_profile or .zshrc
```
export NOTES_PATH=$HOME/.notes
# Fish
set -x NOTES_PATH $HOME/.notes
```

Add notes in your path. In this example I put my code into ~/Codes.
```
export PATH=$HOME/Codes/notesCli/bin:$PATH
# Fish 
set PATH $HOME/Codes/notesCli/bin $PATH
```

## Examples
### Add note
```bash
$ notes @foo @bar My first note
['foo', 'bar']
 My first note

$ notes @py "My command line" @tips
['py', 'tips']
 My command line @tips
```

### List notes
```
$ notes @foo
@foo
*  My first note
```

### List tags
```
$ notes tags
```