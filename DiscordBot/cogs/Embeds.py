from discord.ext import commands
import discord  # импортируем библиотеку discord.


class Embeds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def embed_info(self, ctx):
        embed_info = discord.Embed(
            title='Добро пожаловать на сервер Lounge zone!',
            description=' ᅠ\nПозволь нам провести небольшую экскурсию.\n ᅠ',
            color=0x8A2BE2

        )
        embed_info.set_thumbnail(url='https://c.tenor.com/YxpnJdn7aKoAAAAM/stargaze-anime.gif')
        embed_info.add_field(name='Раздел инфо:', value='ᅠ\n<#879492097189765180> - канал с основной информацией о '
                                                        'сервере.\n '
                                                        'ᅠ\n<#879492182694842378> - канал, в котором перечислены все '
                                                        'правила '
                                                        'нашего сервера.\n '
                                                        '\n<#880033184488771604> - канал, в котором будут '
                                                        'выкладываться '
                                                        'свежие новости сервера.\n '
                                                        '\n<#879651435778834462> - канал, в котором вы можете оставить '
                                                        'свои предложения для развития нашего сервера.', inline=False)
        embed_info.add_field(name=' ᅠ\nРаздел разное:', value='ᅠ\n<#901186399997403166> - канал, в котором вы сможете '
                                                              'ввести доступные вам команды сервера. Чтобы узнать '
                                                              'список команд, необходимо в этом же канале ввести '
                                                              'команду: **.help**\n '
                                                              'ᅠ\n<#941035624415252580> - основной текстовый канал, '
                                                              'в котором вы можете общаться с участниками сервера.\n '
                                                              'ᅠ\n<#879755307423793173> - канал, в котором вы можете '
                                                              'выкладывать свои шедевры искусства.\n '
                                                              'ᅠ\n<#879769305758191686> - канал, в котором вы можете '
                                                              'заказать любую музыку у музыкального бота. Для '
                                                              'прослушивания музыки можно перейти в голосовой канал '
                                                              '<#879730576800747551>.', inline=False)
        embed_info.add_field(name=' ᅠ\nПо всем вопросам писать:', value='<@&879514110927208448> '
                                                                        '<@&879514829566644324>', inline=False)
        embed_info.set_image(url='https://c.tenor.com/AAqButx49DIAAAAC/i-need-you.gif')
        await ctx.message.delete()
        await ctx.send(embed=embed_info)

# ---------------------------------------------------------------------------------------------------------------------#

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def embed_rules(self, ctx):
        embed_rules = discord.Embed(
            title='Правила Lounge zone:',
            description=' ᅠ\nНесоблюдение правил приведёт к Mute или бану.\n ᅠ',
            color=0x8A2BE2

        )
        embed_rules.set_thumbnail(url='https://c.tenor.com/HkoXys8I_xEAAAAC/anime-tower-of-god.gif')
        embed_rules.add_field(name='Текстовые и голосовые чаты:', value='ᅠ\n1.1 Незнание правил не освобождает от '
                                                                   'ответственности.\n ᅠ '
                                                                   'ᅠ\n1.2 Запрещён флуд, спам и чрезмерное '
                                                                   'использование CAPS.\n ᅠ '
                                                                   'ᅠ\n1.3 Запрещены любые оскорбления, неадекватное '
                                                                   'поведение, угрозы, провокации и любые попытки '
                                                                   'препятствовать '
                                                                   'комфортному общению в чате/войсе.\n ᅠ'
                                                                   'ᅠ\n1.4 Запрещены нецензурные, оскорбительные, '
                                                                   'аморальные никнеймы и аватарки.\n ᅠ '
                                                                   'ᅠ\n1.5 Запрещены нацизм, расизм, сексизм.\n ᅠ'
                                                                   'ᅠ\n1.6 '
                                                                   'Запрещены межнациональные, политические и '
                                                                   'религиозные споры.\n ᅠ '
                                                                   'ᅠ\n1.7 Запрещена любая пропаганда и обсуждение '
                                                                   'наркотических веществ.\n ᅠ '
                                                                   'ᅠ\n1.8 Запрещено разглашение личной информации '
                                                                   'участника сервера без его разрешения.\n ᅠ '
                                                                   'ᅠ\n1.9 Запрещено выкладывать любой контент, '
                                                                   'который содержит сцены насилия, сцены интимного '
                                                                   'характера и прочий запрещённый и неадекватный '
                                                                   'контент.\n ᅠ '
                                                                   'ᅠ\n1.10 Запрещено попрошайничество и '
                                                                   'вымогательство.\n ᅠ '
                                                                   'ᅠ\n1.11 Запрещены спойлеры к играм, фильмам и '
                                                                   'сериалам.\nᅠ', inline=False)
        embed_rules.add_field(name='Серверные правила:\n ᅠ', value='2.1 Запрещено выдавать себя за Администрацию и '
                                                           'других участников сервера.\nᅠ'
                                                           'ᅠ\n2.2 Запрещена реклама сторонних серверов и ресурсов, '
                                                           'реклама услуг и товаров, зазывание в личные сообщение '
                                                           'участников сервера с целью прорекламировать что-либо '
                                                           'из вышесказанного.\nᅠ'
                                                           'ᅠ\n2.3 Запрещено осуждение действий Модерации. Каждое '
                                                           'действие со стороны Модерации происходит осознанно, и '
                                                           'Модераторы отвечают за то, что сделали. В частности, '
                                                           'указывая причину. Если вас не устраивает работа Модерации, '
                                                           'вы можете написать жалобу, которая будет '
                                                           'рассмотрена Администрацией.\nᅠ'
                                                           'ᅠ\n2.4 Запрещено публично обсуждать, игнорировать и '
                                                           'провоцировать модерацию сервера как в общих чатах на '
                                                           'сервере, так и в личных сообщениях.\nᅠ'
                                                           'ᅠ\n2.5 Запрещено подавать фейковые жалобы.\nᅠ'
                                                           'ᅠ\n2.6 Запрещён обман Администрации.\nᅠ'
                                                           'ᅠ\n2.7 Запрещено использование багов дискорда или '
                                                           'багов серверных ботов.\nᅠ', inline=False)
        embed_rules.add_field(name='Модерация:\n ᅠ', value='1. Модератор выносит решение по своему опыту, '
                                                           'основываясь на имеющихся правилах.\n '
                                                           'ᅠ\n2. За маленькие нарушения может быть выдано '
                                                           'предупреждение. При повторном нарушении выдаётся Mute. '
                                                           'Срок Mute определяет Модератор.\n '
                                                           'ᅠ\n3. В случае повторных нарушений могут быть применены '
                                                           'более строгие санкции, '
                                                           'вплоть до перманентного бана.\n ', inline=False)
        await ctx.message.delete()
        await ctx.send(embed=embed_rules)

# ---------------------------------------------------------------------------------------------------------------------#


def setup(bot):
    bot.add_cog(Embeds(bot))


# ---------------------------------------------------------------------------------------------------------------------#