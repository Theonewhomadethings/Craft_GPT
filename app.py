import os
import discord
import tensorflow as tf
import time


def main():

    with open('vocab.txt') as f:
        vocab = f.read().splitlines()
    vocab = set(vocab)

    ids_from_strings = tf.keras.layers.StringLookup(
        vocabulary=list(vocab), mask_token=None)

    strings_from_ids = tf.keras.layers.StringLookup(
    vocabulary=ids_from_strings.get_vocabulary(), invert=True, mask_token=None)


    intents = discord.Intents.all()
    client = discord.Client(command_prefix='!', intents=intents)

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))
        channel = client.get_channel(***CHANNEL_NUMBER_HERE***)

        await channel.send('''```
          ___   .--.
    .--.-"   "-' .- |
   / .-,`          .'
   \   `           \\               WELCOME TO 
    '.            ! \\              CRAFT-GPT
      |     !  .--.  |
      \        '--'  /.____
     /`-.     \__,'.'      `\\
  __/   \`-.____.-' `\      /
  | `---`'-'._/-`     \----'    _ 
  |,-'`  /             |    _.-' `\\
 .'     /              |--'`     / |
/      /\              `         | |
|   .\/  \      .--. __          \ |
 '-'      '._       /  `\         /
             `\    '     |------'`
               \  |      |
                \        /
                 '._  _.'
                    `` ```''')

        await channel.send('To use the crafting bot and recieve a new crochet recipe, type /pattern followed by your keyword! For example, /pattern doll\n\nType /help for help')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('hi'):
            await message.channel.send('Hello!')

        if message.content.startswith('/pattern '):
            prompt = message.content[9:]
            print(prompt)

            if prompt in vocab:
                one_step_model_reloaded = tf.saved_model.load('final_model/content/one_step_8')

                states = None
                next_string=[prompt]

                for n in range(1000):
                    next_string, states = one_step_model_reloaded.generate_one_step(next_string, states=states, training=False)
                    result.append(next_string)

                result = tf.strings.join(result, separator=" ")
                end = time.time()
                await message.channel.send((result[0].numpy().decode('utf-8'), '\n\n' + '_'*80))
            else:
                await message.channel.sent('Unfortunately Craft-GPT does\'nt know that word perhaps try from one of these? "Ant", "Ball", "Bear", "Batman", "Bunny", "Cactus", "Christmas", "Dachshund", "Dog", "Elephant" etc')

        if message.content.startswith('/about'):
            await message.channel.sent('This is CRAFT-GPT, a Generative RNN trained on a corpus of crochet instructions in the Hope that they could suggest new and exciting ideas to crochet. Created by Holly Everest, Abdullah Saleem and Joel Dolman')
            
        
        if message.content.startswith('/help'):
            await message.channel.sent('Craft-GPT: Use /pattern "pattern" to generate part of a crochet instruction, Whilst Craft-GPT is almost as intelligent as Chat-GPT it does not know all words, so if the pattern fails, please try another one, the full list is found in /fullprompts')
            await message.channel.sent('Whilst every effort has been made to create a competent generative AI, it is sometimes prudent to retry the model multiple times before settling on your instructions, some interpretation will be required whilst we iron out the kinks in the algorithm')
            


    client.run('***CLIENT SECRET KEY HERE***')


if __name__ == "__main__":
    main()


