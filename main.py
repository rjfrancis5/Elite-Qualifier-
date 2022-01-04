import random
print ("Anytime you'd like to stop, press q!")
def generate_response(user_input):
  responses = [
    "That's what's up!",
    "For sure",
    "Definetley!",
    "You dont say!"
  ]
  return random.choice(responses)

def init_chat():
  quit_character = 'q'

  user_input = input("Hello, how are you?\n")

  while user_input != quit_character:
    #Ask the user for more input, then use that in your response
    user_input = input(generate_response(user_input) + "\n")

if __name__ == "__main__":
  init_chat()