---
layout: lesson
root: ../..
github_username: your_user_id
bootcamp_slug: yyyy-mm-dd-site
title: Fast-paced or Intermediate Shell
---

## What is shell and why am I about to learn it?

The shell is a computer program with a *command-line interface* (CLI), which means that you interact with the program by typing a command in a terminal.
This is in contrast to many modern computer programs, which have a *graphical user interface* (GUI) that you interact with by clicking on  icons with a mouse.
While GUIs tend to be prettier and more intuitive, CLIs have their inherent advantages too:

* Run from anywhere! CLIs are typically how you access remote computer resources like supercomputers or web servers, and how you interact with those computers once you get there.
* Typing at a keyboard tends to be more ergonomic than mousing, so your wrists will thank you.
* CLIs make your work easier and faster to document and reproduce—just copy and paste those commands.
* Using a CLI makes you feel like a l33t hax0r ;)

Shell is a CLI to your computer's operating system.
There are many shell programs, and we'll be using a popular one called [bash](http://en.wikipedia.org/wiki/Bash_(Unix_shell)).

Shell is not the only CLI out there—Python, Matlab, Git, PyMol, and many other scientific software applications can be accessed by a command line too.
So getting comfortable at a command line will come in handy in lots of contexts.

In particular, shell's strengths include:

1. Interacting with the file system to create, find, organize, and generally slice and dice files and folders.
2. Using just the right tool for the job, or building your own tool out of components that play nicely together.
3. Automating routine tasks—with a shell script, it's as easy to rename 1000 files as to rename 1, or to run your snazzy new analysis on last year's samples as on yesterday's.
4. Learning about and modifying the internal guts of your computer.
5. Surprisingly sophisticated calculations.

Not by coincidence, this is also an outline for this lesson.

## <a name="prompt"></a> The prompt

Let's get started by opening up a terminal.
(On Windows, open Git Bash. On a Mac, go to your Applications folder, Utilities subfolder, and open the application called Terminal. On the Linux virtual machine, double click on the Terminal shortcut on the desktop.)
You should see something like this:

	anna$

This is the *prompt*, where you can type commands and see their results. We haven't given any commands, so there are no results to see yet.

