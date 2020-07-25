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