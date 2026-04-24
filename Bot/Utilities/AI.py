# Bot/Utilities/AI_Chat.py
from Utils.Logger import setup_logging
import requests

logging = setup_logging()


def setup(bot):
    @bot.command(name="ask", aliases=["Ask", "ASK"])
    async def ask(ctx, *, msg):
        if not msg:
            await ctx.send("❌ Ask me something! Example: `!ask What is Python?`")
            return
        try:
            response = requests.post(
                "https://text.pollinations.ai/",
                json={"messages": [{"role": "user", "content": msg}]},
            )
            ai_reply = response.text

            # Trim if too long
            if len(ai_reply) > 1900:
                ai_reply = ai_reply[:1900] + "..."

            await ctx.send(ai_reply)
            logging.info(f"{ctx.author} asked ai: {msg}")
        except Exception as e:
            await ctx.send("Couldn't fetch AI API, Please contact the owner!")
            logging.error(f"Couldn't fetch AI API {e}")
