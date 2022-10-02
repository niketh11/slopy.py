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
from PIL import Image
import time
client = commands.Bot(command_prefix=['#','<@970577992877223946> '], intents = nextcord.Intents.all())
@client.event
async def on_ready():
  
    channel = client.get_channel(999541224975376486)
    print(f'{client.user} is ONLINE!')
    await channel.send('online')
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f"UNDER MAINTENANCE #help"))

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
    if client.user.mentioned_in(message):
      
      embed = nextcord.Embed(title = "Hey wassup?", description="my prefix is `#`")
      embed.set_image(url="https://media.discordapp.net/attachments/949881939576389645/1025061501901471794/images_29.jpg")
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
                nextcord.SelectOption(label="INFO", description="Shows info commands", emoji="<a:info:993763572888899584>",value="in",),
                nextcord.SelectOption(label="Modration", description="Shows modration commands",emoji='<:moderation:990580070466846720>', value="mod"),
                nextcord.SelectOption(label="Fun", description="Shows fun commands", emoji = '<a:fun:1025273034543730768>',value="fun"),


                nextcord.SelectOption(label="Games", description="Shows Game commands", emoji = '<a:games:1025277092461559849>',value="game"),                
              
                nextcord.SelectOption(label="Actions", description="Shows action commands", emoji='<:actionshin:1025273873450676294>',value="action"),              
                nextcord.SelectOption(label="Utility", description="Shows utility commands", emoji='<:Utility:990582796198244382>',value="util"),

                ]
            super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)
        async def callback(self, interaction: nextcord.Interaction):

            if self.values[0] == "in":
               
                await interaction.response.send_message(embed = nextcord.Embed(title="<a:info:993763572888899584>|Info",description="```USERINFO,SERVERINFO,INVITE,SUPPORT,UPTIME```"))
                                                        
                                                          
            elif self.values[0] == "mod":
                await interaction.response.send_message(embed = nextcord.Embed(title='<:moderation:990580070466846720>Modration',description = '```kick,Ban,lock,unlock,purge,mute,unmute```'))
            elif self.values[0] == "fun":
                await interaction.response.send_message(embed = nextcord.Embed(title='<a:fun:1025273034543730768>Fun',description='```hack,meme,lovecalc,lie,8ball,coinflip,dice, fliptext,virus,wanted,secret```'))                


            elif self.values[0] == "action":
                await interaction.response.send_message(embed = nextcord.Embed(title="<:actionshin:1025273873450676294>Action",description='```slap,hug,pat``'))                



            elif self.values[0] == "util":
                await interaction.response.send_message(embed = nextcord.Embed(title='<:Utility:990582796198244382>Utility',description='```dm,invites,members,rate,say,slowmode,avatar,8ball```'))                
            elif self.values[0] == "game":
                await interaction.response.send_message(embed = nextcord.Embed(title='<a:games:1025277092461559849>Games',description='```rps```'))

              
    class SelectView(nextcord.ui.View):
        def __init__(self, *, timeout = 180):
            super().__init__(timeout=timeout)
            self.add_item(Select())
    embed = nextcord.Embed(title='hey wassup?',description='i dont want to say anything:/ just try ur own')
    embed.set_thumbnail(url=client.user.display_avatar)
    embed.set_image(url="https://media.discordapp.net/attachments/949881939576389645/1025061501901471794/images_29.jpg")

    
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
  await ctx.send(f"Im up for {uptimes}")









client.run(os.getenv('token'))