from random import choice
from art import logo, vs
from game_data import data  # game data
from replit import clear  # only in replit


def increase_score(score_user):
  """Returns increased current score by one"""
  return score_user + 1


def compare_followers(num_followers_a, num_followers_b):
  """Returns the correct answer acording of comparison"""
  if num_followers_a > num_followers_b:
    return 'A'
  elif num_followers_a < num_followers_b:
    return 'B'
  else:
    return 'AB'  # if equals, the answer is correct for both


def format_data(comparation):
  """Returns the printable format of data"""
  comparation_name = comparation['name']
  comparation_desc = comparation['description']
  comparation_country = comparation['country']

  return f"{comparation_name}, a {comparation_desc}, from {comparation_country}."


def play_higher_lower():
  print(logo)
  score = 0
  comparation_a = {}
  comparation_b = {}
  user_is_right = True
  while user_is_right:
    if score == 0:
      comparation_a = choice(data)
    else:
      comparation_a = comparation_b

    comparation_b = choice(data)
    # while the comparations are equals, get another choice for data
    # to have different comparations
    while comparation_a == comparation_b:
      comparation_b = choice(data)

    print(f"Compare A: {format_data(comparation_a)}")
    print(vs)
    print(f"Against B: {format_data(comparation_b)}")

    answer_user = input("Who has more followers? Type 'A' or 'B': ").upper()
    while answer_user not in ['A', 'B']:
      answer_user = input(
        "Invalid input. Who has more followers? Type 'A' or 'B': ")

    winner_answer = compare_followers(comparation_a['follower_count'],
                                      comparation_b['follower_count'])
    # Clear the screen between rounds
    clear()
    print(logo)

    # We use "contains" method in case winner_answer is 'AB'
    if answer_user in winner_answer:
      score = increase_score(score)
      print(f"You're right! Current score: {score}.")
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      user_is_right = False


play_higher_lower()
while input(
    "\nDo you want to play another game? Type 'y' for yes or any other key for no: "
).lower() == 'y':
  clear()
  play_higher_lower()
