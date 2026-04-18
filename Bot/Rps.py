# Bot_games/rps.py
import random
import asyncio
from Utils.Logger import setup_logging

logging = setup_logging()


def setup(bot):
    @bot.command(name="rps")
    async def rps(ctx):
        """Rock Paper Scissors - First to 3 points wins!"""
        logging.info(f"RPS game started by: {ctx.author}")

        choices = ["rock", "paper", "scissors"]
        player_score = 0
        computer_score = 0

        await ctx.send("🎮 **Rock Paper Scissors** - First to 3 wins!")
        await ctx.send("Type `rock`, `paper`, or `scissors`. Type `quit` to stop.")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        while player_score < 3 and computer_score < 3:
            await ctx.send(
                f"\n🏆 Score: You **{player_score}** | Computer **{computer_score}**"
            )
            await ctx.send("Your choice:")

            try:
                msg = await bot.wait_for("message", timeout=30.0, check=check)
                choice = msg.content.lower()

                if choice == "quit":
                    await ctx.send("👋 Game cancelled!")
                    return

                if choice not in choices:
                    await ctx.send("❌ Invalid! Choose: `rock`, `paper`, or `scissors`")
                    continue

                computer = random.choice(choices)
                await ctx.send(f"🤖 Computer chose: **{computer}**")

                if choice == computer:
                    await ctx.send("😐 Tie!")
                elif (
                    (choice == "rock" and computer == "scissors")
                    or (choice == "paper" and computer == "rock")
                    or (choice == "scissors" and computer == "paper")
                ):
                    await ctx.send("✅ You win this round!")
                    player_score += 1
                else:
                    await ctx.send("❌ Computer wins this round!")
                    computer_score += 1

                await asyncio.sleep(1)

            except asyncio.TimeoutError:
                await ctx.send("⏰ Time's up! Game cancelled.")
                return

        # Game over
        if player_score == 3:
            await ctx.send(
                f"\n🎉🎉🎉 **YOU WIN THE GAME!** {player_score}-{computer_score} 🎉🎉🎉"
            )
        else:
            await ctx.send(
                f"\n💻 **COMPUTER WINS!** {computer_score}-{player_score} 💻"
            )

        logging.info(
            f"RPS game ended: {ctx.author} - Final score {player_score}-{computer_score}"
        )

        # Ask to play again
        await ctx.send("\nPlay again? (yes/no)")
        try:
            msg = await bot.wait_for("message", timeout=30.0, check=check)
            if msg.content.lower() in ["yes", "y"]:
                await rps(ctx)  # Restart
            else:
                await ctx.send("Thanks for playing!")
        except asyncio.TimeoutError:
            await ctx.send("Thanks for playing!")
