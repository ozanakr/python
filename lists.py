primes = [2, 3, 5, 7]
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]
hands_alt = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]

def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L) < 2:
        return None
    return L[1]

def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """

    pass
# example data to test the function
# i could do dictionary in order to write this in one go i think
team_a = ["a", "b", "c", "d"]
team_b = ["e", "f", "g", "h"]
team_c = ["j", "k", "l", "m"]

teams = [team_a, team_b, team_c]

print(teams[-1][1])

def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    # my solution was:
    # racers[0], racers[-1] = racers[-1], racers[0]

    # One slick way to do the swap is x[0], x[-1] = x[-1], x[0].
    temp = racers[0]
    racers[0] = racers[-1]
    racers[-1] = temp

a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

# Put your predictions in the list below. Lengths should contain 4 numbers, the
# first being the length of a, the second being the length of b and so on.
lengths = [3, 2, 0, 2]
#a: There are three items in this list. Nothing tricky yet.
#b: The list [2, 3] counts as a single item. It has one item before it. So we have 2 items in the list
#c: The empty list has 0 items
#d: The expression is the same as the list [2, 3], which has length 2.

def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1