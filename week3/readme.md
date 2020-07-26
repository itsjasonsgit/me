TODO: Reflect on what you learned this week and what is still unclear.

Most of my "notes" are written in comments in the code. But in terms of what I've learned:

.format(value1, value2)
An alternative way of formatting to concatenation:
val1 = great
print("something {value1} you know?".format(val1))
Data within the {} is placeholder data for readability

try/except/else/etc.
Used to test if code is working or if it ain't. There's a lot here, for example
except can test for certain exceptions.

I'm not sure my formatting of this, or my understanding of what it does in
every circumstance is clear.

Most importantly, I learned this week that it's not "concantonate" it's "concatenate".
Yikes.

Exercise 2 "diagram":
> User sets upper bounds
> Program sets an actual number, at random, between the range set by the user
> Create a loop
    > While the loop thinks the guess is wrong (False) keep running
    > Ask the user to guess
    > If the user is right, set the guess to True
    > Else if the number is too small, say it's too small
    > Else the number must be too big - say it's too big


Binary search
Is the most effective way of guessing a number in a range
IF you're getting a "it's higher/lower" result.
STATISTICALLY - that is, it'll work the best, on average, when used
over many times. Like, a random guess may be quicker SOME times, but
on average, will take the length of the range to guess.
A linear search will also take, on average, 50% of the total
number of the values. (is that right?)
Anyway, searching binary makes a lot of sense. Split the values.
Now you've got 50% less numbers to work with. Repeat until you've
found the value. Pretty obvious, I guess. Now to implement...

So I went with my stupid method to find the midpoint of a range, which is:
high - ((high - low) / 2)

But it woulda been easier just to do:
high + low // 2
// is a floor division
But ima leave it. Whatever. It works.


A code reading experience! Thoughts:
I didn't struggle with this question. But I didn't feel like
it was an optimal solution, either.

Rizo's solution is more elegant than mine, since it doesn't require
adding spaces before AND after. It just figures out
if there needs to be a space or a star.

What is "abs"? Penny used it too.
Ah, it returns an absolute number.

Did... penny copy Rizo? Or visa versa?

Either way, I'd need to go through this step by step to figure
out what the hell is going on. It's not.. readable.
Why aren't these students commenting?

FlimEden had a super strange solution.
Again, I hate that they didn't comment.

Lorniashi had a really simple solution.
Using the {} for formatting is interesting. I'm not sure
I understand her equation at first glance, but that's pretty sweet.
Again. COMMENT!!!!

DanielHeh looks like he did the same sort of thing as me.
That's cool I guess. I think it's pretty readable. But..
Obviously not the cleanest solution.

These guys seem to be more experienced than 3rd week
programmers.

Looking at these solutions now, reconsidering the problem,
I can already think of new ways to solve it. Cleaner ways.
That's fine. I imagine much of programming, early on, is just
writing stuff and then re-writing it as you "get it" and
think about it more with your new, better understanding.