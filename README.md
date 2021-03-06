# Advent of Code

My attempts at the 2020 Advent of Code. Try it. It's great!

[https://adventofcode.com/2020](https://adventofcode.com/2020)

## Approach

In 2019 I started using python unit tests after a while. This year I'm doing this from the start. I like to try and hit the right answer first time, so this helps give a bit of confidence and it also allows for easy fettling of the solution once it's done: I like to try and refactor to get "better" solutions once I've completed the task.

## Day 1

**Easy**

I was slow off the mark, having forgotten about AoC! Easy solution though, iterating over lists and checking addition.

## Day 2

**Easy**

I used a regular expression matcher to split the spec, then a simple check on the validity conditions. 

## Day 3

**Straightforward**

Nice problem this one. Some basic modular arithmetic to deal with the "wrap around". I made my first blunder on this problem, forgetting to `strip()` the lines after reading them, which meant the map had newlines in it and my first submission was wrong.

## Day 4

**Straightforward**

Part one was straightforward, but I ended up faffing around a lot with regular expressions to get part two right.

I've been trying to second-guess the problems now as well, thinking about how a solution might be easily extended to part two. 

## Day 5

**Straightforward**

It's just converting the seat codes to binary, using `F = 0, B = 1` and `L = 0, R = 1`. I wasn't as clever as I thought though, as I didn't do it all in one, but converted row, then seat then did the calculation, rather than noticing that the `row*8` meant that the whole thing just converted to binary in one. Doh!

Part two just involved ordering then finding the gap. I did cut a corner here and eyeballed the results just to make sure. I should trust my code!

## Day 6

**Easy**

Relatively easy this one. I used a python `set` to record the questions answered by each group. The parsing and conversion to sets was a little clunky though. With part two, it was basically a case of adjusting to use `intersection` rather than `union`. Some refactoring and use of `reduce` simplified things a lot, meaning the only difference between the parts was the operator that was being passed in to `reduce`.

If I'd *really* thought ahead, I would have used the reduce solution from the start, resulting in a one-line change for part two. 

Today I also started using `logging` rather than my own hand rolled debugging code. 

## Day 7

**Straightforward**

Still fairly straightforward. Hardest bit here was the parsing. I considered trying to do the whole thing with a regex, but in the end I chopped it up using `split` and then dealt with pieces explicitly.

My data structure choice was right though as Part 2 only required minimal coding. I was guessing it would involve some kind of recursive trawl though the bags.

Unit tests helped here in picking up a potential off by one error in part two.

## Day 8

Looks like we're on our way with a multi-part machine build!

With that in mind, I've tried to build something that's extensible and provides a basic machine for execution of instructions. Solution is a bit clunky. Part one keeps a trace of instructions and then checks through. Part two does the "termination" check outside of the machine. This probably needs refactoring if we're going to see more machine based problems. 

Also added a slightly better specification of test data using split.

## Day 9

**Easy**

Sliding window across a list of numbers with some calculations. Initial solution is pretty clunky -- could certainly do better with some python list wrangling.
