from PIL import Image
import nextcord
from nextcord.ext import commands
from io import BytesIO


class wanted(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def wanted(self, ctx, member: nextcord.Member = ''):
        if member == '':
            member = ctx.author

        wanted = Image.open('hi.jpeg')

        asset = member.display_avatar.with_size(256)
        data = BytesIO(await asset.read())

        pfp = Image.open(data)

        pfp = pfp.resize((255, 255))
        wanted.paste(pfp, (98, 200))
        wanted.save('wanted.png')
        await ctx.send(file=nextcord.File('wanted.png'))




def setup(client):
    client.add_cog(wanted(client))