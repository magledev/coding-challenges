# Build Your Own wc Tool

This challenge involves creating your own version of the Unix command wc.

From the Linux man pages for [wc](https://www.gnu.org/software/coreutils/wc):


```
NAME
       wc - print newline, word, and byte counts for each file

SYNOPSIS
       wc [OPTION]... [FILE]...
       wc [OPTION]... --files0-from=F

DESCRIPTION
       Print  newline,  word,  and byte counts for each FILE, and a total line if more than one FILE is specified.  A word is a nonempty sequence of non white
       space delimited by white space characters or by start or end of input.

       With no FILE, or when FILE is -, read standard input.

       The options below may be used to select which counts are printed, always in the following order: newline, word, character, byte, maximum line length.

       -c, --bytes
              print the byte counts

       -m, --chars
              print the character counts

       -l, --lines
              print the newline counts

       --files0-from=F
              read input from the files specified by NUL-terminated names in file F; If F is - then read names from standard input

       -L, --max-line-length
              print the maximum display width

       -w, --words
              print the word counts

       --total=WHEN
              when to print a line with total counts; WHEN can be: auto, always, only, never

       --help display this help and exit

       --version
              output version information and exit
```

## Steps:

### Step One:
- [x] In this step your goal is to write a simple version of wc, let’s call it ccwc (cc for Coding Challenges) that takes the command line option -c and outputs the number of bytes in a file.

### Step Two:
- [ ] In this step your goal is to support the command line option -l that outputs the number of lines in a file.

### Step Three:
- [ ] In this step your goal is to support the command line option -w that outputs the number of words in a file.

### Step Four:
- [ ] In this step your goal is to support the command line option -m that outputs the number of characters in a file. If the current locale does not support multibyte characters this will match the -c option.

### Step Five:
- [ ] In this step your goal is to support the default option - i.e. no options are provided, which is the equivalent to the -c, -l and -w options.

### Step Six:
- [ ] In this step your goal is to support being able to read from standard input if no filename is specified.
