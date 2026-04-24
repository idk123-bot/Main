# Bot/Utilities/Morse.py
from Utils.Logger import setup_logging
import asyncio

logging = setup_logging()


def setup(bot):
    @bot.command(name="morse", aliases=["Morse", "MORSE"])
    async def morse(ctx):
        logging.info(f"{ctx.author} used !morse command")

        MORSE_CODE = {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            "0": "-----",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            " ": "/",
        }

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            await ctx.send("What text do you want to translate to Morse code?")
            msg = await bot.wait_for("message", timeout=30.0, check=check)
            text = msg.content.upper()

            morse_text = []
            for char in text:
                if char in MORSE_CODE:
                    morse_text.append(MORSE_CODE[char])
                else:
                    morse_text.append(char)

            result = " ".join(morse_text)
            await ctx.send(f"📡 **Morse Code:**\n`{result}`")
            logging.info(f"Morse code generated for: {text}")

        except asyncio.TimeoutError:
            await ctx.send("⏰ Time's up! Cancelled.")
