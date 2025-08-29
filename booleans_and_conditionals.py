# Define a function called 'sign'
def sign(num):
    if num == 0:
        return 0
    elif num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        print("no value")


def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")
    return total_candies % 3

to_smash(91)
to_smash(1)

def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    return have_umbrella or rain_level < 5 and have_hood or ((not rain_level > 0) and is_workday)

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = True
rain_level = 1
have_hood = True
is_workday = True

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)

def is_negative(number):
    if number < 0:
        return True
    else:
        return False
# writing the same function by just one line of code below:(which was fun to discover)
def concise_is_negative(number):
    return number < 0

def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    return not onion

def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup and mustard and onion

def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not (ketchup or mustard or onion)

def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return (ketchup and not mustard) or (mustard and not ketchup)

def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    return (int(ketchup) + int(mustard) + int(onion)) == 1
# or without the need to make them integer: (ketchup + mustard + onion) == 1

""" Question 7: Return True if the player should hit (request another card) given the current game state, or False if the player should stay. When calculating
a hand's total value, we count aces as "high" (with value 11) if doing so doesn't bring the total above 21, otherwise we count them as low (with value 1). 
For example, if the player's hand is {A, A, A, 7}, we will count it as 11 + 1 + 1 + 7, and therefore set player_total=20, player_low_aces=2, player_high_aces=1.
The player is dealt two face-up cards. The dealer is dealt one face-up card. The player may ask to be dealt another card ('hit') as many times as they wish. 
If the sum of their cards exceeds 21, they lose the round immediately. The dealer then deals additional cards to himself until either:
the sum of the dealer's cards exceeds 21, in which case the player wins the round the sum of the dealer's cards is greater than or equal to 17.
If the player's total is greater than the dealer's, the player wins. Otherwise, the dealer wins (even in case of a tie).
When calculating the sum of cards, Jack, Queen, and King count for 10. Aces can count as 1 or 11 (when referring to a player's "total" above,
we mean the largest total that can be made without exceeding 21. So e.g. A+8 = 19, A+8+8 = 17).
"""

def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    # If player's total is 11 or less, always hit (you can't bust)
    if player_total <= 11:
        return True
    
    # If player's total is between 12 and 16, hit only if dealer shows 7 or more
    elif 12 <= player_total <= 16:
        return dealer_total >= 7

    # If player's total is 17 or more, don't hit
    else:
        return False

#below is a test case we passed:
should_hit(10, 14, 0, 0) # → True (dealer has strong card, hit)

def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    """Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay.
    When calculating a hand's total value, we count aces as "high" (with value 11) if doing so
    doesn't bring the total above 21, otherwise we count them as low (with value 1). 
    For example, if the player's hand is {A, A, A, 7}, we will count it as 11 + 1 + 1 + 7,
    and therefore set player_total=20, player_low_aces=2, player_high_aces=1.
    """
    # Soft hand logic
    if player_high_aces >= 1:
        return player_total <= 17
    
    # Hard hand logic
    if player_total >= 17:
        return False
    elif 12 <= player_total <= 16:
        return dealer_total >= 7
    else:
        return True