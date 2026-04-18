# Bot_games/calculator.py
from Utils.Logger import setup_logging

logging = setup_logging()


def setup(bot):
    @bot.command(name="calc")
    async def calc(ctx, num1, op, num2):
        logging.info(f"Calc by {ctx.author}: {num1} {op} {num2}")

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            await ctx.send("❌ Please provide valid numbers!")
            return

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op in ["x", "*"]:
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                await ctx.send("❌ Can't divide by zero!")
                return
            result = num1 / num2
        else:
            await ctx.send("❌ Invalid operator!")
            return

        await ctx.send(f"🧮 The answer is: {result}")
