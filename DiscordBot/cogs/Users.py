from discord.ext import commands
from datetime import datetime
import discord  # импортируем библиотеку discord.
import random


class Users(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.Cog.listener()
    async def on_message(self, message):
        username = str(message.author).split("#")[0]  # Ник пользователя.
        channel = str(message.channel.name)
        user_message = str(message.content)
        if user_message.lower() == 'привет' or user_message.lower() == 'ку':
            await message.channel.send(f' Привет {message.author.mention}!')
        elif user_message.lower() == "hi" or user_message.lower() == "hello":
            await message.channel.send(f' Hello {message.author.mention}!')
        elif user_message.lower() == "bye" or user_message.lower() == "bb":
            await message.channel.send(f' Bye {message.author.mention}!')
            return

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.Cog.listener()  # Запрещённые слова.
    async def on_message(self, message):
        username = str(message.author).split("#")[0]  # Ник пользователя.
        channel = str(message.channel.name)
        user_message = str(message.content)
        if user_message.lower() in []:
            await message.channel.send(f'{message.author.mention} не стоит это здесь писать!')
            return

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.command()
    async def pr(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        roles = [role for role in member.roles if role != ctx.guild.default_role]
        info = discord.Embed(title=f'Информация о пользователе *{member.name}*', timestamp=datetime.now(),
                             color=0x8A2BE2)
        info.set_thumbnail(url=member.avatar)
        info.add_field(name='**ID:**', value=member.id, inline=False)
        info.add_field(name='**Псевдоним:**', value=member.display_name, inline=False)
        info.add_field(name='**Аккаунт создан:**', value=member.created_at.strftime('`%d/%m/%Y %H:%M`'), inline=False)
        info.add_field(name='**Вступил(а) на сервер:**', value=member.joined_at.strftime('`%d/%m/%Y %H:%M`'),
                       inline=False)
        info.add_field(name='**Роли:**', value=''.join(role.mention for role in roles), inline=False)
        info.add_field(name='**Высшая роль:**', value=member.top_role.mention, inline=False)
        info.add_field(name='**Бот?**', value='Да' if member.bot == True else 'Нет', inline=False)
        info.set_footer(text=f'{member.guild.name}')
        await ctx.send(embed=info)

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        avatar = discord.Embed(title=f'Аватарка *{member.display_name}*')
        avatar.set_image(url=member.avatar)
        await ctx.send(embed=avatar)

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.command()  # Доработать: если первое число меньше второго, если оба числа не указали, если отрицательные
    # числа, если одно из чисел не указали.
    async def rand(self, ctx, num1: int, num2: int):
        if num1 is None and num2 is None:
            try_rand = discord.Embed(description='Укажите в параметрах два числа!')
            await ctx.send(embed=try_rand)
        else:
            s = []
            for x in range(num1, num2+1):
                s.append(x)
            rand_num = random.choice(s)
            await ctx.send(rand_num)

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.command()
    async def yon(self, ctx):
        yon = ['Да', 'Нет']
        rand_yon = random.choice(yon)
        await ctx.send(rand_yon)

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.command()
    async def lol(self, ctx):
        await ctx.send('Lol')

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.command(name="reply")
    async def command_reply(self, ctx, *, text):
        await ctx.send(text)

    '''@commands.command()
    async def joke(self, ctx):
        channel = str(ctx.channel.name)
        jokes = [
            "One", "Two", 'Three', 'Four', 'Five'
        ]
        if channel == '🗯общение' or channel == '⚙команды' or channel == '🤖test_bot':
            await ctx.send(random.choice(jokes))'''

    @commands.command()
    async def help(self, ctx):
        channel = str(ctx.channel.name)
        member_id = 377030335982075905
        rabot = discord.utils.get(ctx.guild.roles, id=997844839662112818)
        obecp = discord.utils.get(ctx.guild.roles, id=997844978871042108)
        bogat = discord.utils.get(ctx.guild.roles, id=997845044755169392)
        mil = discord.utils.get(ctx.guild.roles, id=997845145510744095)
        sheih = discord.utils.get(ctx.guild.roles, id=997845231791788122)
        if channel == '⚙команды' or channel == '🤖test_bot' or channel == '🔒admin' or channel == '🖼заготовки':
            help = discord.Embed(title='Команды Lounge Bot', color=0x8A2BE2)
            help.add_field(name='ᅠ\n***Пользовательский команды***', value=f"ᅠ\n**.reply** (текст) *- повтор "
                                                                            f"сообщения пользователя ботом.*\nᅠ"
                                                       f"ᅠ\n**.joke** *- случайная шутка.* "
                                                       f"\n(В разработке! Свои шутки и анекдоты cкидывать в лс "
                                                       f"<@{member_id}>)\nᅠ"
                                                       f"ᅠ\n**.avatar** (пользователь) *- аватарка пользователя.*\nᅠ"
                                                       f"ᅠ\n**.pr** (пользователь) *- вся информация о пользователе."
                                                       f"*\nᅠᅠ\n**.rand** (1 число) (2 число) *- случайное число в "
                                                       f"пределах, указанных в параметрах команды.*\nᅠ"
                                                       f'ᅠ\n**.yon** *- если возникла трудность перед выбором '
                                                                           f'**"Да или нет"**, то данная команда вам '
                                                                           f'в помощь.*', inline=False)
            help.add_field(name='ᅠ\n***Экономика***', value=f'ᅠ\n**.balance** (пользователь) *- узнать баланс '
                                                             f'пользователя.*\nᅠ'
                                                       f'ᅠ\n**.pay** (сумма) (пользователь) *- перечислить пользователю'
                                                       f' сумму денег.*\nᅠ'
                                                       f'ᅠ\n**.case** *- **раз в сутки** можно открыть кейс, где '
                                                       f'может выпасть от **0** до **100$**.*\nᅠ'
                                                       f'ᅠ\n**.mr** *- вы получаете денежную роль.*\nᅠ'
                                                       f'ᅠ\n*Если ваш баланс:*\n**1000$ и больше:** {rabot.mention}\n'
                                                       f'**10000$ и больше:** {obecp.mention}\n'
                                                       f'**100000$ и больше:** {bogat.mention}\n'
                                                       f'**1000000$ и больше:** {mil.mention}\n'
                                                       f'**10000000$ и больше:** {sheih.mention}\n', inline=False)
            help.add_field(name='ᅠ\n***Мини-игры***', value=f'ᅠ\n**.rb** (сумма) (цвет) *- игра '
                                                            f'**"Красное и чёрное"**.*'
                                                             f'\nᅠ'
                                                       f'ᅠ\n**.coin** (сумма) (цвет) *- игра **"Орёл и решка"**.*',
                           inline=False)
            await ctx.message.delete()
            await ctx.send(embed=help)

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = str(message.channel.name)
        if channel == '📝предложения':
            await message.add_reaction('👍')
            await message.add_reaction('👎')

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.command(pass_context=True)
    @commands.has_any_role(853028950288760834)
    async def custom_roles(self, ctx):
        role_male = discord.utils.get(ctx.guild.roles, name="♂")
        role_female = discord.utils.get(ctx.guild.roles, name="♀")
        roles = discord.Embed(
            title='```Серверные роли```',
            description=f'***{role_male.mention} - роль для пользователей мужского пола.***\n***{role_female.mention} '
                        f'- роль для пользователей женского пола.***',
            color=0x8A2BE2
        )
        await ctx.message.delete()
        msg = await ctx.send(embed=roles)
        await msg.add_reaction('♀')
        await msg.add_reaction('♂')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message = 996866690476417135
        if message == payload.message_id:
            member = payload.member
            guild = member.guild
            emoji = payload.emoji.name
            if emoji == '♂':
                role = discord.utils.get(guild.roles, name="♂")
                role_del = discord.utils.get(guild.roles, name="♀")
                channel = self.bot.get_channel(payload.channel_id)
                msg = await channel.fetch_message(payload.message_id)
                await msg.remove_reaction('♀', member)
            if emoji == '♀':
                role = discord.utils.get(guild.roles, name="♀")
                role_del = discord.utils.get(guild.roles, name="♂")
                channel = self.bot.get_channel(payload.channel_id)
                msg = await channel.fetch_message(payload.message_id)
                await msg.remove_reaction('♂', member)
            await member.add_roles(role)
            await member.remove_roles(role_del)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message = 996866690476417135
        if message == payload.message_id:
            guild = await self.bot.fetch_guild(payload.guild_id)
            emoji = payload.emoji.name
            if emoji == '♂':
                role = discord.utils.get(guild.roles, name="♂")
            if emoji == '♀':
                role = discord.utils.get(guild.roles, name="♀")
            member = await guild.fetch_member(payload.user_id)
            if member is not None:
                await member.remove_roles(role)
            else:
                print('Пользователь не найден!')


# ---------------------------------------------------------------------------------------------------------------------#


def setup(bot):
    bot.add_cog(Users(bot))

# ---------------------------------------------------------------------------------------------------------------------#

# ОБНОВИТЬ!
# 5 строка: создадим class под названием Test. Он будет унаследован от commands.Cog
# 6 строка: создадим функцию __int__, передадим в неё self и bot (это позволяет ссылаться на основной файл).
# 7 строка: эта часть позволит ссылаться на bot, который мы ранее создали.
# 10-11 строка: создадим функцию настройки, которая позволит подключить ког к нашему боту.
# 9-11 строка: создадим функцию для проверки кога.
# 23-25 строка: повтор сообщения пользователя через префикс и reply. Пример: Ввод: .reply hi, Вывод: hi.
# 37-38 строка: в декораторе @commands.command() пишем асинхронную функцию и передаём в неё self и контекст.
# 39 строка: создаём эмбед.
# 40 строка: Название
# 41 строка: Описание
# 42 строка: Цвет рамки эмбеда (в данном случае указан цвет роли автора сообщение, но можно выбрать любой цвет).
# 45 строка: Верхнее поле эмбеда (можно указать автора или какой-либо текст).
# 45 строка: Параметры: name - имя автора, icon_url - иконка автора, url - ссылка на автора.
# 46 строка: Маленькое изображение сбоку.
# 46 строка: Параметры: url - ссылка на изображение (в данном случае аватарка сервера)
# 47-49 строка: Добавление поля в эмбед.
# 47-49 строка: Параметры: name - название поля, value - значение поля, inline=True/False - поля в строчку/столбик.
# 50 строка: Ссылка на изображение. Параметры: url - ссылка на изображение.
# 51 строка: Нижнее поле эмбеда (нельзя передавать ссылку).
# 51 строка: Параметры: text - текст нижнего поля, icon_url - иконка нижнего поля.
# 52 строка: Вывод эмбеда по команде (вывод сообщения в канал, где написана команда).
# ЗАПОМНИТЬ, что в когах:
# @bot.command() = @commands.command()
# @bot.event() = @commands.Cog.listener()

# * берёт текст причины полностью. Без * причина только 1-ое слово.
# @commands.has_permissions(ban_members=True) с этой командой соседнюю команду могут писать только те, кто может банить.

# ---------------------------------------------------------------------------------------------------------------------#