First command: computer, tell me where I am!
The command for this is `pwd`, which stands for "present working directory".
(Shell commands are often somewhat cryptic abbreviations for the thing that they do,
and it's easier to keep them all straight if you can remember what they stand for;
check the [cheat sheet](#cheat) at the end if you get lost.)

At the prompt, type `pwd` and hit Return.
(In this lesson, anytime you're asked to type a command that's `formatted like this`, type that at the terminal prompt then hit Return.)
Immediately, the path to a directory (aka folder) should appear, followed by a fresh prompt.

	anna$ pwd
	/Users/anna
	anna$ 


What just happened?
Your computer *read* the `pwd` command you gave it, *evaluated* the command to figure out what directory you're in, *printed* the result on the screen, and got you all set up to give it another command.
This workflow is called a *read-eval-print loop* (REPL) and it's a big part of why I love shell and other CLIs so much—it encourages you to engage in a fast, fluid, back-and-forth conversation with your computer about whatever you're trying to do.

> Hey computer, try this out?

> Hey human, this is what happens.

> Hey computer, that's only sorta what I wanted, how about you try it this way?

REPL means that you don't need to really know what you're trying to do before you start trying to do it, because you and the computer can figure it out together as you go.

REPL also means that shell is a turn-based game—you can type anything you want,
and nothing happens until you press return.


## <a name="files"></a> The file system: better safe than sorry

One place where REPL makes a big difference is in file management.
Everything you can do in a file manager like 
Windows Explorer or Mac Finder, you can do in shell,
with one key difference: it's a whole lot harder to undo destructive changes like deleting a file.
But with REPL, it's easy to hedge your bets, check your work, and explore the unintended consequences of your actions before you take the leap.
This kind of "defensive programming" mindset is also helpful in testing software written in other languages.

Before we look at some examples, here's a quick reference for how to replace your old boring GUI file manager! Here, "safe" means that you will never *accidentally* change anything by running that command.

| Thing to do | How you do it | What's that short for? | Safe? |
|:----------- |:------------- |:---------------------- |:----- |
| Find out what's in a folder | `ls` | list | yes |
| Find out extra info about what's in a folder | `ls -l` | list, long format | yes |
| Go somewhere new | `cd` | change directory | yes |
| Make a new empty folder | `mkdir` | make directory | yes |
| Make a new empty file | `touch` | "touch" a location in the file system | no |
| Copy a file | `cp` | copy | no |
| Copy a folder | `cp -r` | copy recursively | no |
| Move something | `mv` | move | no |
| Rename something | `mv` | yep, `mv` again! "move" to a new name | no |
| Delete a file | `rm` | remove | no |
| Delete a folder and its contents | `rm -r` | remove recursively | no |
| Delete things, but ask me first | `rm -i` | remove interactively | no |

Let's see some of those commands in action. First, let's create a safe place for us to play:

	mkdir playground
	cd playground

How do you know our playground is safe?
Well, we expect our brand-new directory to be empty, so we can check that it has no files in it by making sure that `ls` has no output.
`ls` is a safe command, and it's a great one to run early and often.

### Interlude

Follow along with these excercises to discover some surprising shell features and gotchas.

**mv and cp are unsafe**

Which files are present after each command? This is why `mv` is unsafe (`cp` is unsafe for the same reason).

	touch better.txt
	cp better.txt faster.txt
	ls
	cp better.txt stronger.txt
	ls
	mv faster.txt stronger.txt
	ls

`mv` acts a bit differently for files and folders... This is also an example of using `ls` to look inside a different directory from the one you're in, and demonstrates that `touch` doesn't care what the file extension is.

	mkdir thesis
	touch figure.png
	ls
	mv figure.png thesis
	ls
	ls thesis
	mkdir introduction
	ls
	mv introduction thesis
	ls
	ls thesis
		

**touch is a little bit unsafe**

Wait a minute in between these two `touch` commands, and keep your eye on the time stamps (the bit just to the left of the file name). This is why `touch` is technically unsafe (even though the unintended consequence is often unimportant).

	touch data.txt
	ls -l
	touch data.txt
	ls -l

**mkdir is safe**

Your first error message! This is why I say that `mkdir` is safe even though it causes *non-accidental* changes (i.e., it makes you that folder you asked for!).

	mkdir experiments
	ls
	mkdir experiments
	ls

**Doing it faster**

Where do these paths lead? Which are *relative* to the current directory, and which are absolute (i.e., would give you the same result regargless of the current directory)? (Extra credit: check out [even more paths](http://en.wikipedia.org/wiki/Path_(computing)).)

	cd thesis
	ls .
	ls ..
	ls ../experiments
	ls ~
	ls /
	cd -

Pressing the tab button is almost as good as mind reading (and an excellent way to avoid typos).

	t<tab><tab>
	to<tab><tab>
	tou<tab>
	ls e<tab>

Wildcards: `*` is a substitute for any string of characters (even of length 0), and `?` is a substitute for any one character. (Extra credit: check out [even more wildcards](http://www.tldp.org/LDP/GNU-Linux-Tools-Summary/html/x11655.htm).)

	ls *txt
	ls *er*
	touch thesis/figure2.png
	ls thesis/figure*.png
	touch butter.txt blotter.txt
	ls b?tter.txt

**Delete files, keep your piece of mind**

Suppose you want to delete all the figures in the thesis directory.
Who needs those figures anyway?
Before you do anything with `rm`, try to find an `ls` command that will list all the files you want to delete, and only the files you want to delete.
(Hint: we saw one in the previous excercise.)
Then, and only then, replace `ls` with `rm` in that command, and press return knowing that you're only trashing the files you no longer care about.

Congrats, you are practicing safe shell!


## <a name="rtfm"></a> RTFM

In the previous section, we saw that some commands (like `ls`) can take *flags* (optional arguments that start with a hyphen, like `-l`).
There are far more flags than I can remember, and the same flag usually has a different effect when it's used with a different command.
How can you keep track of it all?

In a word, RTFM.

RTFM stands for "read the f**ing manual".
This is the computer-speak equivalent of "teach a man to fish"—really, it's more like "teach a man to teach himself how to fish."
Reading manuals (or querying Google or [Stack Overflow](http://stackoverflow.com)) is something that everyone does, from novice to expert,
because it's such a powerful way to get yourself out of computer-related troubles.
We're going to cover a lot of material today, so I want to make sure you get really good at RTFM so you can review the material afterward, fill in any missing details, and keep learning.
Of course, RTFM is complementary to "ask a f**ing human"—don't hesitate to talk with the people around you :)

In shell, the manual is called `man`, short for manual.
`man` includes documentation for everything else that we'll be covering, including `man` itself!

Let's try it out by reading the "man page" for ls, by typing `man ls`.
Everything else in the terminal should disappear and be replaced with a description of the `ls` command.
There's a very concise description under **NAME**, a quick reference for what to type under **SYNOPSIS**, a long description all the flags under **DESCRIPTION**, etc.
Press the arrow buttons or the space bar to scroll down and view the rest of the "man page."
Read the description for `-l` and any of the other flags that strike your fancy.
(Some of my favorites are `-a`, `-h`, and `-t`.)
When you're ready, you can get back to your terminal by typing `q` for quit.

Now try out your newly-found flags!
You can also use multiple flags at once:
for instance, `-h` isn't useful by itself, but it is when combined with `-l` (`ls -lh` and `ls -l -h` both work).


## <a name="tools"></a> Tools of the trade

Looking at the outside of empty files is only fun for so long... Let's start to look inside.

### Just a peek

Start by downloading the PDB file for a protein I worked on for my PhD:
LHCII, the light-harvesting complex in plants.
You can download things right from the command line using `curl` (that's like URL),
and unzip them using `gunzip`.
(Extra credit: check out the man pages for these!)

	curl -O http://www.rcsb.org/pdb/files/1RWT.pdb.gz
	gunzip 1RWT.pdb.gz

How big is the pdb file? We already know that command:

	anna$ ll -h 1RWT.pdb
	-rw-r--r--+ 1 anna  staff   3.5M Mar 16 21:54 1RWT.pdb

3.5 megabytes, that's not small... how many lines is that? `wc` for word count gives three statistics: the number of lines, the number of words, and the number of characters.

	anna$ wc 1RWT.pdb
	45354  380840 3673674 1RWT.pdb

More than 45 thousand lines—I wouldn't want to open that in Word!
How can we look at the contents anyway?
Shell gives us four main tools for that: `head`, `tail`, `cat`, and `less`.
`cat`, for concatenate, just prints the whole file to the screen—and that's what we *don't* want to do. (The name "concatenate" is because you can use it to print multiple files to the screen, one after another.)
`head` and `tail` print only the first and last 10 lines of a file, respectively.

	anna$ head 1RWT.pdb
	HEADER    PHOTOSYNTHESIS                          17-DEC-03   1RWT              
	TITLE     CRYSTAL STRUCTURE OF SPINACH MAJOR LIGHT-HARVESTING COMPLEX AT 2.72   
	TITLE    2 ANGSTROM RESOLUTION                                                  
	COMPND    MOL_ID: 1;                                                            
	COMPND   2 MOLECULE: CHLOROPHYLL A-B BINDING PROTEIN, CHLOROPLAST;              
	COMPND   3 CHAIN: A, B, C, D, E, F, G, H, I, J;                                 
	COMPND   4 SYNONYM: LHCII TYPE I CAB, LHCP                                      
	SOURCE    MOL_ID: 1;                                                            
	SOURCE   2 ORGANISM_SCIENTIFIC: SPINACIA OLERACEA;                              
	SOURCE   3 ORGANISM_COMMON: SPINACH;
	anna$ tail 1RWT.pdb
	CONECT2891726760
	CONECT2892326694
	CONECT2892426533  
	CONECT2892526643 
	CONECT2898627910 
	CONECT2899127844 
	CONECT2899227683    
	CONECT2899327793  
	MASTER     2884    0  211   95    0    0  728    629039   1011992  180          
	END

And `less` lets you scroll through the file the same way you scrolled through the man pages (getting back to the terminal is the same too, just press `q`).

Yep, that looks like a pdb file!

### Search and filter

Suppose we don't care about all that header and footer material—we just want to extract the positions of all the atoms in the protein.
I know that those lines start with "ATOM", so we can search for those lines using `grep`.
`grep` is an extremely powerful tool for searching within files using a complicated pattern-matching system called *regular expressions*
(hence the "re" in `grep`).
The full power of `grep` is far beyond the scope of this lesson, but I highly recommend you look into it in more depth next time you need some searching awesomeness.

Let's try it:

	grep ATOM 1RWT.pdb

Oops, too much output! At least it looks right...

Luckily, we can limit the output of `grep` by handing that output to something like `head` before letting it print to the screen.
This idea of handing the output of command to the input of another command is called *piping* and it's central to the design of the shell language.
In shell, each command like `grep` or `head` does just one thing really well,
and piping is what lets you get the whole job done by making all the little commands work together.
Many shell commands look for piped input if you don't give them their usual input argument;
for `head`, that means that we leave off the name of a file.
Piping is done with the `|` character, like so:

	anna$ grep ATOM 1RWT.pdb | head
	REMARK   3  NUMBER OF NON-HYDROGEN ATOMS USED IN REFINEMENT.                    
	REMARK   3   PROTEIN ATOMS            : 16619                                   
	REMARK   3   NUCLEIC ACID ATOMS       : 0                                       
	REMARK   3   HETEROGEN ATOMS          : 11721                                   
	REMARK   3   SOLVENT ATOMS            : 699                                     
	REMARK 290 THE FOLLOWING TRANSFORMATIONS OPERATE ON THE ATOM/HETATM             
	REMARK 375 THE FOLLOWING ATOMS ARE FOUND TO BE WITHIN 0.15 ANGSTROMS            
	REMARK 375 OF A SYMMETRY RELATED ATOM AND ARE ASSUMED TO BE ON SPECIAL          
	REMARK 375 ATOM RES CSSEQI                                                      
	REMARK 610 MISSING HETEROATOM 

Oh no, that's not right at all!
`grep` did just what we asked it to do:
it returned every line that contained ATOM, not just the lines with ATOM at the beginning.
The regular expression for "start of a line" is the `^` character,
so to only match occurances of ATOM at the beginning of a line,
we have to search for ^ATOM, like so:

	anna$ grep ^ATOM 1RWT.pdb | head
	ATOM      1  N   SER A  14     -13.921  26.524 129.578  1.00 54.61           N  
	ATOM      2  CA  SER A  14     -14.233  26.685 128.126  1.00 53.16           C  
	ATOM      3  C   SER A  14     -14.808  25.389 127.561  1.00 51.78           C  
	ATOM      4  O   SER A  14     -14.755  24.346 128.217  1.00 52.35           O  
	ATOM      5  CB  SER A  14     -12.965  27.078 127.356  1.00 53.76           C  
	ATOM      6  OG  SER A  14     -11.932  26.125 127.539  1.00 52.81           O  
	ATOM      7  N   PRO A  15     -15.378  25.441 126.342  1.00 49.74           N  
	ATOM      8  CA  PRO A  15     -15.957  24.250 125.716  1.00 47.77           C  
	ATOM      9  C   PRO A  15     -14.891  23.346 125.100  1.00 46.49           C  
	ATOM     10  O   PRO A  15     -15.209  22.294 124.536  1.00 46.15           O  

Whew, that looks more like it.
This was another great example of the power of REPL:
we had to try asking for those lines a few times,
but it looks like we finally have what we want.

### Interlude

* Try piping this same search into `tail` and `wc`. See anything fishy?

* The 3rd column of the pdb file has atom abbreviations (e.g., there's only one CA atom per amino acid), 4th column of the pdb file has the amino acid abbreviations (e.g., SER is serine), and there are two spaces between the columns.
How many serines are in this protein?
 * Hint 1: pipe `grep` into `grep`, then into `wc`!
 * Hint 2: when there are spaces in a search, enclose the whole search string in quotes. For instance, `grep "search for this" in_this_file`.

 * Use `ls` to find any extraneous files in this directory, and delete them with `rm`. Make sure to *not* to delete `1RWT.pdb` though!

### Save your work

You know, now that we have our search working so nicely,
it would be nice if we could save those lines for later.
We can do that using *redirection*.
No, that's not when you try to get your adviser to bug another grad student instead of you,
that's when you direct the output of a shell command into a file.
It's a similar concept to piping, but instead of another command accepting the input, now it's just a file.
You can have an infinite chain of pipes, but redirection ends the chain.
Redirection is done with the `>` character, like so:

	grep ^ATOM 1RWT.pdb > 1RWT_atoms.txt

You can check out your new file `1RWT_atoms.txt` with `ls`, `head`, `tail`, etc., and you should find no surprises.
Now, you can safely delete the original pdb file

## <a name="scripts"></a> Scripting: Programmers are lazy

Let's recap what we did in the last section:

1. Downloaded a zipped file
2. Unzipped it
3. Extracted the part we cared about and saved it in a file
4. Cleaned up

What if you had to process 1000 proteins this way?
By putting the commands to do those steps into a *script*, we'll be able to reuse our hard work next time we have to do the same thing.
Programmers never like to solve the same problem twice when it's easier to reuse their previous solution—and if you have to solve the same problem three times, it's worth coming up with a general solution that you can reuse ad nauseum with as little effort on your part as possible.
This is why [some people](http://threevirtues.com/) say that "good programmers are lazy."

A script is just a file that contains commands written in a programming language.
Shell scripts end in `.sh` by convention, so let's make a blank file with a descriptive name to put our script in:

	touch get_atoms_in_protein.sh

Open this file in your favorite code-friendly text editor (not Word; some suggestions are [here](http://swcarpentry.github.io/2014-03-17-ucb/)).

Scripts are easier to understand if they have *comments*:
purely descriptive notes to yourself and anyone else who comes across the script about what's going on.
Even though comments aren't executed when you run a script,
commenting code is just as important as keeping a lab notebook,
for exactly the same reasons.
In shell, comments are preceded by a `#` character.
Add some comments to your script by typing these lines in your text editor (or whatever other comments you find helpful):

	# download a zipped pdb file

	# unzip the file

	# extract only the atoms, and pipe them into a .txt file

	# clean up by deleting the pdb file

### Interlude

Go back to your terminal and find the commands that actually did those steps,
and copy and paste them into the script on the lines after their respective comments.
You can go through your old commands in several ways:

* scroll up with the mouse
* use the up and down arrows
* press control-r, type a search term like `curl`, and press return
* use the `history` command (try `history | grep curl`)

When you're ready, run the script:

	bash get_atoms_in_protein.sh

Congratulations, you've written a real live program! Now let's make it better :)

In addition to comments, another great way to make a script more understandable is to add informative output commands
(you might call them "print statements" in languages like Python).
The command to print something to the screen is `echo`—you're asking the computer to holla back at you.
For instance,

	anna$ echo hello world
	hello world

Add some output to your script, whatever you find useful.
For instance, when the script is finished,
you could print "Success!"

Yet another improvement is to make the script *executable*.
The command and flag for this is `chmod +x` for CHange MODe to eXecutable.
You can see its effect on the *permissions flags* by checking `ls -l` before and after running `chmod`:

	anna$ ls -l get_atoms_in_protein.sh
    -rw-r--r--+ 1 anna  staff  260 Mar 17 01:14 get_atoms_in_protein.sh
	anna$ chmod +x get_atoms_in_protein.sh
	anna$ ls -l get_atoms_in_protein.sh
    -rwxr-xr-x+ 1 anna  staff  260 Mar 17 01:14 get_atoms_in_protein.sh

You can learn more about permissions [here](http://en.wikipedia.org/wiki/File_system_permissions) and on the man page for `chmod`.
Now you can run the script by simply typing `./get_atoms_in_protein.sh`, no `bash` needed.
To make sure that the computer still knows that it's a bash script, though,
add this line at the very beginning of your script:

	#!/bin/bash

`/bin/bash` is the path to the `bash` executable; `bash` is just a program that knows how to execute other programs.

Check your work: does your script look like mine?
It's ok if it looks different as long as the result is the same!

	anna$ cat get_atoms_in_protein.sh
	#!/bin/bash

	# download a zipped pdb file
	curl -O http://www.rcsb.org/pdb/files/1RWT.pdb.gz

	# unzip the file
	gunzip 1RWT.pdb.gz

	# extract only the atoms, and pipe them into a .txt file
	grep ^ATOM 1RWT.pdb > 1RWT_atoms.txt

	# clean up by deleting the .pdb file
	rm 1RWT.pdb

	# acknowledge success
	echo Success!

### Getting loopy

This is a great solution for processing one protein, but it's *hard-coded* to work for just my favorite protein.
What if we want to do the operations on another protein,
say myoglobin (PDB code 1MBN)?
Let's make the same code do more by putting it inside a *for loop*.
In shell, the syntax for a for loop is `for element in list; do something with ${element}; done`.
This will execute all the commands between `do` and `done` once for every element of the list.
For instance:

	anna$ for word in This is a sentence.; do echo ${word}; done
	This
	is
	a
	sentence.

Make a copy of your script named `get_atoms_in_proteins.sh` (proteins plural), and modify it to run all the protein-specific commands inside a for loop that loops over a list of PDB codes.
For instance, mine looks like

	anna$ cat get_atoms_in_proteins.sh
	#!/bin/bash

	# loop over pdb codes
	for pdb_code in 1RWT 1MBN
	do

	    # report current pdb code
	    echo Working on ${pdb_code}...

	    # download a zipped pdb file
	    curl -O http://www.rcsb.org/pdb/files/${pdb_code}.pdb.gz

	    # unzip the file
	    gunzip ${pdb_code}.pdb.gz

	    # extract only the atoms, and pipe them into a .txt file
	    grep ^ATOM ${pdb_code}.pdb > ${pdb_code}_atoms.txt

	    # clean up by deleting the .pdb file
	    rm ${pdb_code}.pdb

	# end loop
	done

	# acknowledge success
	echo Success!

Now you can add as many PDB codes to the list as you want, and process all of them with a single command!

### Optional interlude

What if you had a file with 1000 PDB codes in it and you wanted to process each of them?
Typing all 1000 codes into the list section of a for loop sounds too annoying—there must be an easier way.
And there is: the syntax `while read line; do something with $line; done < input_file` is like a for loop that runs once for each line in a file.
If there were one PDB code on each line, then we can use *command-line arguments* to pass the PDB code into the script:

	anna$ cat get_atoms_in_protein.sh
	#!/bin/bash

	# get command-line argument
	pdb_code=$1

    # report current pdb code
    echo Working on ${pdb_code}...

    # download a zipped pdb file
    curl -O http://www.rcsb.org/pdb/files/${pdb_code}.pdb.gz

    # unzip the file
    gunzip ${pdb_code}.pdb.gz

    # extract only the atoms, and pipe them into a .txt file
    grep ^ATOM ${pdb_code}.pdb > ${pdb_code}_atoms.txt

    # clean up by deleting the .pdb file
    rm ${pdb_code}.pdb

After you set up your input file (note that the redirect command `>` deletes any preexisting content in the file, while `>>` appends to a file)

	echo 1RWT > pdb_codes.txt
	echo 1MBN >> pdb_codes.txt

...then you can process everything in the file:

	while read line; do ./get_atoms_in_protein.sh $line; done < pdb_codes.txt

Now *that's* a flexible, reproducible, extensible workflow.

## <a name="systems"></a> What's under the hood

Shell is the user interface to your operating system,
and there are shell commands to replace many of your GUI system utilities.

For instance, run `top`. This shows every process that's running on your computer right now, how much CPU and memory it's using, etc.
(Get back to your terminal by pressing `q`.)

Another useful utility is `du` for disk usage.
This gives concise information about how much stuff is stored in a directory,
which is especially useful when you need to figure out who's hogging all the space on a shared computer.
I like to use `du` with the `-h` flag, which does the same thing as the `-h` flag to `ls`.

	anna$ du -h
	  0B	./experiments/theories
	  0B	./experiments
	  0B	./thesis/introduction
	  0B	./thesis
	5.3M	.

Looks like I have a bunch of empty folders, and a few large files hanging out loose in the current directory `.`.
Maybe I need a better file organization scheme!

### Interlude

Read the man pages for `top` and `du`. RTFM!


## <a name="awk"></a> Replacing Excel with `awk`

Now that we know how to do better than Word, let's do better than Excel too.
Let's calculate the center of mass of this protein, right on the command line!

What do we need to be able to do this?

First, we need to know the coordinates of each atom.
The x, y, and z coordinates are located in the 7th, 8th, and 9th columns of our `1RWT_atoms.txt` file, respectively.

Next, we need to know a formula for the center of mass.
If we assume that all the atoms are the same weight
(not a terrible approximation for nitrogen, carbon, and oxygen),
then the center of mass is just the vector average of all of the coordinates.

So if we can find the average of a column in a file, we can find the center of mass of the protein.

The tool to do this is `awk`.
It's one of my favorite things in the shell, and I bet it will be one of your favorites too.
`awk` (which is [named after its authors](http://en.wikipedia.org/wiki/AWK)) is actually a full programming language—my boyfriend has even written physics simulations in pure `awk` (yeah we're those kinds of nerds :) ).
Like `grep`, the full power of `awk` is far beyond what we'll get to today,
but it's easy to get started.
You can check out some more advanced examples [here](http://www.catonmat.net/blog/awk-one-liners-explained-part-one/).

The anatomy of an `awk` command is `awk '{stuff}' input_file`.
`awk` loops over every line in `input_file`,
splits it into columns (default column separator is whitespace),
and applies the `stuff` part to the columns.
Each column is referenced by a dollar sign followed by the column number: for instance, the first column is `$1`.
(`$0` gets you the whole line.)
So to print the 7th, 8th, and 9th columns of the first few lines of `1RWT_atoms.txt`, we can run

	head 1RWT_atoms.txt | awk '{print $7, $8, $9}' 

or equivalently

	awk '{print $7, $8, $9}' 1RWT_atoms.txt | head

Compare to the output of plain old `head 1RWT_atoms.txt`: looks good to me!

Now let's break down how to calculate the average.
An average is a sum over the number of elements in the sum;
let's start with the sum.

The syntax for summing up a column in `awk` is a bit complicated,
but it's easy enough to copy, paste, and tweak to suit your needs.
To calculate the sum of the first column in a file,
the command is `awk '{sum += $1}END{print sum}' input_file`.
`sum` is a variable that starts out at zero and stores a running sum of the values in the column (you can name it whatever you like).
Let's calculate the sum of the x coordinates:

	anna$ awk '{sumx+=$7}END{print sumx}' 1RWT_atoms.txt
	305108

`awk` has a built-in way to get the number of lines that have been processed so far:
it's `NR` (number of records).
After `END`, we've processed all the rows, so `NR` should be the same as the number of lines in the file.
Let's check that:

	anna$ awk '{sumx+=$7}END{print NR}' 1RWT_atoms.txt
	16619

You can check that against what we expect from `wc`; looks good to me.

Now let's put the sum and the count together to get the average of the x coordinates:

	anna$ awk '{sumx+=$7}END{print sumx/NR}' 1RWT_atoms.txt
	18.359

To get all three coordinates of the center of mass at once, separate the sums by semicolons and the print statements by commas:

	anna$ awk '{sumx+=$7; sumy+=$8; sumz+=$9}END{print sumx/NR, sumy/NR, sumz/NR}' 1RWT_atoms.txt
	18.359 68.5232 56.0891

Et voila.

### Interlude

You can even count the number of atoms in each kind of amino acid in `1RWT_atoms.txt` using just one `awk` command! Check out [this link](http://kuscsik.blogspot.com/2008/02/how-to-create-histogram-using-awk.html) to see how to create a histogram using `awk`. (I can never remember the syntax, but I can always remember how to find this link: just google for "awk histogram"!) Copy and paste the sample command into the terminal, replace `$0` with `$4` (the amino acid name is in the 4th column), and replace `FILE.DAT` with `1RWT_atoms.txt`. Press return. Magic!

## Great job!

You are now a shell master!
Use your skills wisely :)

## <a name="cheat"></a> Cheat sheet

| Command | What it's short for | What it does | Lesson |
|:------- |:------------- |:------------ |:------ |
| `awk`   | the authors Aho, Weinberger, and Kernighan | analyze columnar data | [Awk](#awk) |
| `bash`   | bash    | run a bash script | [Scripts](#scripts) |
| `cat`   | concatenate     | print one or more whole files | [Tools](#tools) |
| `cd`   | change directory  | go somewhere | [File system](#files) |
| `cp`   | copy        | copy something | [File system](#files) |
| `curl`   | like URL     | download something | [Tools](#tools) |
| `du`   | disk usage  | how much stuff is stored where | [Systems](#systems) |
| `echo`   | holla back    | print to the screen | [Scripts](#scripts) |
| `grep`   | like "regular expressions"     | search in a file | [Tools](#tools) |
| `gunzip`   | unzip for *gz files*  | unzip something | [Tools](#tools) |
| `head`   | top of a file     | print the first lines | [Tools](#tools) |
| `history`   | history    | see previously-executed commands | [Scripts](#scripts) |
| `less`   | "less is more"    | scroll through more of a file | [Tools](#tools) |
| `ls`   | list        | what's there? | [File system](#files) |
| `man`   | manual     | opens documentation | [RTFM](#rtfm) |
| `mkdir`   | make directory  | make a folder | [File system](#files) |
| `mv`   | move      | move or rename something | [File system](#files) |
| `pwd`   | present working directory | where am I? | [Prompt](#prompt) |
| `rm`   | remove        | delete something | [File system](#files) |
| `tail`   | bottom of a file  | print the last lines | [Tools](#tools) |
| `top`   | top view of your computer  | what's running right now? | [Systems](#systems) |
| `touch`   | touch     | make a blank file | [File system](#files) |
| `wc`   | word count | how many lines, words, and characters? | [Tools](#tools) |
| vertical slash  | pipe     | chain commands together | [Tools](#tools) |
| `>`   | redirect     | put something into a file | [Tools](#tools) |
| `>>`   | redirect too    | append something to a file | [Tools](#tools) |
| `#`   | comment    | don't execute the rest of the line | [Scripts](#scripts) |
