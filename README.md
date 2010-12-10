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

This is a terribly hacky solution - no, seriously, this is terrible. Don't use
it if you're not aware of the Bad Things that can happen and are willing to
accept those risks.

If you really, really want to try this, take a look at the instructions in
`waypoint.sh`.

# pushd and popd

Shortly after starting this, [raylu] brought [pushd and popd] to my attention.
They're pretty cool, I must say, but [popd] doesn't seem to have the kind of
name-specified path-popping that I want. That said, if you just want to build a
stack of paths and rewind back down, go use those instead of waypoint.


[0]: http://stackoverflow.com/questions/2375003/how-do-i-set-the-working-directory-of-the-parent-process/2375174#2375174
[voodoo magic]: http://ajdiaz.wordpress.com/2008/02/09/bash-ini-parser/
[raylu]: https://github.com/raylu
[pushd and popd]: http://en.wikipedia.org/wiki/Pushd_and_popd
[popd]: http://ss64.com/bash/popd.html
