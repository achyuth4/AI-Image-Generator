import os # We import the OS library, to be able to use console commands
import random # We import the random library, to be able to generate a random file name
import string # We import the string library, to be able to assign some parameters to the variable of the file name
import openai # We imported the open ai library, which allows us to use the open ai api
import requests # We import the requests library, to be able to download the generated image
from colorama import Fore # Clean the Y finally import Fore from the Colorama library, to give a little color to the console
os.system("cls") # We clean the console

# And here we define the variables of the colors to have them more orderly
w = Fore.LIGHTWHITE_EX
r = Fore.LIGHTRED_EX
g = Fore.LIGHTGREEN_EX
b = Fore.LIGHTBLUE_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
black = Fore.LIGHTBLACK_EX



openai.organization = "Enter Your Org ID" # Here you must put the ID of your organization that you can find in -> https://beta.openai.com/account/org-settings
openai.api_key = "Enter Your API Key" # Here you must put your API KEY that you can find in -> https://beta.openai.com/account/api-keys
openai.Model.list()

os.system("title achyuth4 - Image Generator - OPEN AI") # Here we give a title to the console

print(f"{m}[{w}1{m}] {black}Image Generator")


def image_gen(): # Here we define the function of image generation
    image=input(f"{m}[{w}>>>{m}] {black}Leave your arguments here?:{w} ") # Here we ask for the arguments for the image
    print(f"{m}[{w}>{m}] {black}Generating image{m}...")
    r = openai.Image.create(prompt=image, n=2, size="1024x1024") # Here we tell the api to generate the image with the arguments we gave
    image_url = r["data"][0]["url"] # Here we tell you to save the url of the generated image
    os.system("cls")
    print(f"{m}[{w}!{m}] {black}Generated image: {y}{image_url}")
    print(f"{image_url}")
    save=input(f"{m}[{w}>>>{m}] {black}Do You want to save the image? [y/n]:{w} ") # Here we ask you if you want to save the image
    if save == "y": # If the answer is "and" then...
        path="./img/" # Here we tell you to save the image in the "img" folder
        nombre_random= "".join(random.choice(string.ascii_letters + string.digits)  for i in range(10)) # Here we tell you to generate a random name for the image
        nombre_archivo = f"{path}{nombre_random}.png" # Here we tell you to save the image with the random name and extension.png
        imagen_save= requests.get(image_url).content # Here we tell you to download the image"
        with open(nombre_archivo, 'wb') as i:
            i.write(imagen_save)
            print(f"{m}[{w}!{m}] {black}Image saved in folder: {y}{nombre_archivo}")
    openask=input("¿Do You want to open the image? [y/n]: ") # Here we ask if you want to open the image in the browser
    if openask == "y": # If the answer is "and" then...
        os.system(f"""explorer {image_url}""") # Here we tell you to open the image in the browser
    else: # And if the answer is any other, then we simply tell you to exit the program by pressing any key.
        print("OK")
        print("Press any key to exit")
        os.system("pause >nul")
        os.system("exit")

image_gen()

# https://github.com/achyuth4
