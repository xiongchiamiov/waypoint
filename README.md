Sometimes I'd like to mark a directory in the shell, and skip back to it quickly
later, like using marks in vim.  Waypoint is designed to do just that.

In an Unix environment, there's no real way to change a parent process's working
directory, aside from [some really terrible thing][0] I spotted on
StackOverflow.  I could think of 3 options:

1. Spawn new shells, and try and keep the number of them under control.  
2. Write a terrible shell script that uses some [voodoo magic] to parse ini
files and `cd` to the appropriate directory, and then `source` that file.
3. Write a less-terrible Python script that writes a file that is then
`source`d.

I chose option 3.

This is a terribly hacky solution - no, seriously, this is terrible. I wouldn't
really recommend you use it, even after it's finished, and right now it's a
hacky spattering of ideas onto my screen. Don't use it if you're not aware of
the Bad Things that can happen and are willing to accept those risks.

If you really, really want to try this, you'll need to change the hard-coded
paths to match your system, source the waypoint.sh in your .zshrc or .bashrc,
and create the .config/waypoint directory. IIRC, you'll have to touch the
scratch.sh file as well.


[0]: http://stackoverflow.com/questions/2375003/how-do-i-set-the-working-directory-of-the-parent-process/2375174#2375174
[voodoo magic]: http://ajdiaz.wordpress.com/2008/02/09/bash-ini-parser/
