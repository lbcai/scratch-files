# hanoi towers is a useful problem to understand recursion. move a stack of discs from one stick to another
# each disc is 1 smaller than the one on top of it. n = 3 discs, stack starting from bottom: 3 2 1
# you can only move one disc at a time and cannot place the disc on any disc smaller than it.

n = 2
# range(5) = 0 1 2 3 4
# reversed(range(1, 5)) = 4 3 2 1
list_1 = list(reversed((range(1, n + 1))))
list_2 = []
list_3 = []
print(list_1, list_2, list_3)
counter = 0

# rotate through "positions" because when the problem is solved, each piece gets placed
# on an intermediate stick before going to the third "end" position. basically, the game is
# pattern recognition when coding this problem

# use global counter to stop annoying counter resetting

def towers(n, start, helper, end):
    global counter
    if n == 1:
        end.append(start[-1])
        start.pop()
        print(list_1, list_2, list_3)
        counter += 1
        print(counter)

    else:
        towers(n - 1, start, end, helper)
        end.append(start[-1])
        start.pop()
        print(list_1, list_2, list_3)
        counter += 1
        print(counter)

        towers(n - 1, helper, start, end)


towers(n, list_1, list_2, list_3)

# the number of moves is known to be 2^n - 1 (minimum) for each n of the hanoi towers puzzle.
# input generated looks like [2, 1] [] []
# gives output [] [] [2, 1] and all the steps in between. also counts each step. printed to console for
# easy error checking.
