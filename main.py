import os
import nextcord
from nextcord.ext import commands
import asyncio
import datetime
import requests
import urllib
import json
import random
import os
import akinator
from nextcord import ButtonStyle, Interaction
from nextcord.ui import button, View, Button
from nextcord.abc import GuildChannel
from PIL import Image,ImageDraw,ImageFont,ImageChops
import io
import time
from io import BytesIO
import craiyon
from craiyon import Craiyon
import base64
import motor.motor_asyncio
import psutil
from nextcord.ext.commands import BucketType, cooldown
import nest_asyncio


global startTime
startTime = time.time()

cluster = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGO"])
well = cluster["main"]
welcome = well["welcome"]
leave = well["leave"]
cd = well["saved"]
print("Database Initalized")

client = commands.Bot(command_prefix=['#','<@970577992877223946> '], intents = nextcord.Intents.all())
@client.event
async def on_ready():
  
    channel = client.get_channel(999541224975376486)
    print(f'{client.user} is ONLINE!')
    await channel.send('online')
    await client.change_presence(status=nextcord.Status.dnd,activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f"#help"))
    
    





  


client.remove_command("help")

  
if __name__ == "__main__":
        for name in os.listdir("./cogs"):
            if name.endswith(".py"):
                try:
                    client.load_extension("cogs.{}".format(name[:-3]))
                    print('Loaded: cogs.{}'.format(name[:-3]))
                except Exception as error:
                    print(f'cogs.{name[:-                3]} cannot be loaded. [{error}]')


  
@client.slash_command(description="Replies with pong!")
async def ping(interaction: nextcord.Interaction):
    await interaction.send("Pong!", ephemeral=True)





@client.event
async def on_message(message):
    if message.content.startswith(f'<@970577992877223946>'):
      
      embed = nextcord.Embed(title = "Hey wassup?", description="my prefix is `#`")
    
      embed.set_thumbnail(url=client.user.display_avatar)
      
      await message.channel.send(embed=embed)
    await client.process_commands(message)


      







  


























  


@client.command()
async def hi(ctx):
  
  await ctx.send("testing nextcord buttons")






@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, limit: int):
    await ctx.message.delete()
    await asyncio.sleep(1)
    await ctx.channel.purge(limit=limit)
    purge_embed = nextcord.Embed(title='Purge [!purge]', description=f'Successfully purged {limit} messages. \n Command executed by {ctx.author}.', color=nextcord.Colour.random())
    purge_embed.set_footer(text=str(datetime.datetime.now()))
    await ctx.channel.send(embed=purge_embed, delete_after=True)
@purge.error
async def purge_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send('You do not have permission to use this command!')
















@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: nextcord.Member = None, *, reason=None):
    if user == None:
        await ctx.send("Please enter a user!")
        return

    await user.kick(reason=reason)
    await ctx.send(f'Kicked {user.name} for reason {reason}')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send('You do not have permission to use this command!')


@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
@unban.error
async def unban_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send('You do not have permission to use this command!')


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: nextcord.Member = None, *, reason=None):
    if user == None:
        await ctx.send("Please enter a user!")
        return

    await user.ban(reason=reason)
    await ctx.send(f'Banned {user.name} for reason {reason}')
@ban.error
async def ban_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send('You do not have permission to use this command!')






@client.command()
async def hack(ctx, *, member: nextcord.Member = None):
  password = [

        ':nxjdididkxkkxk)',
        '13384859(&8_8_(&(',
        'ndidicjckoxixk',
        'discordpaddfjfjj',
        'Definitely',
        'ye',
        'Maybe so.',
        'No i doi dont thinkdont think so'
        'ofcdjjdjxkxk'

      ]
  message = await ctx.send(f"HACKING {member.name} now...")
  await asyncio.sleep(1)
  message.edit(content=f"installing virus in all connected divices")
  await asyncio.sleep(1)
  await message.edit(content=f"installing virus")
  await asyncio.sleep(4)
  message.edit(content=f"installed virus")
  await asyncio.sleep(1)
  message.edit(content=f"Finding discord login info....")
  await asyncio.sleep(1)
  await message.edit(content=f"""FOUND  Email: `{member.name}@gmail.com`              Password:`{random.choice(password)}`""")
  await asyncio.sleep(1)
  await  message.edit(content=f"deleting all data")
  await  message.edit(content=f"SUCCESS FULLY HACKED {member.name}")


@client.command()
async def say(ctx,*,message=None):
  if message is None:
    await ctx.send(f'{ctx.author.mention} mention some message to say')
    return
  else:
      	await ctx.send(message)

@client.command(aliases=['cf']) 
async def coinflip(ctx):

  message = await ctx.send(f"<a:coinflip1:1003650084312981615>|coin fliping...")
  cf = [



    "Tails", 
    "Heads"


  ]
  await asyncio.sleep(1)
  await message.edit(f"{random.choice(cf)}")



@client.command() 
async def dice(ctx):

  message = await ctx.send(f"<a:dice:1003653068325396500>Rolling dice")
  dice = [



    "1", 
    "2", 
    "3", 
    "5", 
    "6",
    "4"


  ]
  await asyncio.sleep(1)
  await message.edit(f"<a:dice:1003653068325396500>|{random.choice(dice)}")

@client.command()
async def rate(ctx,*,message=None):
  if message is None:
    await ctx.send(f'{ctx.author.mention} mention any word to rate')
    return
  else:
    b = [
    "1", 
    "6", 
    "9", 
    "15", 
    "12", 
    "20", 
    "28", 
    "35", 
    " 65", 
    "33", 
    "38", 
    "45", 
    "50", 
    "58", 
    "68", 
    "65", 
    " 74", 
    "79", 
    "80", 
    "91", 
    "100", 
    " 98", 
    
  ]
  await ctx.send(f"I rate {message} {random.choice(b)}%")
@rate.error
async def rate_error(ctx):
  await ctx.send(f"{ctx.author.name} give me a word to rate")




@client.command()
async def fliptext(ctx, *, arg="A normal sentence"): 
    await ctx.send(arg[::-1])



@client.command()
async def lovecalc(ctx, *, member: nextcord.Member = None):
  l = [
    "1", 
    "6", 
    "9", 
    "15", 
    "12", 
    "20", 
    "28", 
    "35", 
    "65", 
    "33", 
    "38", 
    "45", 
    "50", 
    "58", 
    "68", 
    "65", 
    " 74", 
    "79", 
    "80", 
    "91", 
    "100", 
    " 98", 
    
  ]
  hug = [
    'https://c.tenor.com/8Jk1ueYnyYUAAAAC/hug.gif',
    'https://i.pinimg.com/originals/31/d2/3c/31d23cb7e7f199a0524eb2a95eeb6397.gif',
    'https://c.tenor.com/2VVGNLi-EV4AAAAM/anime-cute.gif'
    'https://c.tenor.com/5fiWSpLaEe0AAAAC/anime-hug.gif',
    'https://c.tenor.com/AO-1yttBeH8AAAAC/anime-hug.gif',
    'https://c.tenor.com/2lr9uM5JmPQAAAAC/hug-anime-hug.gif',
  'https://c.tenor.com/cFhjNVecNGcAAAAC/anime-hug.gif',
    'https://c.tenor.com/SIw6C9wrgPUAAAAC/anime-hug.gif',
    'https://c.tenor.com/1GDpumaCq_4AAAAC/anime-hug.gif'
  ]
  embed = nextcord.Embed(title="love calc", description=f"{ctx.author.name} loves {member.name}  {random.choice(l)}%")
  embed.set_image(url = f"{random.choice(hug)}")
  await ctx.send(embed=embed)







