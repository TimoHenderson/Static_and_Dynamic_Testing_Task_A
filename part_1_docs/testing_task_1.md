### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    # card.value is being assigned the value of 1 (=)
    # instead of being checked for equality with 1 (==)
    if card.value = 1:
      return True
    #  : missed after else
    else
      return False
   
  # typo in method declaration - dif should be def
  # comma missed between card1 and card 2 in parameters
  dif highest_card(self, card1 card2):
  # code block not indented
  if card1.value > card2.value:
    # card not initialised - should be card1
    return card
  else:
    return card2
  

# indentation is wrong -method is outside the class
def cards_total(self, cards):
  # total is not assigned a value - should be total = 0
  total
  for card in cards:
    total += card.value
# can't concatenate a string and an int. Use str(total)
# return is inside for loop
    return "You have a total of" + total
  
```
