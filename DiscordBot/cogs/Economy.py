from discord.ext import commands
from discord.ext import tasks
import discord  # импортируем библиотеку discord.
from launch import open_acc, get_bank
from datetime import datetime
from func import *
import random
import datetime


class Eco(commands.Cog):
    def __init__(self, bot):
        self.guild = None
        self.bot = bot

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.command()
    async def balance(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        if member.id == 377030335982075905:
            if ctx.author.id == 377030335982075905:
                await open_acc(member)
                users = await get_bank()
                member_bank = users[str(member.id)]['wallet']
                balance = discord.Embed(description=f'**Баланс {member.mention}: *{member_bank}$***')
                await ctx.send(embed=balance)
            else:
                return await ctx.send('Секрет)')
        else:
            await open_acc(member)
            users = await get_bank()
            member_bank = users[str(member.id)]['wallet']
            balance = discord.Embed(description=f'**Баланс {member.mention}: *{member_bank}$***')
            await ctx.send(embed=balance)

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.command()
    async def mr(self, ctx):
        await open_acc(ctx.author)
        users = await get_bank()
        author_bank = users[str(ctx.author.id)]['wallet']
        rabot = discord.utils.get(ctx.guild.roles, id=997844839662112818)
        obecp = discord.utils.get(ctx.guild.roles, id=997844978871042108)
        bogat = discord.utils.get(ctx.guild.roles, id=997845044755169392)
        mil = discord.utils.get(ctx.guild.roles, id=997845145510744095)
        sheih = discord.utils.get(ctx.guild.roles, id=997845231791788122)
        if author_bank < 1000:
            await ctx.send(f'{ctx.author.display_name}, на данный момент у вас недостаточно средств для получения '
                           f'денежной роли!')
        if 1000 <= author_bank < 10000:
            if rabot not in ctx.author.roles:
                await ctx.author.remove_roles(obecp)
                await ctx.author.remove_roles(bogat)
                await ctx.author.remove_roles(mil)
                await ctx.author.remove_roles(sheih)
                await ctx.author.add_roles(rabot)
                await ctx.send(f'Поздравляем {ctx.author.mention}! Вы получили роль {rabot.mention}.')
            else:
                await ctx.author.remove_roles(obecp)
                await ctx.author.remove_roles(bogat)
                await ctx.author.remove_roles(mil)
                await ctx.author.remove_roles(sheih)
                await ctx.send(f'{ctx.author.mention} У вас уже есть роль {rabot.mention}.'
                               f'\nДо следующей денежной роли осталось: ***{10000 - author_bank}$***.')
        if 10000 <= author_bank < 100000:
            if obecp not in ctx.author.roles:
                await ctx.author.remove_roles(rabot)
                await ctx.author.remove_roles(bogat)
                await ctx.author.remove_roles(mil)
                await ctx.author.remove_roles(sheih)
                await ctx.author.add_roles(obecp)
                await ctx.send(f'Поздравляем {ctx.author.mention}! Вы получили роль {obecp.mention}.')
            else:
                await ctx.author.remove_roles(rabot)
                await ctx.author.remove_roles(bogat)
                await ctx.author.remove_roles(mil)
                await ctx.author.remove_roles(sheih)
                await ctx.send(f'{ctx.author.mention} У вас уже есть роль {obecp.mention}.'
                               f'\nДо следующей денежной роли осталось: ***{100000 - author_bank}$***.')
        if 100000 <= author_bank < 1000000:
            if bogat not in ctx.author.roles:
                await ctx.author.remove_roles(rabot)
                await ctx.author.remove_roles(obecp)
                await ctx.author.remove_roles(mil)
                await ctx.author.remove_roles(sheih)
                await ctx.author.add_roles(bogat)
                await ctx.send(f'Поздравляем {ctx.author.mention}! Вы получили роль {bogat.mention}.')
            else:
                await ctx.author.remove_roles(rabot)
                await ctx.author.remove_roles(obecp)
                await ctx.author.remove_roles(mil)
                await ctx.author.remove_roles(sheih)
                await ctx.send(f'{ctx.author.mention} У вас уже есть роль {bogat.mention}.'
                               f'\nДо следующей денежной роли осталось: ***{1000000 - author_bank}$***.')
        if 1000000 <= author_bank < 10000000:
            if mil not in ctx.author.roles:
                await ctx.author.remove_roles(rabot)
                await ctx.author.remove_roles(obecp)
                await ctx.author.remove_roles(bogat)
                await ctx.author.remove_roles(sheih)
                await ctx.author.add_roles(mil)
                await ctx.send(f'Поздравляем {ctx.author.mention}! Вы получили роль {mil.mention}.')
            else:
                await ctx.author.remove_roles(rabot)
                await ctx.author.remove_roles(obecp)
                await ctx.author.remove_roles(bogat)
                await ctx.author.remove_roles(sheih)
                await ctx.send(f'{ctx.author.mention} У вас уже есть роль {mil.mention}.'
                               f'\nДо следующей денежной роли осталось: ***{10000000 - author_bank}$***.')
        if author_bank >= 10000000:
            if sheih not in ctx.author.roles:
                await ctx.author.remove_roles(rabot)
                await ctx.author.remove_roles(obecp)
                await ctx.author.remove_roles(bogat)
                await ctx.author.remove_roles(mil)
                await ctx.author.add_roles(sheih)
                await ctx.send(f'Поздравляем {ctx.author.mention}! Вы получили роль {sheih.mention}.')
            else:
                await ctx.author.remove_roles(rabot)
                await ctx.author.remove_roles(obecp)
                await ctx.author.remove_roles(bogat)
                await ctx.author.remove_roles(mil)
                await ctx.send(f'{ctx.author.mention} У вас уже есть роль {sheih.mention}.\nВы уже достигли '
                               f'максимальной денежной роли!')

# ---------------------------------------------------------------------------------------------------------------------#

    @tasks.loop()
    async def check_timecase(self):
        current = datetime.datetime.now()
        timecase = load_json("jsons/timecase.json")
        users, times = list(timecase.keys()), list(timecase.values())
        for i in range(len(times)):
            time = times[i]
            casetime = datetime.datetime.strptime(str(time), "%c")
            if casetime < current:
                user_id = users[times.index(time)]
                try:
                    member = await self.guild.fetch_member(int(user_id))
                    timecase.pop(str(member.id))
                except discord.NotFound:
                    pass
                write_json("jsons/timecase.json", timecase)

    @commands.command()
    async def case(self, ctx):
        await open_acc(ctx.author)
        users = await get_bank()
        author_bank = users[str(ctx.author.id)]['wallet']
        s = []
        for x in range(101):
            s.append(x)
        rand_m = random.choice(s)
        seconds = 86400
        case_expiration = (datetime.datetime.now() + datetime.timedelta(seconds=int(seconds))).strftime("%c")
        timecase = load_json("jsons/timecase.json")
        try:
            member_case = timecase[str(ctx.author.id)]
            current = datetime.datetime.now()
            timecase = load_json("jsons/timecase.json")
            users, times = list(timecase.keys()), list(timecase.values())
            for i in range(len(times)):
                time = times[i]
                casetime = datetime.datetime.strptime(str(time), "%c")
                time_ost = str(casetime - current)
            return await ctx.send(f"Вы уже открывали кейс. До следующего открытия кейса осталось ***{time_ost[:8]}***")
        except:
            users[str(ctx.author.id)]['wallet'] += rand_m
            write_json('jsons/bank.json', users)
            author_bank = users[str(ctx.author.id)]['wallet']
            if rand_m == 0:
                await ctx.send(f'{ctx.author.mention} Увы... Вам ничего не выпало.')
            else:
                await ctx.send(f'{ctx.author.mention} Вам выпало: {rand_m}$.\nВаш баланс: {author_bank}$')
            timecase[str(ctx.author.id)] = str(case_expiration)
            write_json("jsons/timecase.json", timecase)

    @commands.Cog.listener()
    async def on_ready(self):
        self.guild = await self.bot.fetch_guild(852691105077657641)
        self.check_timecase.start()

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.command()
    async def pay(self, ctx, num: int, member: discord.Member = None):
        if member is None:
            try_pay = discord.Embed(description='**Пользователь не указан!**')
            return await ctx.send(embed=try_pay, delete_after=3)
        if num < 0:
            try_pay_otr = discord.Embed(description='**Перевод должен быть положительным!**')
            return await ctx.send(embed=try_pay_otr, delete_after=3)
        await open_acc(ctx.author)
        await open_acc(member)
        users = await get_bank()
        member_bank = users[str(member.id)]['wallet']
        author_bank = users[str(ctx.author.id)]['wallet']
        if author_bank < num:
            try_pay_ned = discord.Embed(description='**Недостаточно средств!**')
            return await ctx.send(embed=try_pay_ned, delete_after=3)
        users[str(member.id)]['wallet'] += num
        users[str(ctx.author.id)]['wallet'] -= num
        write_json('jsons/bank.json', users)
        pay = discord.Embed(description=f'**{ctx.author.mention} перевёл {member.mention} *{num}$***')
        await ctx.send(embed=pay)

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.command()
    async def add(self, ctx, num: int, member: discord.Member = None):
        role_own = discord.utils.get(ctx.guild.roles, name="Owner")
        role_sys_adm = discord.utils.get(ctx.guild.roles, name="System Admin")
        if role_own in ctx.author.roles or role_sys_adm in ctx.author.roles:
            if member is None:
                try_add = discord.Embed(description='**Пользователь не указан!**')
                return await ctx.send(embed=try_add, delete_after=3)
            if num < 0:
                try_add_otr = discord.Embed(description='**Перевод должен быть положительным!**')
                return await ctx.send(embed=try_add_otr, delete_after=3)
            await open_acc(member)
            users = await get_bank()
            member_bank = users[str(member.id)]['wallet']
            if member_bank < 0:
                users[str(member.id)]['wallet'] = 0
            users[str(member.id)]['wallet'] += num
            write_json('jsons/bank.json', users)
            member_bank = users[str(member.id)]['wallet']
            add = discord.Embed(description=f'**{ctx.author.mention} начислил {member.mention}: *{num}$***\nᅠ '
                                            f'\n**Баланс {member.mention}: *{member_bank}$***',
                                                    color=0x008000)
            try_add_t = discord.Embed(description=f'Пользователь {ctx.author.mention} воспользовался командой '
                                                f'\n```.add {num} {member.mention}```',
                                    timestamp=datetime.now(), color=0x4169E1)
            try_add_t.set_author(name=ctx.author, icon_url=ctx.author.avatar)
            try_add_t.set_footer(text=f'{ctx.guild.name}')
            await ctx.send(embed=add)
            await self.bot.get_channel(992759616595296256).send(embed=try_add_t)
        else:
            add_error = discord.Embed(description='Недостаточно прав для использования данной команды!')
            try_add = discord.Embed(description=f'Пользователь {ctx.author.mention} попытался воспользоваться командой '
                                              f'\n```.add {num} {member.mention}```',
                                              timestamp=datetime.now(), color=0x4169E1)
            try_add.set_author(name=ctx.author, icon_url=ctx.author.avatar)
            try_add.set_footer(text=f'{ctx.guild.name}')
            await ctx.message.delete()
            await ctx.send(embed=add_error, delete_after=3)
            await self.bot.get_channel(992759616595296256).send(embed=try_add)

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.command()
    async def rem(self, ctx, num: int, member: discord.Member = None):
        role_own = discord.utils.get(ctx.guild.roles, name="Owner")
        role_sys_adm = discord.utils.get(ctx.guild.roles, name="System Admin")
        if role_own in ctx.author.roles or role_sys_adm in ctx.author.roles:
            if member is None:
                try_rem = discord.Embed(description='**Пользователь не указан!**')
                return await ctx.send(embed=try_rem, delete_after=3)
            await open_acc(member)
            users = await get_bank()
            member_bank = users[str(member.id)]['wallet']
            if member_bank < num:
                try_rem_not = discord.Embed(description=f'**Ошибка! У пользователя {member.mention} на счету: '
                                                        f'*{member_bank}$***')
                return await ctx.send(embed=try_rem_not, delete_after=3)
            users[str(member.id)]['wallet'] -= num
            write_json('jsons/bank.json', users)
            member_bank = users[str(member.id)]['wallet']
            rem = discord.Embed(description=f'**{ctx.author.mention} снял у {member.mention}: *{num}$***\nᅠ '
                                            f'\n**Баланс {member.mention}: *{member_bank}$***', color=0xFF0000)
            try_rem_t = discord.Embed(description=f'Пользователь {ctx.author.mention} воспользовался командой '
                                                f'\n```.rem {num} {member.mention}```',
                                    timestamp=datetime.now(), color=0x4169E1)
            try_rem_t.set_author(name=ctx.author, icon_url=ctx.author.avatar)
            try_rem_t.set_footer(text=f'{ctx.guild.name}')
            await ctx.send(embed=rem)
            await self.bot.get_channel(992759616595296256).send(embed=try_rem_t)
        else:
            rem_error = discord.Embed(description='Недостаточно прав для использования данной команды!')
            try_rem = discord.Embed(description=f'Пользователь {ctx.author.mention} попытался воспользоваться командой '
                                                f'\n```.add {num} {member.mention}```',
                                    timestamp=datetime.now(), color=0x4169E1)
            try_rem.set_author(name=ctx.author, icon_url=ctx.author.avatar)
            try_rem.set_footer(text=f'{ctx.guild.name}')
            await ctx.message.delete()
            await ctx.send(embed=rem_error, delete_after=3)
            await self.bot.get_channel(992759616595296256).send(embed=try_rem)

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.command()
    async def rb(self, ctx, num: int, *, reason=None):
        if reason.lower() in ['красное', 'чёрное', 'черное']:
            await open_acc(ctx.author)
            users = await get_bank()
            author_bank = users[str(ctx.author.id)]['wallet']
            user_message = ctx.message.content
            rb = ['красное', 'чёрное']
            rb_ch = random.choice(rb)
            if reason.lower() == 'красное':
                if rb_ch == 'красное':
                    users[str(ctx.author.id)]['wallet'] += num
                    write_json('jsons/bank.json', users)
                    author_bank = users[str(ctx.author.id)]['wallet']
                    kr_w = discord.Embed(description=f'Поздравляем! Вы выиграли ***{num}$***. Выпало **{rb_ch}**.\n '
                                                     f'Ваш баланс: ***{author_bank}$***', color=0xFF0000)
                    await ctx.send(embed=kr_w)
                elif rb_ch == 'чёрное':
                    users[str(ctx.author.id)]['wallet'] -= num
                    write_json('jsons/bank.json', users)
                    author_bank = users[str(ctx.author.id)]['wallet']
                    kr_l = discord.Embed(description=f'Увы... Вы проиграли ***{num}$***. Выпало **{rb_ch}**.\n'
                                                     f'Ваш баланс: ***{author_bank}$***')
                    await ctx.send(embed=kr_l)
            if reason.lower() == 'чёрное' or reason.lower() == 'черное':
                if rb_ch == 'чёрное':
                    users[str(ctx.author.id)]['wallet'] += num
                    write_json('jsons/bank.json', users)
                    author_bank = users[str(ctx.author.id)]['wallet']
                    ch_w = discord.Embed(description=f'Поздравляем! Вы выиграли ***{num}$***. Выпало **{rb_ch}**.\n '
                                                     f'Ваш баланс: ***{author_bank}$***')
                    await ctx.send(embed=ch_w)
                elif rb_ch == 'красное':
                    users[str(ctx.author.id)]['wallet'] -= num
                    write_json('jsons/bank.json', users)
                    author_bank = users[str(ctx.author.id)]['wallet']
                    ch_l = discord.Embed(description=f'Увы... Вы проиграли ***{num}$***. Выпало **{rb_ch}**.\n'
                                                     f'Ваш баланс: ***{author_bank}$***', color=0xFF0000)
                    await ctx.send(embed=ch_l)
        else:
            await ctx.send('Вы указали неправильный цвет или не указали его вовсе!')

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.command()
    async def coin(self, ctx, num: int, *, reason=None):
        if reason.lower() in ['решка', 'орёл', 'орел']:
            await open_acc(ctx.author)
            users = await get_bank()
            author_bank = users[str(ctx.author.id)]['wallet']
            user_message = ctx.message.content
            coin = ['решка', 'орёл']
            coin_ch = random.choice(coin)
            if reason.lower() == 'решка':
                if coin_ch == 'решка':
                    users[str(ctx.author.id)]['wallet'] += num
                    write_json('jsons/bank.json', users)
                    author_bank = users[str(ctx.author.id)]['wallet']
                    r_w = discord.Embed(description=f'Поздравляем! Вы выиграли ***{num}$***. Выпала **{coin_ch}**.\n '
                                                     f'Ваш баланс: ***{author_bank}$***', color=0xFFD700)
                    await ctx.send(embed=r_w)
                elif coin_ch == 'орёл':
                    users[str(ctx.author.id)]['wallet'] -= num
                    write_json('jsons/bank.json', users)
                    author_bank = users[str(ctx.author.id)]['wallet']
                    r_l = discord.Embed(description=f'Увы... Вы проиграли ***{num}$***. Выпал **{coin_ch}**.\n'
                                                     f'Ваш баланс: ***{author_bank}$***', color=0xFFD700)
                    await ctx.send(embed=r_l)
            if reason.lower() == 'орёл' or reason.lower() == 'орел':
                if coin_ch == 'орёл':
                    users[str(ctx.author.id)]['wallet'] += num
                    write_json('jsons/bank.json', users)
                    author_bank = users[str(ctx.author.id)]['wallet']
                    o_w = discord.Embed(description=f'Поздравляем! Вы выиграли ***{num}$***. Выпал **{coin_ch}**.\n '
                                                     f'Ваш баланс: ***{author_bank}$***', color=0xFFD700)
                    await ctx.send(embed=o_w)
                elif coin_ch == 'решка':
                    users[str(ctx.author.id)]['wallet'] -= num
                    write_json('jsons/bank.json', users)
                    author_bank = users[str(ctx.author.id)]['wallet']
                    o_l = discord.Embed(description=f'Увы... Вы проиграли ***{num}$***. Выпала **{coin_ch}**.\n'
                                                     f'Ваш баланс: ***{author_bank}$***', color=0xFFD700)
                    await ctx.send(embed=o_l)
        else:
            await ctx.send('Вы указали неправильную сторону монетки или не указали её вовсе!')

# ---------------------------------------------------------------------------------------------------------------------#


def setup(bot):
    bot.add_cog(Eco(bot))


# ---------------------------------------------------------------------------------------------------------------------#
