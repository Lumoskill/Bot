from discord.ext import commands
from datetime import datetime
import discord  # импортируем библиотеку discord.


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.command()  # Впринципе гуд.
    async def clear(self, ctx, amount: int):
        role_own = discord.utils.get(ctx.guild.roles, name="Owner")
        role_sys_adm = discord.utils.get(ctx.guild.roles, name="System Admin")
        if role_own in ctx.author.roles or role_sys_adm in ctx.author.roles:
            if amount <= 100:
                if amount == 1:
                    await ctx.channel.purge(limit=amount + 1)
                    clear = discord.Embed(description=f'Удалено сообщений: 1')
                    await ctx.send(embed=clear, delete_after=3)
                    del_m = discord.Embed(description=f':wastebasket: **Сообщение от {ctx.author.mention} удалено в '
                                                      f'{ctx.channel.mention}.\n ** ```.clear 1```\n'
                                                      f'**:wastebasket: Сообщение, '
                                                      f'которое было написано '
                                                      f'на самом деле:**\n```.clear {amount}```',
                                          timestamp=datetime.now(), color=0x4169E1)
                    del_m.set_author(name=ctx.author, icon_url=ctx.author.avatar)
                    del_m.set_footer(text=f'{ctx.guild.name}')
                    await self.bot.get_channel(992759616595296256).send(embed=del_m)
                else:
                    deleted_messages = await ctx.channel.purge(limit=amount + 1)
                    clear = discord.Embed(description=f'Удалено сообщений: {len(deleted_messages) - 1}')
                    await ctx.send(embed=clear, delete_after=3)
                    del_m = discord.Embed(description=f':wastebasket: **Сообщение от {ctx.author.mention} удалено в '
                                                      f'{ctx.channel.mention}.\n ** ```.clear '
                                                      f'{len(deleted_messages) - 1}```\n**:wastebasket: Сообщение, '
                                                      f'которое '
                                                      f'было написано '
                                                      f'на самом деле:**\n```.clear {amount}```',
                                          timestamp=datetime.now(), color=0x4169E1)
                    del_m.set_author(name=ctx.author, icon_url=ctx.author.avatar)
                    del_m.set_footer(text=f'{ctx.guild.name}')
                    await self.bot.get_channel(992759616595296256).send(embed=del_m)
            else:
                clear = discord.Embed(description='Лимит команды clear: 100 сообщений!')
                try_c = discord.Embed(
                    description=f'**Пользователь {ctx.author.mention} попытался воспользоваться командой** '
                                f'`clear`.\nВ параметре для удаления было указано более 100 сообщений, а именно:'
                                f'\n```.clear {amount}```',
                    timestamp=datetime.now(), color=0x4169E1)
                try_c.set_author(name=ctx.author, icon_url=ctx.author.avatar)
                try_c.set_footer(text=f'{ctx.guild.name}')
                await ctx.channel.purge(limit=1)  # удалить именно ошибочное сообщение.
                await ctx.send(embed=clear, delete_after=3)
                await self.bot.get_channel(992759616595296256).send(embed=try_c)
        else:
            clear_error = discord.Embed(description='Недостаточно прав для использования данной команды!')
            try_c = discord.Embed(description=f'Пользователь {ctx.author.mention} попытался воспользоваться командой '
                                              f'\n```.clear {amount}```',
                                  timestamp=datetime.now(), color=0x4169E1)
            try_c.set_author(name=ctx.author, icon_url=ctx.author.avatar)
            try_c.set_footer(text=f'{ctx.guild.name}')
            await ctx.message.delete()
            await ctx.send(embed=clear_error, delete_after=3)
            await self.bot.get_channel(992759616595296256).send(embed=try_c)

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.command()  # Впринципе гуд (потом сделать так, чтобы except работал).
    async def ban(self, ctx, member: discord.Member, *, reason='Не указана'):
        role_own = discord.utils.get(ctx.guild.roles, name="Owner")
        role_sys_adm = discord.utils.get(ctx.guild.roles, name="System Admin")
        if role_own in ctx.author.roles or role_sys_adm in ctx.author.roles:
            if member != ctx.author:
                try:
                    ban = discord.Embed(
                        description=f'**:no_entry_sign: Пользователь {member.mention} был забанен пользователем'
                                    f' {ctx.author.mention}.**\nᅠ\n**Причина:** ```{reason}```.',
                        timestamp=datetime.now(), color=0xFF0000)
                    ban.set_author(name=ctx.author, icon_url=ctx.author.avatar)
                    ban.set_footer(text=f'{ctx.guild.name}')
                    await member.ban(reason=reason)
                    await ctx.message.delete()
                    await ctx.send(f'{member.mention} успешно забанен!', delete_after=3)
                    await self.bot.get_channel(992759616595296256).send(embed=ban)
                except:  # Не работает!
                    await ctx.send('Данный пользователь отсутствует на сервере или уже забанен!', delete_after=3)
            else:
                await ctx.send('Вы не можете забанить себя!', delete_after=3)
        else:
            ban_error = discord.Embed(title='Недостаточно прав для использования данной команды!')
            try_b = discord.Embed(description=f'Пользователь {ctx.author.mention} попытался воспользоваться командой '
                                              f'\n```.ban {member.mention}```',
                                  timestamp=datetime.now(), color=0x4169E1)
            try_b.set_author(name=ctx.author, icon_url=ctx.author.avatar)
            try_b.set_footer(text=f'{ctx.guild.name}')
            await ctx.message.delete()
            await ctx.send(embed=ban_error, delete_after=3)
            await self.bot.get_channel(992759616595296256).send(embed=try_b)

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.command()  # Впринципе гуд.
    async def unban(self, ctx, id: int):
        role_own = discord.utils.get(ctx.guild.roles, name="Owner")
        role_sys_adm = discord.utils.get(ctx.guild.roles, name="System Admin")
        if role_own in ctx.author.roles or role_sys_adm in ctx.author.roles:
            user = await self.bot.fetch_user(id)
            try:
                unban = discord.Embed(
                    description=f'**:white_check_mark: Пользователь {user.mention} был разбанен пользователем '
                                f'{ctx.author.mention}.**',
                    timestamp=datetime.now(), color=0x008000)
                unban.set_author(name=ctx.author, icon_url=ctx.author.avatar)
                unban.set_footer(text=f'{ctx.guild.name}')
                await ctx.guild.unban(user)
                await ctx.message.delete()
                await ctx.send(f'{user.mention} разбанен!', delete_after=3)
                await self.bot.get_channel(992759616595296256).send(embed=unban)
            except:
                unban = discord.Embed(title='Данный пользователь не забанен!')
                try_ub = discord.Embed(
                    description=f'Пользователь {ctx.author.mention} попытался воспользоваться командой '
                                f'\n```.unban {user.mention}```',
                    timestamp=datetime.now(), color=0x4169E1)
                try_ub.set_author(name=ctx.author, icon_url=ctx.author.avatar)
                try_ub.set_footer(text=f'{ctx.guild.name}')
                await ctx.message.delete()
                await ctx.send(embed=unban, delete_after=3)
                await self.bot.get_channel(992759616595296256).send(embed=try_ub)
        else:
            user = await self.bot.fetch_user(id)
            unban_error = discord.Embed(title='Недостаточно прав для использования данной команды!')
            try_ub = discord.Embed(description=f'Пользователь {ctx.author.mention} попытался воспользоваться командой '
                                               f'\n```.unban {user.mention}```',
                                   timestamp=datetime.now(), color=0x4169E1)
            try_ub.set_author(name=ctx.author, icon_url=ctx.author.avatar)
            try_ub.set_footer(text=f'{ctx.guild.name}')
            await ctx.message.delete()
            await ctx.send(embed=unban_error, delete_after=3)
            await self.bot.get_channel(992759616595296256).send(embed=try_ub)

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.command()  # Впринципе гуд.
    async def mute(self, ctx, member: discord.Member, *, reason='Не указана'):
        role_own = discord.utils.get(ctx.guild.roles, name="Owner")
        role_sys_adm = discord.utils.get(ctx.guild.roles, name="System Admin")
        role_mute = discord.utils.get(ctx.guild.roles, name="Muted")
        if role_own in ctx.author.roles or role_sys_adm in ctx.author.roles:
            if role_mute not in member.roles:
                if member != ctx.author:
                    await member.move_to(channel=None)
                    mute = discord.utils.get(ctx.guild.roles, name='Muted')
                    users = discord.utils.get(ctx.guild.roles, id=992082548333232128)
                    mut = discord.Embed(
                        description=f'**:mute: {member.mention} был замучен пользователем '
                                    f'{ctx.author.mention}.**\nᅠ\n**Причина:** ```{reason}```',
                        timestamp=datetime.now(), color=0xFF0000)
                    mut.set_author(name=ctx.author, icon_url=ctx.author.avatar)
                    mut.set_footer(text=f'{ctx.guild.name}')
                    await member.add_roles(mute)
                    await member.remove_roles(users)
                    await ctx.message.delete()
                    await ctx.send(f'{ctx.author.mention} замутил пользователя {member.mention}. Причина: {reason}.',
                                   delete_after=3)
                    await self.bot.get_channel(992759616595296256).send(embed=mut)
                else:
                    try_mute = discord.Embed(
                        description=f'Пользователь {ctx.author.mention} попытался воспользоваться командой '
                                    f'\n.mute {member.mention}',
                        timestamp=datetime.now(), color=0x4169E1)
                    try_mute.set_author(name=ctx.author, icon_url=ctx.author.avatar)
                    try_mute.set_footer(text=f'{ctx.guild.name}')
                    await ctx.message.delete()
                    await ctx.send('Вы не можете замутить себя!', delete_after=3)
                    await self.bot.get_channel(992759616595296256).send(embed=try_mute)
            else:
                try_mute = discord.Embed(
                    description=f'Пользователь {ctx.author.mention} попытался воспользоваться командой '
                                f'\n.mute {member.mention}',
                    timestamp=datetime.now(), color=0x4169E1)
                try_mute.set_author(name=ctx.author, icon_url=ctx.author.avatar)
                try_mute.set_footer(text=f'{ctx.guild.name}')
                await ctx.message.delete()
                await ctx.send(f'{member.mention} уже находится в муте!', delete_after=3)
                await self.bot.get_channel(992759616595296256).send(embed=try_mute)
        else:
            mute_error = discord.Embed(title='Недостаточно прав для использования данной команды!')
            try_mute = discord.Embed(
                description=f'Пользователь {ctx.author.mention} попытался воспользоваться командой '
                            f'\n.mute {member.mention}',
                timestamp=datetime.now(), color=0x4169E1)
            try_mute.set_author(name=ctx.author, icon_url=ctx.author.avatar)
            try_mute.set_footer(text=f'{ctx.guild.name}')
            await ctx.message.delete()
            await ctx.send(embed=mute_error, delete_after=3)
            await self.bot.get_channel(992759616595296256).send(embed=try_mute)

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.command()  # Впринципе гуд.
    async def unmute(self, ctx, member: discord.Member):
        role_own = discord.utils.get(ctx.guild.roles, name="Owner")
        role_sys_adm = discord.utils.get(ctx.guild.roles, name="System Admin")
        role_mute = discord.utils.get(ctx.guild.roles, name="Muted")
        if role_own in ctx.author.roles or role_sys_adm in ctx.author.roles:
            if role_mute in member.roles:
                if member != ctx.author:
                    unmute = discord.Embed(
                        description=f'**:white_check_mark: Пользователь {member.mention} был размучен пользователем '
                                    f'{ctx.author.mention}.**',
                        timestamp=datetime.now(), color=0x008000)
                    unmute.set_author(name=ctx.author, icon_url=ctx.author.avatar)
                    unmute.set_footer(text=f'{ctx.guild.name}')
                    mute = discord.utils.get(ctx.guild.roles, name='Muted')
                    users = discord.utils.get(ctx.guild.roles, id=992082548333232128)
                    await member.remove_roles(mute)
                    await member.add_roles(users)
                    await ctx.message.delete()
                    await ctx.send(f'{ctx.author.mention} размутил {member.mention}.', delete_after=3)
                    await self.bot.get_channel(992759616595296256).send(embed=unmute)
                else:
                    try_unmute = discord.Embed(
                        description=f'Пользователь {ctx.author.mention} попытался воспользоваться командой '
                                    f'\n.unmute {member.mention}',
                        timestamp=datetime.now(), color=0x4169E1)
                    try_unmute.set_author(name=ctx.author, icon_url=ctx.author.avatar)
                    try_unmute.set_footer(text=f'{ctx.guild.name}')
                    await ctx.message.delete()
                    await ctx.send('Вы не можете размутить себя!', delete_after=3)
                    await self.bot.get_channel(992759616595296256).send(embed=try_unmute)
            else:
                try_unmute = discord.Embed(
                    description=f'Пользователь {ctx.author.mention} попытался воспользоваться командой '
                                f'\n.unmute {member.mention}',
                    timestamp=datetime.now(), color=0x4169E1)
                try_unmute.set_author(name=ctx.author, icon_url=ctx.author.avatar)
                try_unmute.set_footer(text=f'{ctx.guild.name}')
                await ctx.message.delete()
                await ctx.send(f'{member.mention} не находится в муте!', delete_after=3)
                await self.bot.get_channel(992759616595296256).send(embed=try_unmute)
        else:
            unmute_error = discord.Embed(title='Недостаточно прав для использования данной команды!')
            try_unmute = discord.Embed(
                description=f'Пользователь {ctx.author.mention} попытался воспользоваться командой '
                            f'\n.unmute {member.mention}',
                timestamp=datetime.now(), color=0x4169E1)
            try_unmute.set_author(name=ctx.author, icon_url=ctx.author.avatar)
            try_unmute.set_footer(text=f'{ctx.guild.name}')
            await ctx.message.delete()
            await ctx.send(embed=unmute_error, delete_after=3)
            await self.bot.get_channel(992759616595296256).send(embed=try_unmute)

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = member.guild.get_role(996171351457017897)  # выдача роли при заходе на сервер.
        await member.add_roles(role)

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.command(pass_context=True)
    @commands.has_any_role(853028950288760834)
    async def verific(self, ctx):
        access = discord.Embed(
            title='Добро пожаловать в Lounge zone!',
            description='ᅠ \nЧтобы получить доступ к серверу, нажмите на реакцию.',
            color=0x8A2BE2
        )
        access.set_thumbnail(url='https://c.tenor.com/o9c6lRvOpMkAAAAd/dazai-dazai-osamu.gif')
        await ctx.message.delete()
        msg = await ctx.send(embed=access)
        await msg.add_reaction('🔑')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message = 996513165175181334
        if message == payload.message_id:
            member = payload.member
            guild = member.guild
            emoji = payload.emoji.name
            if emoji == '🔑':
                role_users = discord.utils.get(guild.roles, name='☆')
                role_new_users = discord.utils.get(guild.roles, name='🔒')
            # channel = self.bot.get_channel(payload.channel_id)
            # msg = await channel.fetch_message(payload.message_id)
            await member.remove_roles(role_new_users)
            await member.add_roles(role_users)
            # await msg.remove_reaction(emoji, member)  # убирается поставленная реакция пользователем.

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.command()
    async def users(self, ctx):
        await ctx.send(f'Количество пользователей на сервере: {ctx.guild.member_count}.')  # кол-во игроков на сервере.

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.command()
    @commands.has_any_role(853028950288760834)
    @commands.guild_only()
    async def kick(self, ctx, member: discord.Member, *, reason='Не указана.'):
        await member.kick(reason=reason)
        await ctx.message.delete()
        await ctx.send(f'{member.mention} выгнан!', delete_after=3)
        await self.bot.get_channel(992759616595296256).send(f'{member.mention} был выгнан пользователем '
                                                            f'{ctx.author.mention}.')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            kick_error = discord.Embed(title='Недостаточно прав для использования данной команды!')
            await ctx.message.delete()
            await ctx.send(embed=kick_error, delete_after=3)


# ---------------------------------------------------------------------------------------------------------------------#


def setup(bot):
    bot.add_cog(Moderation(bot))

# ---------------------------------------------------------------------------------------------------------------------#

# {ctx.author.name} - ник пользователя, совершившего команду.
# {member.display_name} - ник пользователя, над которым совершили команду.
# @commands.has_any_role(853028950288760834)  # Доступ к команде по роли.

# ---------------------------------------------------------------------------------------------------------------------#