class hi(nextcord.ui.View):
  def __init__(self):
    super().__init__()
    self.value = None 
    
@nextcord.ui.button(label = 'subscribe', style=nextcord.ButtonStyle.green)
async def subcribe(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
  self.value = True
  self.stop()




@client.command()
async def t(ctx):
  view = hi()
  await ctx.send("hi", view=view)
  await view.wait()
  


























@client.command()
async def invites(ctx):
    totalInvites = 0
    for i in await ctx.guild.invites():
        if i.inviter == ctx.author:
            totalInvites += i.uses
    await ctx.send(f"You've invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server!")

@client.command(aliases=["mc"])

async def members(ctx):

    a=ctx.guild.member_count
    b=nextcord.Embed(title=f"members in {ctx.guild.name}",description=a,color=nextcord.Color((0xffff00)))
    await ctx.send(embed=b)



class ButtonName(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
        self.value = None


      
    @nextcord.ui.button(label="🗿ROCK", style=nextcord.ButtonStyle.grey)
    async def rock(self, button: nextcord.ui.Button ,interaction: Interaction):
        rps = [
          "Rock",
          "Paper",
          "scissors"



        ]
        test = nextcord.Embed(title="<a:rps:1004022823842480168>Rock paper scissors",description=f'You choosed rock and i chossed {random.choice(rps)}')
        await interaction.response.send_message(embed=test)
        self.value=True
        self.stop()
    @nextcord.ui.button(label="📄Paper", style=nextcord.ButtonStyle.grey)
    async def paper(self, button: nextcord.ui.Button ,interaction: Interaction):
        rps = [
          "Rock",
          "Paper",
          "scissors"



        ]
        test1 = nextcord.Embed(title="<a:rps:1004022823842480168>Rock paper scissors",description=f'You choosed paper and i chossed {random.choice(rps)}')      
        await interaction.response.send_message(embed=test1)
        self.value=True
        self.stop()      
    @nextcord.ui.button(label="✂Scissors", style=nextcord.ButtonStyle.grey)
    async def scissors(self, button: nextcord.ui.Button ,interaction: Interaction):
        rps = [
          "Rock",
          "Paper",
          "scissors"



        ]
        test2 = nextcord.Embed(title="<a:rps:1004022823842480168>Rock paper scissors",description=f'You choosed scissors and i chossed {random.choice(rps)}')      
        await interaction.response.send_message(embed=test2)
        self.value=True
        self.stop()     

        
@client.command()
async def rps(ctx):
    embed = nextcord.Embed(title="<a:rps:1004022823842480168>Rps",description='click on button to play')
    view = ButtonName()
    await ctx.send(embed=embed, view=view)

@client.command()
async def serverinfo(ctx):
    embed = nextcord.Embed(title = f"{ctx.guild.name} Info", description = "Information of this Server", color = nextcord.Colour.blue())
    embed.add_field(name = 'Server ID', value = f"{ctx.guild.id}", inline = True)
    embed.add_field(name = 'Created On', value = ctx.guild.created_at.strftime("%b %d %Y"), inline = True)
    embed.add_field(name = 'Owner', value = f"{ctx.guild.owner}", inline = True)
    embed.add_field(name = 'Members', value = f'{ctx.guild.member_count} Members', inline = True)
    
    embed.add_field(name = 'Region', value = f'{ctx.guild.region}', inline = True)
        
    
    await ctx.send(embed=embed)




@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : nextcord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('Channel locked.')

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : nextcord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('Channel unlocked.')



















  
@client.command()
async def help(ctx):

    class Select(nextcord.ui.Select):
        def __init__(self):
            options=[
                nextcord.SelectOption(label="INFO",emoji="<a:info:993763572888899584>",value="in",),
                nextcord.SelectOption(label="Modration",emoji='<:moderation:990580070466846720>', value="mod"),
                nextcord.SelectOption(label="Fun",emoji = '<a:fun:1025273034543730768>',value="fun"),


                nextcord.SelectOption(label="Games",emoji = '<a:games:1025277092461559849>',value="game"),                
              
                nextcord.SelectOption(label="Actions",emoji='<:actionshin:1025273873450676294>',value="action"),
              nextcord.SelectOption(label="Welcome",emoji='<a:animeWelcome:1034761336334331946>',value="welcw"),
nextcord.SelectOption(label="support",emoji='<a:supporter:1034813070708580352>',value="supp"),              
                nextcord.SelectOption(label="Utility",emoji='<:Utility:990582796198244382>',value="util"),

                ]
            super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)
        async def callback(self, interaction: nextcord.Interaction):

            if self.values[0] == "in":
               
                await interaction.response.send_message(embed = nextcord.Embed(title="<a:info:993763572888899584>|Info",description="```USERINFO,SERVERINFO,INVITE,SUPPORT,UPTIME,VOTE,PING```"))
                                                        
                                                          
            elif self.values[0] == "mod":
                await interaction.response.send_message(embed = nextcord.Embed(title='<:moderation:990580070466846720>Modration',description = '```kick,Ban,lock,unlock,purge,mute,unmute```'))
            elif self.values[0] == "fun":
                await interaction.response.send_message(embed = nextcord.Embed(title='<a:fun:1025273034543730768>Fun',description='```hack,meme,lovecalc,lie,8ball,coinflip,dice, fliptext,virus,wanted,secret,genimage,chat```'))                


            elif self.values[0] == "action":
                await interaction.response.send_message(embed = nextcord.Embed(title="<:actionshin:1025273873450676294>Action",description='```slap,hug,pat``'))                



            elif self.values[0] == "util":
                await interaction.response.send_message(embed = nextcord.Embed(title='<:Utility:990582796198244382>Utility',description='```dm,invites,members,rate,say,slowmode,avatar,8ball,save,find```'))                
            elif self.values[0] == "game":
                await interaction.response.send_message(embed = nextcord.Embed(title='<a:games:1025277092461559849>Games',description='```rps```'))
              
            elif self.values[0] == "welcw":
                await interaction.response.send_message(embed = nextcord.Embed(title='<a:animeWelcome:1034761336334331946>|Games',description='```setchannel,rwchannel,leavechannel,rlchannel```'))
            elif self.values[0] == "supp":
                await interaction.response.send_message(embed = nextcord.Embed(title='<a:supporter:1034813070708580352>|Support',description='```suggest report```'))              
    class SelectView(nextcord.ui.View):
        def __init__(self, *, timeout = 180):
            super().__init__(timeout=timeout)
            self.add_item(Select())
    embed = nextcord.Embed(title='hey wassup?',description='Use select menu to get cmds')
    
    embed.set_thumbnail(url=ctx.author.display_avatar)
    embed.set_image(url="https://media.discordapp.net/attachments/999541224975376486/1038829585254592592/standard_1.gif")

    
    await ctx.send(embed=embed,view=SelectView())                            

















  
@client.command()
@commands.has_permissions(administrator=True)
async def slowmode(ctx, seconds: int):
    if commands.has_permissions(administrator=True):
        if not seconds:
            await ctx.channel.edit(slowmode_delay=0)
            
            embed = nextcord.Embed(description=f'slow mode set to 0sec', color=0x60C546)
            await ctx.send(embed=embed)
        elif seconds > 21600:
          
          embed = nextcord.Embed(description=f'breh 🥴', color=0x60C546)
          await ctx.send(embed=embed)
        else:
            await ctx.channel.edit(slowmode_delay=seconds)
            
            embed = nextcord.Embed(description=f' Slowmode set to {seconds} seconds', color=0x60C546)
            await ctx.send(embed=embed)
@slowmode.error
async def slowmode_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send('You do not have permission to use this command!```emaple:#slowmode <time>```')            



  























@client.command(aliases=['av'])
async def avatar(ctx, *, user: nextcord.Member=None):
  user = user or ctx.author
  embed = nextcord.Embed(title="AVATAR", description=f"showing {user} avatar")
  embed.set_image(url=user.display_avatar)
  embed.set_footer(text="av")
  await ctx.send(embed=embed)

























@client.command()
async def lie(ctx, *, user: nextcord.Member=None):
  lie = [
    "lier",
    "Not a lier"
  ]
  user = user or ctx.author
  embed = nextcord.Embed(title="lier Or not a lier",description=f'{user} is {random.choice(lie)}')
  
  embed.set_image(url="https://media.discordapp.net/attachments/999541224975376486/1025383418269290586/images_31.jpg")
  embed.set_thumbnail(url=user.display_avatar)
  await ctx.send(embed=embed)
  



@client.command()
async def hug(ctx, *, member: nextcord.Member = None):
  hug = [
    'https://c.tenor.com/8Jk1ueYnyYUAAAAC/hug.gif',
    'https://i.pinimg.com/originals/31/d2/3c/31d23cb7e7f199a0524eb2a95eeb6397.gif',
    'https://c.tenor.com/2VVGNLi-EV4AAAAM/anime-cute.gif'
    'https://c.tenor.com/5fiWSpLaEe0AAAAC/anime-hug.gif',
    'https://c.tenor.com/AO-1yttBeH8AAAAC/anime-hug.gif',
    'https://c.tenor.com/2lr9uM5JmPQAAAAC/hug-anime-hug.gif',
  'https://c.tenor.com/cFhjNVecNGcAAAAC/anime-hug.gif',
    'https://c.tenor.com/SIw6C9wrgPUAAAAC/anime-hug.gif',
    'https://c.tenor.com/1GDpumaCq_4AAAAC/anime-hug.gif'
]


  embed = nextcord.Embed(title = f"{member.name} got a hug by {ctx.author.name}")
  embed.set_image(url = f"{random.choice(hug)}")
  await ctx.send(embed=embed)


@client.command()
async def pat(ctx, *, member: nextcord.Member = None):
  pat = [
    'https://c.tenor.com/E6fMkQRZBdIAAAAM/kanna-kamui-pat.gif',
    'https://c.tenor.com/dmYhPDHbbI4AAAAM/misha-misha-necron-anos-voldigoad-the-misfit-of-demon-king-academy-headpat-pat.gif',
    'https://i.pinimg.com/originals/70/96/0e/70960e87fb9454df6a1d15c96c9ad955.gif',
    'https://c.tenor.com/lVsnDFq21W8AAAAC/pat-head-anime.gif',
    'https://c.tenor.com/-hkJYNs7tUkAAAAC/anime-pat.gif',
    'https://64.media.tumblr.com/tumblr_lps86chQSj1qbvovho1_500.gifv',
    'https://c.tenor.com/Av63tpT8Y14AAAAC/pat-head.gif'
    'https://64.media.tumblr.com/80f4e1aeee44dee530b1e6b416a8459d/83ad7e3b43d48041-53/s500x750/ddbb45d884338428dd0f1e042099b353fd3f49b3.gifv'


    
  ]
  embed = nextcord.Embed(title = f"{member.name} got patted by {ctx.author.name}")
  embed.set_image(url = f"{random.choice(pat)}")
  await ctx.send(embed=embed)




@client.command()
async def slap(ctx, *, member: nextcord.Member = None):
  slap = [
    'https://c.tenor.com/CvBTA0GyrogAAAAC/anime-slap.gif',
    'https://c.tenor.com/Ws6Dm1ZW_vMAAAAC/girl-slap.gif',
    'https://i.pinimg.com/originals/1c/8f/0f/1c8f0f43c75c11bf504b25340ddd912d.gif',
    'https://c.tenor.com/fKzRzEiQlPQAAAAC/anime-slap.gif',
    'https://c.tenor.com/iDdGxlZZfGoAAAAC/powerful-head-slap.gif',
    'https://i.gifer.com/7zBH.gif',
    'https://64.media.tumblr.com/743b1aa4147c380f7aee3594b146c8fc/tumblr_mtu1yqvCd51s4bvyoo1_400.gif',
    'https://c.tenor.com/FJsjk_9b_XgAAAAM/anime-hit.gif',
    'https://c.tenor.com/Pae1Oya15vYAAAAM/anime-hit.gif'
  ]
  embed = nextcord.Embed(title = f"{member.name} got slapped by {ctx.author.name}")
  embed.set_image(url = f"{random.choice(slap)}")
  await ctx.send(embed=embed)


@client.command(name='8ball',
            description="Answers a yes/no question.",
            brief="Answers from the beyond.",
            aliases=['eight_ball', 'eightball', '8-ball'],
            pass_context=True)

async def eight_ball(context):
    possible_responses = [

        ':)',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
        'ye',
        'Maybe so.',
        'No i doi dont thinkdont think so'
        'ofc'

    ]
    await context.channel.send(random.choice(possible_responses) + ", " + context.message.author.mention)



class tb(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        

    @nextcord.ui.button(label="84", style=nextcord.ButtonStyle.primary)
    async def green_button(self,button:nextcord.ui.Button,interaction:nextcord.Interaction):
          ahh = await interaction.response.send_message("correct")
          await asyncio.sleep(2)
          await ahh.edit("injected virus successfully..  btw u r dumb")


@client.command()
async def virus(ctx, *, member: nextcord.Member = None):
  class TestButtons(nextcord.ui.View):
        def __init__(self, *, timeout=None):
            super().__init__(timeout=timeout)
          
          
        @nextcord.ui.button(label="connect",style=nextcord.ButtonStyle.green) 
        async def green_button(self,button:nextcord.ui.Button,interaction:nextcord.Interaction):
          hi = await interaction.response.send_message("connecting")
          await asyncio.sleep(2)
          await hi.edit("connected successfully")
          await asyncio.sleep(1)
          await hi.edit("working..")
          await asyncio.sleep(2)
          await hi.edit("hacking.......")
          await asyncio.sleep(2)
          await hi.edit("we got an issue...solve this problem... 🥴to continue..```7+77```",view = tb())
          
         
  user = ctx.author or member
  msg = await ctx.send(f"injecting 1000000 virus on {user}")
  await asyncio.sleep(2)
  await msg.edit("LOST INTERNET...")
  await asyncio.sleep(1)
  await msg.edit("trying to connect again......")
  await asyncio.sleep(2)
  await msg.edit("click on buttons to continue",view = TestButtons())

  


















						










class ta(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        

    @nextcord.ui.button(label="Next meme", style=nextcord.ButtonStyle.primary,emoji="<:Meme:1026044286346735657>")
    async def green_button(self,button:nextcord.ui.Button,interaction:nextcord.Interaction):
      memeApi = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme')
      memeData = json.load(memeApi)
      memeUrl = memeData['url']
      memeName = memeData['title']
      embed = nextcord.Embed(title=f"{memeName}", description="")
      embed.set_image(url=f'{memeUrl}')
      b = await interaction.response.send_message(embed=embed,view=ta())



@client.command()
async def meme(ctx):
  
  memeApi = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme')
  memeData = json.load(memeApi)
  memeUrl = memeData['url']
  memeName = memeData['title']
  
  embed = nextcord.Embed(title=f"{memeName}", description="")
  embed.set_image(url=f'{memeUrl}')
  view = ta()
  await ctx.send(embed=embed,view=view) 







class link(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(nextcord.ui.Button(style = nextcord.ButtonStyle.link, url = "https://discord.com/api/oauth2/authorize?client_id=970577992877223946&permissions=157035186230&scope=bot%20applications.commands", label = "INVITE ME", emoji = "<:invite:997076508050997278>"))
@client.command() 
async def invite(ctx):
      await ctx.send("INVITE ME☠️☠️☠️",view=link())

class SUPPORT(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(nextcord.ui.Button(style = nextcord.ButtonStyle.link, url = "https://discord.gg/8grPm9uSaQ", label = "SUPPORT", emoji = "<a:uptimer:997801903733882880>"))
@client.command()
async def support(ctx):
      await ctx.send("SUPPORT☠️☠️☠️",view=SUPPORT())






class rick(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(nextcord.ui.Button(style = nextcord.ButtonStyle.link, url = "https://youtu.be/dQw4w9WgXcQ", label = "Click me", emoji = "☠️"))
@client.command()
async def secret(ctx):
  await ctx.send("click on below link to reveal secret||Listen we r not hackers u can trust us||",view=rick())
  



@client.command()
async def uptime(ctx):
  uptimes = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
  await ctx.send(f" {uptimes}")


  
class damn(nextcord.ui.View):
    def __init__(self):
      super().__init__()
      self.add_item(nextcord.ui.Button(style = nextcord.ButtonStyle.link, url = "https://discordbotlist.com/bots/fleko", label = "DBL", emoji = "<:topgg:1026364285653360751>"))








      
class topn(nextcord.ui.View):
    def __init__(self):
      super().__init__()
      self.add_item(nextcord.ui.Button(style = nextcord.ButtonStyle.link, url = "https://top.gg/bot/970577992877223946", label = "TOP.GG", emoji = "<:topgg:1026364024469856317>"))
      self.add_item(nextcord.ui.Button(style = nextcord.ButtonStyle.link, url = "https://discordbotlist.com/bots/fleko", label = "DBL", emoji = "<:topgg:1026364285653360751>"))


 
@client.command()
async def vote(ctx):
  
  view = topn()
  
  await ctx.send("VOTE ME",view=view) 


        






@client.command()
async def users(ctx):
  user = client.users
  users = len(user)
  await ctx.send(f"{users}")

@client.command()
async def servers(ctx):
  s = client.guilds
  si = len(s)
  await ctx.send(f"{si}")




mod = nextcord.Embed(title="🔨 | Moderation",description=" `kick`, `ban`, `unban`, `mute`, `unmute`, `purge`")
mod.add_field(name="kick",value='usage:```^kick <@user>```')
mod.add_field(name="Ban",value="usage:```^kick <@user>```")
mod.add_field(name="unban",value="usage:```^unban <member id>```")
mod.add_field(name="mute",value="usage:```^mute <@user> <time>```")
mod.add_field(name="unmute",value = "usage:```^unmute <@user>```")
mod.add_field(name=" Purge",value="usage:```^purge <amount>```")
mod.set_image(url="https://media.tenor.com/oS0d558B98MAAAAC/discord-robot.gif")
mod.set_thumbnail(url="https://media.discordapp.net/attachments/999541224975376486/1026809767387217940/965e748eecc4cd9a2c1a8d019fe34a2b.png")
fun = nextcord.Embed(title='<:fun:1026834098704089129>',description="`ping`, `calc`, `dog`, `cat`, `virus`, `time`, `thank`, `hack`, `profile`, `meme`") 
fun.add_field(name="ping",value="usage:```^ping```")
fun.add_field(name="calc",value="usage:```^calc```")
fun.add_field(name="cat",value="usage:```^cat```")
fun.add_field(name="virus",value="usage:```^virus <@user>```")
fun.add_field(name="time",value="usage:```time```")
fun.set_image(url="https://media.discordapp.net/attachments/999541224975376486/1027160360169513000/giphy.gif")
fun.set_thumbnail(url=f"https://media.discordapp.net/attachments/999541224975376486/1026809767387217940/965e748eecc4cd9a2c1a8d019fe34a2b.png")

class funn(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        

    @nextcord.ui.button(label=None, style=nextcord.ButtonStyle.primary,emoji="<:arrow_side:1027163556048801842> ")
    async def green_button(self,button:nextcord.ui.Button,interaction:nextcord.Interaction):
      await interaction.response.send_message(embed=embed,view=funn())      
@client.command()
async def oru(ctx):

    class orus(nextcord.ui.Select):
        def __init__(self):
            options=[
                nextcord.SelectOption(label="MODRATION", description="Shows MODRATION commands", emoji="<a:modration:1026833720751173682>",value="modration",),
                nextcord.SelectOption(label="FUN", description="Shows Fun commands",emoji='<:fun:1026834098704089129>', value="fun"),
                nextcord.SelectOption(label="Utility", description="Shows Utility commands", emoji = '<:Icons_utility:1026834454016176138>',value="utility"),


                nextcord.SelectOption(label="Games", description="Shows Game commands", emoji = '<:dice:1026834890165063700>',value="game"),                
              
                nextcord.SelectOption(label="Actions", description="Shows action commands", emoji='<:huggingface:1026835320324489296>',value="action"),              
                nextcord.SelectOption(label="Search", description="Shows Search commands", emoji='<a:search:1026835496770474104>',value="util"),
                nextcord.SelectOption(label="Giveaway", description="Shows Giveaway commands", emoji='<:giveaways:1026835691440717915>',value="Giveaway"),
                nextcord.SelectOption(label="Economy", description="Shows Economy commands", emoji='<a:economy:1026835809749438554>',value="Economy"),      


                nextcord.SelectOption(label="Other", description="Shows other commands", emoji='<:others:1026835973406986241>',value="Other"),     

              
                ]
            super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)
        async def callback(self, interaction: nextcord.Interaction):

            if self.values[0] == "modration":
                
              await interaction.response.send_message(embed = mod)
                                                        
                                                     
            elif self.values[0] == "fun":
                await interaction.response.send_message(embed = fun)
            elif self.values[0] == "fuhjn":
                await interaction.response.send_message(embed = nextcord.Embed(title='<a:fun:1025273034543730768>Fun',description='```hack,meme,lovecalc,lie,8ball,coinflip,dice, fliptext,virus,wanted,secret,genimage,chat```'))                


            elif self.values[0] == "action":
                await interaction.response.send_message(embed = nextcord.Embed(title="<:actionshin:1025273873450676294>Action",description='```slap,hug,pat``'))                



            elif self.values[0] == "util":
                await interaction.response.send_message(embed = nextcord.Embed(title='<:Utility:990582796198244382>Utility',description='```dm,invites,members,rate,say,slowmode,avatar,8ball```'))                
            elif self.values[0] == "game":
                await interaction.response.send_message(embed = nextcord.Embed(title='<a:games:1025277092461559849>Games',description='```rps```'))

              
    class oru(nextcord.ui.View):
        def __init__(self, *, timeout = 180):
            super().__init__(timeout=timeout)
            self.add_item(orus())
    embed = nextcord.Embed(title='Hey Im orus',description='Thanks for using <:textard:1026757582611828786>**Orus**! use select menu to get command list')
    embed.add_field(name="TYPES",value="Tyep of commands")
    embed.add_field(name="🔨 | Moderation",value=f"Modration commands")
    embed.add_field(name='🥳 | Fun',value="Fun commands")
    embed.add_field(name='🛠️ | Utility',value="Utility commands")
    embed.add_field(name="🎲 | Games",value="Game commands")
    embed.add_field(name="🤗 | Actions",value=" Action commands")
    embed.add_field(name="🔎 | Search",value="search command")
    embed.add_field(name="🎉 | Giveaway",value="Giveaway commands")
    embed.add_field(name="👹 | Anime",value="Anime commands")
    embed.add_field(name="💰 | Economy",value="Economy commands")
    embed.add_field(name="❓ | Other",value="Other commands")


  
    embed.set_thumbnail(url=client.user.display_avatar)
    
    await ctx.send(embed=embed,view=oru())




@client.command()
async def genimage(ctx: commands.Context, *, prompt: str):
    ETA = int(time.time() + 60)
    msg = await ctx.send(f"Just a moment... ETA : <t:{ETA}:R>")
    generator = Craiyon()
    result = generator.generate(prompt)
    images = result.images
    
    for i in images:
        image = BytesIO(base64.decodebytes(i.encode("utf-8")))
        return await msg.edit(content = "Content generated by **craiyon.com**", file = nextcord.File(image, "craiyon.png"))






def circle(pfp,size = (220,220)):
  pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
  bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
  mask = Image.new('L', bigsize, 0)
  draw = ImageDraw.Draw(mask)
  draw.ellipse((0, 0) + bigsize, fill=255)
  mask = mask.resize(pfp.size, Image.ANTIALIAS)
  mask = ImageChops.darker(mask,pfp.split()[-1])
  pfp.putalpha(mask)
  return pfp

@client.command()
@commands.has_permissions(manage_channels=True)
async def setchannel(ctx, *, channel: nextcord.TextChannel):
  data = await welcome.find_one({"guild_id":ctx.guild.id})
  if data==None:
    cid = {"guild_id":ctx.guild.id,"welcome_id":channel.id}
    await welcome.insert_one(cid)
    message = await ctx.send(embed = nextcord.Embed(title=" welcome has successful fully set",description=f"<#{channel.id}>"))
  else:
    await welcome.update_one({"guild_id": ctx.guild.id}, {"$inc": {"welcome_id":channel.id}})
    await ctx.send("updated welcome channel")
    




      
      
      
class welccf(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        

    @nextcord.ui.button(label="welcome", style=nextcord.ButtonStyle.primary,emoji="<a:animeWelcome:1034761336334331946>")
    async def green_button(self,button:nextcord.ui.Button,interaction:nextcord.Interaction):
          ahh = await interaction.response.send_message(embed = nextcord.Embed(title="welcome",description = f"hey ***{interaction.user.name}*** welcome :D we are glad and happy! thanks for joining")) 
          self.stop()
@client.event
async def on_member_join(member:nextcord.Member):
  data = await welcome.find_one({"guild_id":member.guild.id})
  welcc = data["welcome_id"]
  damnit = client.get_channel(welcc)
  welcce = Image.open('welcome.png')
  asset = member.display_avatar.with_size(256)
  data = BytesIO(await asset.read())
  pfp = Image.open(data)
  pic = pfp.resize((500, 500)) 
  draw = ImageDraw.Draw(welcce)
  membername = member.name
  myFont = ImageFont.truetype('./DrumNBass-ywGy2.ttf', 100)
  draw.text((850,670),membername,font = myFont,fill = (255,255,255))
  welcce.paste(pic, (850,850))
  welcce.save('welccm.png')
  embed = nextcord.Embed(title = "<a:welcome:1034105622586732564>|Welcome",description = f"**Hey!** {member.name} **welcome to this server!**",color=nextcord.Colour.random())
  embed.add_field(name="<a:arrow:1034105896722239578>|start chatting and make new friends",value =":D")
  embed.set_image(url="attachment://welccm.png")
  embed.set_thumbnail(url=member.display_avatar)
  embed.timestamp = datetime.datetime.utcnow()
  embed.set_footer(text='\u200b',icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSx6XVeEpbBs5gPMRwvoCeucv1GbDlxMcAUhQDouhPBb-2pghE&s")
  view = welccf()
  await damnit.send(content = member.mention,embed = embed,file=nextcord.File("welccm.png"),view = view) 

@client.event
async def on_member_remove(member: nextcord.Member):
  data = await leave.find_one({"guild_id":member.guild.id})
  b = data["leave_id"]
  smh = client.get_channel(b)
  leavee = Image.open('leave.png')
  asset = member.display_avatar.with_size(256)
  data = BytesIO(await asset.read())
  pfp = Image.open(data)
  pic = pfp.resize((200, 200))
  pfp = circle(pic,(360,360))
  draw = ImageDraw.Draw(leavee)
  membername = member.name
  myFont = ImageFont.truetype('./DrumNBass-ywGy2.ttf', 80)
  draw.text((200,126),membername,font = myFont,fill = (255,255,255))
  leavee.paste(pfp, (850,50))
  leavee.save('levm.png')
  embed = nextcord.Embed(title="left",description=f"{member.name}just left the server :(")
  embed.set_thumbnail(url=member.display_avatar)
  embed.timestamp = datetime.datetime.utcnow()
  embed.set_image(url="attachment://levm.png")
  await smh.send(embed = embed,file=nextcord.File("levm.png")) 













@client.command()
async def ping(ctx):
  embed = nextcord.Embed(title="Ping",description=f'latency = {round(client.latency * 1000)}ms')
  await ctx.send(embed = embed)


@client.command() 
async def suggest(ctx,*,message):
  channel = client.get_channel(972006872284536902)
  embed1 = nextcord.Embed(title = "suggestion appeared",description=f" from {ctx.author.name}```{message}```")

  await channel.send(embed = embed1)
  await ctx.send("sent your suggestion to developers")

@client.command()
async def report(ctx, *,msg):
  channel = client.get_channel(972006873341521960)
  embed = nextcord.Embed(title="Report",description=f"report from {ctx.author.name} report:- ```{msg}```")
  await channel.send(embed = embed)
  await ctx.send("report successfully sent")

@client.command()
@commands.has_permissions(manage_channels=True)
async def rwchannel(ctx, *,channel: nextcord.TextChannel):
  data = await welcome.find_one({"welcome_id": channel.id})
  
  welcc = data["welcome_id"]
  
  await welcome.update_one({"guild_id": ctx.guild.id}, {"$inc": {"welcome_id": "None"}})
  message = await ctx.send(embed = nextcord.Embed(title=" welcome has successful removed"))

@client.event
async def on_command_error(ctx, err):
  channel = client.get_channel(972006886784258068)
  await channel.send(f"{err}")









@client.command()
async def leavechannel(ctx, *, channel: nextcord.TextChannel):
  b = await leave.find_one({"guild_id":ctx.guild.id}) 
  if b==None:
    cid = {"guild_id":ctx.guild.id,"leave_id":channel.id}
    await leave.insert_one(cid)
    message = await ctx.send(embed = nextcord.Embed(title=" successfully set leave channel",description=f"<#{channel.id}>"))
  else:
    await leave.update_one({"guild_id": ctx.guild.id}, {"$inc": {"welcome_id": channel.id}})
    await ctx.send("successfullu updated leave channel")
    


 
@client.command()
@commands.has_permissions(manage_channels=True)
async def rlchannel(ctx, *,channel: nextcord.TextChannel):
  data = await leave.find_one({"welcome_id": channel.id})
  
  
  
  await leave.update_one({"guild_id": ctx.guild.id}, {"$inc": {"leave_id": "None"}})
  message = await ctx.send(embed = nextcord.Embed(title=" leave has successful removed"))



































@client.slash_command(description = "kicks member from server")
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: nextcord.Member = None, *, reason=None):
    if user == None:
        await ctx.send("Please enter a user!")
        return

    await user.kick(reason=reason)
    await ctx.send(f'Kicked {user.name} for reason {reason}')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send('You do not have permission to use this command!',delete_after = True)








@client.slash_command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, limit: int):
    await ctx.message.delete()
    await asyncio.sleep(1)
    await ctx.channel.purge(limit=limit)
    purge_embed = nextcord.Embed(title='Purge [!purge]', description=f'Successfully purged {limit} messages. \n Command executed by {ctx.author}.', color=nextcord.Colour.random())
    purge_embed.set_footer(text=str(datetime.datetime.now()))
    await ctx.channel.send(embed=purge_embed, delete_after=True)
@purge.error
async def purge_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send('You do not have permission to use this command!')

@client.slash_command(description = "unban's member from server")
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
@unban.error
async def unban_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send('You do not have permission to use this command!')


@client.slash_command(description = "ban's member from server")
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: nextcord.Member = None, *, reason=None):
    if user == None:
        await ctx.send("Please enter a user!")
        return

    await user.ban(reason=reason)
    await ctx.send(f'Banned {user.name} for reason {reason}')
@ban.error
async def ban_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send('You do not have permission to use this command!')










@client.slash_command(description = "just fun")
async def hack(ctx, *, member: nextcord.Member = None):
  password = [

        ':nxjdididkxkkxk)',
        '13384859(&8_8_(&(',
        'ndidicjckoxixk',
        'discordpaddfjfjj',
        'Definitely',
        'ye',
        'Maybe so.',
        'No i doi dont thinkdont think so'
        'ofcdjjdjxkxk'

      ]
  message = await ctx.send(f"HACKING {member.name} now...")
  await asyncio.sleep(1)
  message.edit(content=f"installing virus in all connected divices")
  await asyncio.sleep(1)
  await message.edit(content=f"installing virus")
  await asyncio.sleep(4)
  message.edit(content=f"installed virus")
  await asyncio.sleep(1)
  message.edit(content=f"Finding discord login info....")
  await asyncio.sleep(1)
  await message.edit(content=f"""FOUND  Email: `{member.name}@gmail.com`              Password:`{random.choice(password)}`""")
  await asyncio.sleep(1)
  await  message.edit(content=f"deleting all data")
  await  message.edit(content=f"SUCCESS FULLY HACKED {member.name}")








@client.slash_command(description = "says the msg")
async def say(ctx,*,message=None):
  if message is None:
    await ctx.send(f'{ctx.author.mention} mention some message to say')
    return
  else:
      	await ctx.send(message)




@client.slash_command(description = " flip a coin") 
async def coinflip(ctx):

  message = await ctx.send(f"<a:coinflip1:1003650084312981615>| fliping a coin...")
  cf = [



    "Tails", 
    "Heads"


  ]
  await asyncio.sleep(1)
  await message.edit(f"{random.choice(cf)}")



@client.slash_command(description = "roll a dice") 
async def dice(ctx):

  message = await ctx.send(f"<a:dice:1003653068325396500>|Rolling dice")
  dice = [



    "1", 
    "2", 
    "3", 
    "5", 
    "6",
    "4"


  ]
  await asyncio.sleep(1)
  await message.edit(f"<a:dice:1003653068325396500>|{random.choice(dice)}")







@client.slash_command(description = "rate's a word")
async def rate(ctx,*,message=None):
  if message is None:
    await ctx.send(f'{ctx.author.mention} mention any word to rate')
    return
  else:
    b = [
    "1", 
    "6", 
    "9", 
    "15", 
    "12", 
    "20", 
    "28", 
    "35", 
    " 65", 
    "33", 
    "38", 
    "45", 
    "50", 
    "58", 
    "68", 
    "65", 
    " 74", 
    "79", 
    "80", 
    "91", 
    "100", 
    " 98", 
    
  ]
  await ctx.send(f"I rate {message} {random.choice(b)}%")
@rate.error
async def rate_error(ctx):
  await ctx.send(f"{ctx.author.name} give me a word to rate")

@client.slash_command(description = "flips the text")
async def fliptext(ctx, *, msg="A normal sentence"): 
    await ctx.send(arg[::-1])


@client.slash_command(description = " claclulates love between u and member")
async def lovecalc(ctx, *, member: nextcord.Member = None):
  l = [
    "1", 
    "6", 
    "9", 
    "15", 
    "12", 
    "20", 
    "28", 
    "35", 
    "65", 
    "33", 
    "38", 
    "45", 
    "50", 
    "58", 
    "68", 
    "65", 
    " 74", 
    "79", 
    "80", 
    "91", 
    "100", 
    " 98", 
    
  ]
  hug = [
    'https://c.tenor.com/8Jk1ueYnyYUAAAAC/hug.gif',
    'https://i.pinimg.com/originals/31/d2/3c/31d23cb7e7f199a0524eb2a95eeb6397.gif',
    'https://c.tenor.com/2VVGNLi-EV4AAAAM/anime-cute.gif'
    'https://c.tenor.com/5fiWSpLaEe0AAAAC/anime-hug.gif',
    'https://c.tenor.com/AO-1yttBeH8AAAAC/anime-hug.gif',
    'https://c.tenor.com/2lr9uM5JmPQAAAAC/hug-anime-hug.gif',
  'https://c.tenor.com/cFhjNVecNGcAAAAC/anime-hug.gif',
    'https://c.tenor.com/SIw6C9wrgPUAAAAC/anime-hug.gif',
    'https://c.tenor.com/1GDpumaCq_4AAAAC/anime-hug.gif'
  ]
  embed = nextcord.Embed(title="love calc", description=f"{ctx.author.name} loves {member.name}  {random.choice(l)}%")
  embed.set_image(url = f"{random.choice(hug)}")
  await ctx.send(embed=embed)




  
@client.slash_command(description = "shows ur invites")
async def invites(ctx):
    totalInvites = 0
    for i in await ctx.guild.invites():
        if i.inviter == ctx.author:
            totalInvites += i.uses
    await ctx.send(f"You've invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server!")


@client.slash_command(description = "shows members count in server")

async def members(ctx):

    a=ctx.guild.member_count
    b=nextcord.Embed(title=f"members in {ctx.guild.name}",description=a,color=nextcord.Color((0xffff00)))
    await ctx.send(embed=b)
@client.slash_command(description = " play rps with bot")
async def rps(ctx):
    embed = nextcord.Embed(title="<a:rps:1004022823842480168>Rps",description='click on button to play')
    view = ButtonName()
    await ctx.send(embed=embed, view=view)









@client.slash_command(description = "shows server info")
async def serverinfo(ctx):
    embed = nextcord.Embed(title = f"{ctx.guild.name} Info", description = "Information of this Server", color = nextcord.Colour.blue())
    embed.add_field(name = 'Server ID', value = f"{ctx.guild.id}", inline = True)
    embed.add_field(name = 'Created On', value = ctx.guild.created_at.strftime("%b %d %Y"), inline = True)
    embed.add_field(name = 'Owner', value = f"{ctx.guild.owner}", inline = True)
    embed.add_field(name = 'Members', value = f'{ctx.guild.member_count} Members', inline = True)
    
    embed.add_field(name = 'Region', value = f'{ctx.guild.region}', inline = True)
        
    
    await ctx.send(embed=embed)





@client.slash_command(description = "lock the channel")
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : nextcord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('Channel locked.')

@client.slash_command(description = "unlock the channel")
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : nextcord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('Channel unlocked.')







  








@client.slash_command(description = "shows help menu")
async def help(ctx):

    class Select(nextcord.ui.Select):
        def __init__(self):
            options=[
                nextcord.SelectOption(label="INFO",emoji="<a:info:993763572888899584>",value="in",),
                nextcord.SelectOption(label="Modration",emoji='<:moderation:990580070466846720>', value="mod"),
                nextcord.SelectOption(label="Fun",emoji = '<a:fun:1025273034543730768>',value="fun"),


                nextcord.SelectOption(label="Games",emoji = '<a:games:1025277092461559849>',value="game"),                
              
                nextcord.SelectOption(label="Actions",emoji='<:actionshin:1025273873450676294>',value="action"),
              nextcord.SelectOption(label="Welcome",emoji='<a:animeWelcome:1034761336334331946>',value="welcw"),
nextcord.SelectOption(label="support",emoji='<a:supporter:1034813070708580352>',value="supp"),              
                nextcord.SelectOption(label="Utility",emoji='<:Utility:990582796198244382>',value="util"),

                ]
            super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)
        async def callback(self, interaction: nextcord.Interaction):

            if self.values[0] == "in":
               
                await interaction.response.send_message(embed = nextcord.Embed(title="<a:info:993763572888899584>|Info",description="```USERINFO,SERVERINFO,INVITE,SUPPORT,UPTIME,VOTE,PING```"))
                                                        
                                                          
            elif self.values[0] == "mod":
                await interaction.response.send_message(embed = nextcord.Embed(title='<:moderation:990580070466846720>Modration',description = '```kick,Ban,lock,unlock,purge,mute,unmute```'))
            elif self.values[0] == "fun":
                await interaction.response.send_message(embed = nextcord.Embed(title='<a:fun:1025273034543730768>Fun',description='```hack,meme,lovecalc,lie,8ball,coinflip,dice, fliptext,virus,wanted,secret,genimage,chat```'))                


            elif self.values[0] == "action":
                await interaction.response.send_message(embed = nextcord.Embed(title="<:actionshin:1025273873450676294>Action",description='```slap,hug,pat``'))                



            elif self.values[0] == "util":
                await interaction.response.send_message(embed = nextcord.Embed(title='<:Utility:990582796198244382>Utility',description='```dm,invites,members,rate,say,slowmode,avatar,8ball,save,find```'))                
            elif self.values[0] == "game":
                await interaction.response.send_message(embed = nextcord.Embed(title='<a:games:1025277092461559849>Games',description='```rps```'))
              
            elif self.values[0] == "welcw":
                await interaction.response.send_message(embed = nextcord.Embed(title='<a:animeWelcome:1034761336334331946>|Games',description='```setchannel,rwchannel,leavechannel,rlchannel```'))
            elif self.values[0] == "supp":
                await interaction.response.send_message(embed = nextcord.Embed(title='<a:supporter:1034813070708580352>|Support',description='```suggest report```'))              
    class SelectView(nextcord.ui.View):
        def __init__(self, *, timeout = 180):
            super().__init__(timeout=timeout)
            self.add_item(Select())
    embed = nextcord.Embed(title='hey wassup?',description='Use select menu to get cmds')
    
    embed.set_thumbnail(url=client.user.display_avatar)
    embed.set_image(url="https://media.discordapp.net/attachments/999541224975376486/1038829585254592592/standard_1.gif")

    
    await ctx.send(embed=embed,view=SelectView())




@client.slash_command(description = "set slowmode in current channel")
@commands.has_permissions(administrator=True)
async def slowmode(ctx, seconds: int):
    if commands.has_permissions(administrator=True):
        if not seconds:
            await ctx.channel.edit(slowmode_delay=0)
            
            embed = nextcord.Embed(description=f'slow mode set to 0sec', color=0x60C546)
            await ctx.send(embed=embed)
        elif seconds > 21600:
          
          embed = nextcord.Embed(description=f'breh 🥴', color=0x60C546)
          await ctx.send(embed=embed)
        else:
            await ctx.channel.edit(slowmode_delay=seconds)
            
            embed = nextcord.Embed(description=f' Slowmode set to {seconds} seconds', color=0x60C546)
            await ctx.send(embed=embed)
@slowmode.error
async def slowmode_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send('You do not have permission to use this command!```emaple:#slowmode <time>```')            



  


@client.slash_command(description = "shows member avatar")
async def avatar(ctx, *, user: nextcord.Member=None):
  user = user or ctx.author
  embed = nextcord.Embed(title="AVATAR", description=f"showing {user} avatar")
  embed.set_image(url=user.display_avatar)
  embed.set_footer(text="av")
  await ctx.send(embed=embed)





@client.slash_command()
async def lie(ctx, *, user: nextcord.Member=None):
  lie = [
    "lier",
    "Not a lier"
  ]
  user = user or ctx.author
  embed = nextcord.Embed(title="lier Or not a lier",description=f'{user} is {random.choice(lie)}')
  
  embed.set_image(url="https://media.discordapp.net/attachments/999541224975376486/1025383418269290586/images_31.jpg")
  embed.set_thumbnail(url=user.display_avatar)
  await ctx.send(embed=embed)
















@client.slash_command()
async def hug(ctx, *, member: nextcord.Member = None):
  hug = [
    'https://c.tenor.com/8Jk1ueYnyYUAAAAC/hug.gif',
    'https://i.pinimg.com/originals/31/d2/3c/31d23cb7e7f199a0524eb2a95eeb6397.gif',
    'https://c.tenor.com/2VVGNLi-EV4AAAAM/anime-cute.gif'
    'https://c.tenor.com/5fiWSpLaEe0AAAAC/anime-hug.gif',
    'https://c.tenor.com/AO-1yttBeH8AAAAC/anime-hug.gif',
    'https://c.tenor.com/2lr9uM5JmPQAAAAC/hug-anime-hug.gif',
  'https://c.tenor.com/cFhjNVecNGcAAAAC/anime-hug.gif',
    'https://c.tenor.com/SIw6C9wrgPUAAAAC/anime-hug.gif',
    'https://c.tenor.com/1GDpumaCq_4AAAAC/anime-hug.gif'
]


  embed = nextcord.Embed(title = f"{member.name} got a hug by {ctx.author.name}")
  embed.set_image(url = f"{random.choice(hug)}")
  await ctx.send(embed=embed)


@client.slash_command()
async def pat(ctx, *, member: nextcord.Member = None):
  pat = [
    'https://c.tenor.com/E6fMkQRZBdIAAAAM/kanna-kamui-pat.gif',
    'https://c.tenor.com/dmYhPDHbbI4AAAAM/misha-misha-necron-anos-voldigoad-the-misfit-of-demon-king-academy-headpat-pat.gif',
    'https://i.pinimg.com/originals/70/96/0e/70960e87fb9454df6a1d15c96c9ad955.gif',
    'https://c.tenor.com/lVsnDFq21W8AAAAC/pat-head-anime.gif',
    'https://c.tenor.com/-hkJYNs7tUkAAAAC/anime-pat.gif',
    'https://64.media.tumblr.com/tumblr_lps86chQSj1qbvovho1_500.gifv',
    'https://c.tenor.com/Av63tpT8Y14AAAAC/pat-head.gif'
    'https://64.media.tumblr.com/80f4e1aeee44dee530b1e6b416a8459d/83ad7e3b43d48041-53/s500x750/ddbb45d884338428dd0f1e042099b353fd3f49b3.gifv'


    
  ]
  embed = nextcord.Embed(title = f"{member.name} got patted by {ctx.author.name}")
  embed.set_image(url = f"{random.choice(pat)}")
  await ctx.send(embed=embed)




@client.slash_command()
async def slap(ctx, *, member: nextcord.Member = None):
  slap = [
    'https://c.tenor.com/CvBTA0GyrogAAAAC/anime-slap.gif',
    'https://c.tenor.com/Ws6Dm1ZW_vMAAAAC/girl-slap.gif',
    'https://i.pinimg.com/originals/1c/8f/0f/1c8f0f43c75c11bf504b25340ddd912d.gif',
    'https://c.tenor.com/fKzRzEiQlPQAAAAC/anime-slap.gif',
    'https://c.tenor.com/iDdGxlZZfGoAAAAC/powerful-head-slap.gif',
    'https://i.gifer.com/7zBH.gif',
    'https://64.media.tumblr.com/743b1aa4147c380f7aee3594b146c8fc/tumblr_mtu1yqvCd51s4bvyoo1_400.gif',
    'https://c.tenor.com/FJsjk_9b_XgAAAAM/anime-hit.gif',
    'https://c.tenor.com/Pae1Oya15vYAAAAM/anime-hit.gif'
  ]
  embed = nextcord.Embed(title = f"{member.name} got slapped by {ctx.author.name}")
  embed.set_image(url = f"{random.choice(slap)}")
  await ctx.send(embed=embed)











@client.slash_command(name='8ball',
            description="Answers a yes/no question.")

async def eight_ball(context, *,msg):
    possible_responses = [

        ':)',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
        'ye',
        'Maybe so.',
        'No i doi dont thinkdont think so'
        'ofc'

    ]
    await context.channel.send(random.choice(possible_responses))


@client.slash_command()
async def virus(ctx, *, member: nextcord.Member = None):
  class TestButtons(nextcord.ui.View):
        def __init__(self, *, timeout=None):
            super().__init__(timeout=timeout)
          
          
        @nextcord.ui.button(label="connect",style=nextcord.ButtonStyle.green) 
        async def green_button(self,button:nextcord.ui.Button,interaction:nextcord.Interaction):
          hi = await interaction.response.send_message("connecting")
          await asyncio.sleep(2)
          await hi.edit("connected successfully")
          await asyncio.sleep(1)
          await hi.edit("working..")
          await asyncio.sleep(2)
          await hi.edit("hacking.......")
          await asyncio.sleep(2)
          await hi.edit("we got an issue...solve this problem... 🥴to continue..```7+77```",view = tb())
          
         
  user = ctx.author or member
  msg = await ctx.send(f"injecting 1000000 virus on {user}")
  await asyncio.sleep(2)
  await msg.edit("LOST INTERNET...")
  await asyncio.sleep(1)
  await msg.edit("trying to connect again......")
  await asyncio.sleep(2)
  await msg.edit("click on buttons to continue",view = TestButtons())








@client.slash_command(description = "sends memes")
async def meme(ctx):
  
  memeApi = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme')
  memeData = json.load(memeApi)
  memeUrl = memeData['url']
  memeName = memeData['title']
  
  embed = nextcord.Embed(title=f"{memeName}", description="")
  embed.set_image(url=f'{memeUrl}')
  view = ta()
  await ctx.send(embed=embed,view=view)



  







@client.slash_command(description = "invite bot") 
async def invite(ctx):
      await ctx.send("INVITE ME☠️☠️☠️",view=link())



@client.slash_command()
async def support(ctx):
      await ctx.send("SUPPORT☠️☠️☠️",view=SUPPORT())


@client.slash_command()
async def secret(ctx):
  await ctx.send("click on below link to reveal secret||Listen we r not hackers u can trust us||",view=rick())
  

@client.slash_command()
async def uptime(ctx):
  uptimes = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
  await ctx.send(f" {uptimes}")
@client.slash_command()
async def vote(ctx):
  
  view = topn()
  
  await ctx.send("VOTE ME",view=view)





@client.slash_command(description = "generates image by context")
async def genimage(ctx: commands.Context, *, prompt: str):
    ETA = int(time.time() + 60)
    msg = await ctx.send(f"Just a moment... ETA : <t:{ETA}:R>")
    generator = Craiyon()
    result = generator.generate(prompt)
    images = result.images
    
    for i in images:
        image = BytesIO(base64.decodebytes(i.encode("utf-8")))
        return await msg.edit(content = "Content generated by **craiyon.com**", file = nextcord.File(image, "craiyon.png"))





@client.slash_command()
@commands.has_permissions(manage_channels=True)
async def setchannel(ctx, *, channel: nextcord.TextChannel):
  cid = {
    "guild_id":ctx.guild.id,"welcome_id":channel.id
  }
  await welcome.insert_one(cid)
  message = await ctx.send(embed = nextcord.Embed(title=" welcome has successful fully set",description=f"<#{channel.id}>"))





@client.slash_command()
async def leavechannel(ctx, *, channel: nextcord.TextChannel):
  cid = {
    "guild_id":ctx.guild.id,"leave_id":channel.id
  }
  await leave.insert_one(cid)
  message = await ctx.send(embed = nextcord.Embed(title=" successfully set leave channel",description=f"<#{channel.id}>"))
















@client.command()
async def chat(ctx, *, message):
    chat = f'http://api.brainshop.ai/get?bid=153868&key=rcKonOgrUFmn5usX&uid=1&msg={message}'
    url = chat.replace(" ", "%20")
    hm = urllib.request.urlopen(url)
    data = json.load(hm)
    chatw = data['cnt']
    await ctx.send(f'''{chatw}''')
    print(f" {chat}")



@client.command()
async def c(ctx, *, message):
    chat = f'http://api.brainshop.ai/get?bid=153868&key=rcKonOgrUFmn5usX&uid=1&msg={message}'
    url = chat.replace(" ", "%20")
    hm = urllib.request.urlopen(url)
    data = json.load(hm)
    chatw = data['cnt']
    await ctx.send(f'''{chatw}''')
    print(f" {chat}")


@client.event
async def on_command_error(ctx, err):
  hi = await ctx.send(f"{err}")
  b = client.get_channel(972006886784258068)
  await b.send(f"{err}")
  await asyncio.sleep(6)
  await hi.delete()







@client.command()
async def save(ctx,name: str, *,save: str):
  u = ctx.message.author
  await cd.insert_one({"id": u.id,"name": name,"save": save})
  await ctx.send(f"successfully saved the data in db")
  
@client.command()
async def find(ctx, *, name:str):
  u = ctx.message.author
  hi = await cd.find_one({"id": u.id,"name": name})
  if hi is None:
    await ctx.send("could not find anything like that")
  else:
    b = ctx.message.author
    hm = await cd.find_one({"id":b.id,"name":name})
    gm = hm['save']
    ph = hm['name']
    await ctx.send(f"""*{ph}*
    ```{gm}```""")






@client.event
async def on_command(ctx):
  channel = client.get_channel(993515121521479700)
  await channel.send("command used")




  
client.run(os.getenv('token'))