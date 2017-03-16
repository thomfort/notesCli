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
export NOTES_PATH=~/.notes
```

Add notes in your path
```
export PATH=~/Codes/notesCli/bin:$PATH
```

## Examples
### Add note
```
$ notes @foo @bar My first note
```

### List notes
```
$ notes @foo
@foo
*  My first note
```
