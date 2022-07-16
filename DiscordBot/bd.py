from discord.ext import commands
import json


def load_json(filename):
    with open(filename, encoding='latin-1') as infile:  # with open(filename, encoding='utf-8') as infile:
        return json.load(infile)


def write_json(filename, content):
    with open(filename, 'w') as outfile:
        json.dump(content, outfile, ensure_ascii=False, indent=4)


class Json(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# ---------------------------------------------------------------------------------------------------------------------#

    # Первый пример использования json.
    @commands.Cog.listener()
    async def on_message(self, message):
        msg = load_json("bd.json")
        msg["message"] = str(message.content)
        write_json("bd.json", msg)


# Второй пример использования json.
with open("bd.json", "r", encoding='latin-1') as f:
    num = json.load(f)
with open("bd.json", "w", encoding='latin-1') as f:
    num["numbers"] = 'one, two, three!'
    json.dump(num, f, indent=4, ensure_ascii=False)


# ---------------------------------------------------------------------------------------------------------------------#


def setup(bot):
    bot.add_cog(Json(bot))

# ---------------------------------------------------------------------------------------------------------------------#
