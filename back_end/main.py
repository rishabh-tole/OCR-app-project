
from summary import Summary
import sys
from Naked.toolshed.shell import muterun_js
import website_summarizer as ws

def image_to_text():
  response = muterun_js('image_to_text.js')

def summarize_doc(bullets):
  print("sum")
  summ = Summary()
  return summ.summarize(bullets)


def audio_to_text():
  #NOT IMPLEMENTED
  # TO DO
  pass

def print_doc():
  #NOT IMPLEMENTED
  #TO DO
  pass

def website(url):
  ws.summarize_website(url)

audio_vs_image = input("do you want to convert audio, image or website?(a/i/w)")

print(audio_vs_image)
if audio_vs_image == "a":
  sum_or_not = input("Do you want a summary? (y/n)")

  if sum_or_not == 'y':
    bull = input("how many points")
    audio_to_text()
    summarize_doc(int(bull))

  else:
    audio_to_text()
    print_doc()

elif audio_vs_image == "i":
  sum_or_not = input("Do you want a summary? (y/n)")

  if sum_or_not == "y":
    bull = input("how many points")
    image_to_text()
    summarize_doc(int(bull))

  else:
    image_to_text()
    print_doc()
    
elif audio_vs_image == "w":
  url = input("Paste url:")
  website(url)

