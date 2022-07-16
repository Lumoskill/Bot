from discord.ext import commands
from datetime import datetime
import discord  # импортируем библиотеку discord.


class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.Cog.listener()
    async def on_message(self, message):
        username = str(message.author)  # .split("#")[0] (без # и цифр)
        channel = str(message.channel.name)
        user_message = str(message.content)
        print(f'Сообщение: {user_message}\nПользователь: {username}\nКанал: {channel}\nᅠ')  # Логи в Pycharm.

    @commands.Cog.listener()
    async def on_member_join(self, member):
        create_acc = member.created_at.strftime('`%d/%m/%Y %H:%M`')
        join = discord.Embed(description=f'{member.mention} **присоединился к серверу.**',
                             timestamp=datetime.now(), color=0x008000)
        join.set_author(name=member, icon_url=member.avatar)
        join.add_field(name=':timer: **Аккаунт создан:**', value=create_acc, inline=False)
        join.set_thumbnail(url=member.avatar)
        join.set_footer(text=f'{member.guild.name}')
        await self.bot.get_channel(992759616595296256).send(embed=join)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        remove = discord.Embed(description=f'{member.mention} **покинул сервер.**',
                               timestamp=datetime.now(), color=0xFF0000)
        remove.set_author(name=member, icon_url=member.avatar)
        remove.set_thumbnail(url=member.avatar)
        remove.set_footer(text=f'{member.guild.name}')
        await self.bot.get_channel(992759616595296256).send(embed=remove)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.content == '':
            pass
        else:
            edit = discord.Embed(description=f':pencil2: **Сообщение от {before.author.mention} изменено в '
                                             f'{before.channel.mention}.** [Перейти к сообщению]'
                                             f'(https://discord.com/channels/{before.guild.id}/{before.channel.id}/'
                                             f'{before.id})',
                                 timestamp=datetime.now(), color=0xFFFF00)
            edit.set_author(name=before.author, icon_url=before.author.avatar)
            edit.set_footer(text=f'{before.guild.name}')
            try:
                edit.add_field(name='**До этого:**', value=f'```{before.content}```', inline=False)
                edit.add_field(name='**Сейчас:**', value=f'```{after.content}```', inline=False)
            except:
                edit.add_field(name="Сообщение", value=f"Не удалось загрузить!", inline=False)
            await self.bot.get_channel(992759616595296256).send(embed=edit)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.content == '':
            pass
        else:
            del_m = discord.Embed(description=f':wastebasket: **Сообщение от {message.author.mention} удалено в '
                                              f'{message.channel.mention}.\n \n** {message.content}',
                                  timestamp=datetime.now(), color=0x4169E1)
            del_m.set_author(name=message.author, icon_url=message.author.avatar)
            del_m.set_footer(text=f'{message.guild.name}')
            await self.bot.get_channel(992759616595296256).send(embed=del_m)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState,
                                    after: discord.VoiceState):
        if before.channel is None:
            ch = discord.Embed(description=f'{member.mention} **присоединился к голосовому каналу '
                                           f'`{after.channel}`.**', timestamp=datetime.now(), color=0x4169E1)
            ch.set_author(name=member, icon_url=member.avatar)
            ch.set_footer(text=f'{member.guild.name}')
            await self.bot.get_channel(992759616595296256).send(embed=ch)
        elif after.channel is None:
            ch = discord.Embed(description=f'{member.mention} **вышел из голосового канала '
                                           f'`{before.channel}`.**', timestamp=datetime.now(), color=0x4169E1)
            ch.set_author(name=member, icon_url=member.avatar)
            ch.set_footer(text=f'{member.guild.name}')
            await self.bot.get_channel(992759616595296256).send(embed=ch)
        elif before.channel != after.channel:
            ch = discord.Embed(description=f'{member.mention} **сменил голосовой канал `{before.channel}` => '
                                           f'`{after.channel}`.**', timestamp=datetime.now(), color=0x4169E1)
            ch.set_author(name=member, icon_url=member.avatar)
            ch.set_footer(text=f'{member.guild.name}')
            await self.bot.get_channel(992759616595296256).send(embed=ch)

    # @commands.Cog.listener()
    # async def on_member_kick(self, member: discord.Member, message):
        # await self.bot.get_channel(992759616595296256).send(f'{member.mention} выгнан пользователем {ctx.author}')

# ---------------------------------------------------------------------------------------------------------------------#


def setup(bot):
    bot.add_cog(Logs(bot))


# ---------------------------------------------------------------------------------------------------------------------#

# https://discord.com/channels/айди сервера/айди канала где было написано сообщение/айди самого сообщения

# ---------------------------------------------------------------------------------------------------------------------#
