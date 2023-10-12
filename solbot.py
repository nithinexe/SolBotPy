import discord
from discord.ext import commands
import os

# Creating a bot instance with prefix
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')

# Event: when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Custom command !ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Command to create a new Solana wallet
@bot.command()
async def createwallet(ctx):
    # Implement logic to create a new Solana wallet
    # Generate a new wallet address and private key
    # Provide the wallet address to the user
    await ctx.send('Your new Solana wallet has been created!')

# Command to display the wallet address for depositing Solana
@bot.command()
async def deposit(ctx):
    # Retrieve the user's wallet address and display it
    await ctx.send('Your Solana wallet address for deposits: YOUR_WALLET_ADDRESS')

# Command to send Solana to another wallet
@bot.command()
async def send(ctx, recipient_wallet, amount):
    # Implement logic to send Solana to the specified recipient
    # Ensure proper validation and error handling
    await ctx.send(f'Sending {amount} SOL to {recipient_wallet}.')

# Command to check the Solana balance of the user's wallet
@bot.command()
async def balance(ctx):
    # Implement logic to check the Solana balance of the user's wallet
    # Retrieve and display the balance
    await ctx.send('Your Solana wallet balance is: X SOL')

# Command to view recent transactions for the user's wallet
@bot.command()
async def transactions(ctx):
    # Implement logic to retrieve and display recent transactions for the user's wallet
    await ctx.send('Here are your recent Solana transactions:')

# Command to check the estimated transaction fee for a specific amount
@bot.command()
async def fee(ctx, amount):
    # Implement logic to calculate and display the estimated transaction fee
    await ctx.send(f'The estimated transaction fee for {amount} SOL is: X SOL')

# Command to cancel a pending transaction (if supported)
@bot.command()
async def cancel(ctx, transaction_id):
    # Implement logic to cancel a pending Solana transaction
    # Provide feedback to the user
    await ctx.send(f'Cancelling transaction {transaction_id}.')


#run bot with your token 

bot.run('MTE1ODc3NzIyNjE5MjQ4NjUwMA.G-8g-p.931D8ew9APKhbky1G-xEN_nhnH__Wl6992ynh4')

