# Thoughts

Can I make a bot class that has the db, etc etc plus all the
methods. Can I extend the base class with a class of each
of the separate files? Then I can just simplify calls potentially,
instead of having a ton of function calls that pass in the DB cursor
I could just call the method on the bot and the self.DB would be
already there I wouldnt need to pass it in. Need to figure out how to
merge all the individual functions into once class. Will most
liekly need to make each command branch into its own class that extends
the main bot class.

I can convert everything to OOP eventually, I need to get the functional
version live and working first.
