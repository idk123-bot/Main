# Bot/Utilities/AI_Chat.py
from Utils.Logger import setup_logging
import requests

logging = setup_logging()

# Store conversations per user
conversations = {}


def setup(bot):
    @bot.command(name="ask", aliases=["Ask", "ASK"])
    async def ask(ctx, *, msg):
        if not msg:
            await ctx.send("❌ Ask me something! Example: `!ask What is Python?`")
            return

        user_id = ctx.author.id

        # Get or create user's history
        if user_id not in conversations:
            conversations[user_id] = []

        # Add user's message
        conversations[user_id].append({"role": "user", "content": msg})

        try:
            response = requests.post(
                "https://text.pollinations.ai/",
                json={"messages": conversations[user_id]},
            )
            ai_reply = response.text

            # Save AI response
            conversations[user_id].append({"role": "assistant", "content": ai_reply})

            # Trim if too long
            if len(ai_reply) > 1900:
                ai_reply = ai_reply[:1900] + "..."

            await ctx.send(ai_reply)
            logging.info(f"{ctx.author} asked ai: {msg}")

        except Exception as e:
            await ctx.send("Couldn't fetch AI API, Please contact the owner!")
            logging.error(f"Couldn't fetch AI API {e}")

    @bot.command(name="forget", aliases=["Forget", "FORGET"])
    async def forget(ctx):
        """Clear your conversation history."""
        user_id = ctx.author.id
        if user_id in conversations:
            conversations[user_id] = []
        await ctx.send("🧹 Conversation history cleared!")
