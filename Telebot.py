# from telegram import Update
# from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#          await update.message.reply_text('Hi! I am your bot.')

# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#          await update.message.reply_text(update.message.text)

# def main() -> None:
#          application = Application.builder().token('7354187331:AAFr3KsvLouDqOMlGkMEQuGeTtofPWha5VE').build()

#          application.add_handler(CommandHandler("start", start))
#          application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

#          application.run_polling()

# if __name__ == '__main__':
#          main()


# program 2
# from pyrogram import Client, filters

# # Step 1: Define your bot's configuration
# api_id = "20201694"
# api_hash = "383cdc7a9c6967d056fbcab8b3271c43"
# bot_token = "7354187331:AAFr3KsvLouDqOMlGkMEQuGeTtofPWha5VE"

# # Step 2: Initialize the bot client
# app = Client(
#     "my_bot",
#     api_id=api_id,
#     api_hash=api_hash,
#     bot_token=bot_token
# )

# # Step 3: Define command handlers

# # /start command handler
# @app.on_message(filters.command("start"))
# def start_command(client, message):
#     message.reply_text("Hello! I'm your bot. How can I assist you today?")

# # /help command handler
# @app.on_message(filters.command("help"))
# def help_command(client, message):
#     message.reply_text(
#         "Here are the available commands:\n"
#         "/start - Start the bot\n"
#         "/help - Get help information\n"
#         "/echo - Echo the message back to you"
#     )

# # /echo command handler
# @app.on_message(filters.command("echo"))
# def echo_command(client, message):
#     # Get the text after the /echo command
#     text_to_echo = message.text.split(" ", 1)
    
#     if len(text_to_echo) > 1:
#         message.reply_text(text_to_echo[1])
#     else:
#         message.reply_text("Please provide a message to echo.")

# # Default handler for any other text message
# @app.on_message(filters.text & ~filters.command)
# def text_message_handler(client, message):
#     message.reply_text("You said: " + message.text)

# # Step 4: Run the bot
# if __name__ == "__main__":
#     print("Bot is running...")
#     app.run()




# program3
# from pyrogram import Client, filters

# # Step 1: Define your bot's configuration
# api_id = "20201694"
# api_hash = "383cdc7a9c6967d056fbcab8b3271c43"
# bot_token = "7354187331:AAFr3KsvLouDqOMlGkMEQuGeTtofPWha5VE"

# Step 2: Initialize the bot client
# app = Client(
#     "my_bot",
#     api_id=api_id,
#     api_hash=api_hash,
#     bot_token=bot_token
# )

# Step 3: Define command handlers

# /start command handler
# @app.on_message(filters.command("start"))
# def start_command(client, message):
#     message.reply_text("Hello! I'm your bot. How can I assist you today?")

# @app.on_message(filters.command("start"))
# def start_command(client, message):
#     message.reply_text(
#         "Hello!! How can I assist you today?"
#         # parse_mode="Markdown"  # Correct capitalization for Markdown
#     )



# /help command handler
# @app.on_message(filters.command("help"))
# def help_command(client, message):
#     message.reply_text(
#         "Here are the available commands:\n"
#         "/start - Start the bot\n"
#         "/help - Get help information\n"
#         "/echo - Echo the message back to you\n"
#         "/visionimpact - Visit [Vision Impact](https://www.visionimpact.ai) for more info.\n" 
#         "/smart - Visit [Smart](https://honeydew-goldfinch-962912.builder-preview.com/) for more info.\n "
#         "/master - Visit [Master](https://pink-dugong-788341.builder-preview.com/) for more info.\n"
#         "/events - Visit [Events](https://gamma.app/docs/Melody-Moments-Personalized-Event-Harmony-px453jnio3nxg1t?mode=doc) for more info.\n"
#         "/instaskills - Visit [InstaSkills](https://drive.google.com/file/d/1O9dfFCsG1613-W2dHBlOIxgMEMcB3eie/view?pli=1) for more info.\n"
#         "/calendly - Visit [Calendly](https://calendly.com/event_types/user/me) for more info.\n"
#         "/linktree - Visit [LinkTree](https://linktr.ee/visionimpacttech) for more info.\n"
#         "/contact - Visit [visionimpactcontact](https://www.google.com/maps/place/Vision+Impact/@12.968289,77.519199,15z/data=!4m6!3m5!1s0x3bae3d25565e0617:0x98d8394031e828fb!8m2!3d12.968289!4d77.519199!16s%2Fg%2F11v_0932wy?entry=ttu) for more info.\n"
    # )

# /echo command handler
# @app.on_message(filters.command("echo"))
# def echo_command(client, message):
#     # Get the text after the /echo command
#     text_to_echo = message.text.split(" ", 1)
    
#     if len(text_to_echo) > 1:
#         message.reply_text(text_to_echo[1])
#     else:
#         message.reply_text("Please provide a message to echo.")

# /vision command handler
# @app.on_message(filters.command("visionimpact"))
# def vision_command(client, message):
#     message.reply_text(
#         """Vision Impact is a dynamic, tech-driven startup that blends advanced AI technology with creative storytelling to revolutionize digital experiences. The company is an arm of Impactful Visionaries LLP and aims to redefine how stories are told, businesses grow, and skills are developed in the digital age...
#         (Visit [Vision Impact](https://www.visionimpact.ai) for more info.)
#         """
#     )



# /smart channel command handler
# @app.on_message(filters.command("smartchannel"))
# def vision_command(client, message):
#     message.reply_text(
#         """The Smart Channel Partner program by Vision Impact enables individuals or businesses to earn commissions by promoting AI-powered services and digital solutions, with full support and minimal investment required. It offers a low-risk entry into the digital marketing and AI space, ideal for those seeking passive income opportunities....
#         (Visit [Smart Channel](https://honeydew-goldfinch-962912.builder-preview.com/) for more info.)
#         """
#     )


# /master channel command handler
# @app.on_message(filters.command("master"))
# def vision_command(client, message):
#     message.reply_text(
#         """The Master Channel Partner program allows individuals or businesses to sell Vision Impact's services under their own brand, with the opportunity to set premium prices and earn higher commissions. This program provides comprehensive support, including training, marketing materials, and a dedicated website for managing services and client interactions​​...
#         (Visit [Master Channel](https://pink-dugong-788341.builder-preview.com/) for more info.)
#         """
#     ) 



# /events channel command handler
# @app.on_message(filters.command("events"))
# def vision_command(client, message):
#     message.reply_text(
#         """Vision Impact hosts exclusive events, including networking opportunities, advanced workshops, and collaborative sessions, designed to empower participants with cutting-edge AI and digital storytelling skills. These events provide unique platforms for learning, innovation, and growth within a vibrant community of industry leaders and creative professionals...
#         (Visit [Events](https://gamma.app/docs/Melody-Moments-Personalized-Event-Harmony-px453jnio3nxg1t?mode=doc) for more info.)
#         """
#     ) 



 # /instaskills channel command handler
# @app.on_message(filters.command("instaskills"))
# def vision_command(client, message):
#     message.reply_text(
#         """InstaSkills offers short, impactful courses focused on rapidly acquiring digital and AI skills, tailored to meet the immediate needs of learners in a fast-paced technological environment. These courses are designed for accessibility, allowing anyone to quickly enhance their skill set and stay competitive in the digital age....
#         (Visit [InstaSkills](https://drive.google.com/file/d/1O9dfFCsG1613-W2dHBlOIxgMEMcB3eie/view?pli=1) for more info.)
#         """
#     ) 



 # /calendly channel command handler
# @app.on_message(filters.command("calendly"))
# def vision_command(client, message):
#     message.reply_text(
#         """Vision Impact uses Calendly to streamline the booking process for discovery calls, allowing clients and partners to easily schedule meetings at their convenience. This tool ensures efficient communication and seamless coordination for all interactions...
#         (Visit [Calendly](https://calendly.com/event_types/user/me) for more info.)
#         """
#     ) 



 # /linktree channel command handler
# @app.on_message(filters.command("linktree"))
# def vision_command(client, message):
#     message.reply_text(
#         """Linktree is a user-friendly platform that allows you to create a single link containing multiple links to your social profiles, websites, and other online content, making it easy to share all your online presence with just one URL. It's an efficient way to centralize and simplify access to your most important links...
#         (Visit [LinkTree](https://linktr.ee/visionimpacttech) for more info.)
#         """
#     ) 


 # /contact channel command handler
# @app.on_message(filters.command("contact"))
# def vision_command(client, message):
#     message.reply_text(
#         "[Address:](https://www.google.com/maps/place/Vision+Impact/@12.968289,77.519199,15z/data=!4m6!3m5!1s0x3bae3d25565e0617:0x98d8394031e828fb!8m2!3d12.968289!4d77.519199!16s%2Fg%2F11v_0932wy?entry=ttu) #338, 6th Cross, 3rd Main, 2nd Block,1st Stage, Kalyananagara, Nagarabhavi, Bangalore - 560072.\n"
#         "Email: content@visionimpact.ai, visionimpacttechnologies@gmail.com\n"
#         "Phone: +91 9606989902\n"
      
#     ) 



# # Default handler for any other text message
# @app.on_message(filters.text & ~filters.command(None))
# def text_message_handler(client, message):
#     message.reply_text("You said: " + message.text)


# Default handler for any other text message
# @app.on_message(filters.text)
# def text_message_handler(client, message):
#     message.reply_text("You said: " + message.text)

# # Step 4: Run the bot
# if __name__ == "__main__":
#     print("Bot is running...")
#     app.run()


# program 4

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Step 1: Define your bot's configuration
api_id = "20201694"
api_hash = "383cdc7a9c6967d056fbcab8b3271c43"
bot_token = "7354187331:AAFr3KsvLouDqOMlGkMEQuGeTtofPWha5VE"

# Step 2: Initialize the bot client
app = Client(
    "my_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

# Function to generate the inline keyboard menu
def get_menu_keyboard():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Vision Impact", callback_data="visionimpact"),
                InlineKeyboardButton("Smart", callback_data="smart"),
                InlineKeyboardButton("Master", callback_data="master"),
                InlineKeyboardButton("Events", callback_data="events"),
            ],
            [
                InlineKeyboardButton("InstaSkills", callback_data="instaskills"),
                InlineKeyboardButton("Calendly", callback_data="calendly"),
                InlineKeyboardButton("LinkTree", callback_data="linktree"),
                InlineKeyboardButton("Contact", callback_data="contact"),
            ]
        ]
    )

# /start command handler with an inline keyboard menu
@app.on_message(filters.command("start"))
def start_command(client, message):
    message.reply_text(
        "Hello!! The Vision Impact Bot is an AI-driven tool designed to educate and assist the User's by explaining the company’s services, innovations and particularly in AI-powered visual content creation and digital transformation. For more info...\n Choose an option from the menu below:",
        reply_markup=get_menu_keyboard()
    )

# Handle the callbacks from the inline keyboard
# @app.on_callback_query()
# def handle_callback_query(client, callback_query):
#     data = callback_query.data
    
#     if data == "visionimpact":
#         callback_query.message.edit_text(
#             "Vision Impact is a dynamic, tech-driven startup that blends advanced AI technology with creative storytelling to revolutionize digital experiences. Visit [Vision Impact](https://www.visionimpact.ai) for more info.",
#             reply_markup=get_menu_keyboard()
#         )
#     elif data == "smart":
#         callback_query.message.edit_text(
#             "The Smart Channel Partner program by Vision Impact enables individuals or businesses to earn commissions by promoting AI-powered services and digital solutions. Visit [Smart Channel](https://honeydew-goldfinch-962912.builder-preview.com/) for more info.",
#             reply_markup=get_menu_keyboard()
#         )
#     elif data == "master":
#         callback_query.message.edit_text(
#             "The Master Channel Partner program allows individuals or businesses to sell Vision Impact's services under their own brand. Visit [Master Channel](https://pink-dugong-788341.builder-preview.com/) for more info.",
#             reply_markup=get_menu_keyboard()
#         )
#     elif data == "events":
#         callback_query.message.edit_text(
#             "Vision Impact hosts exclusive events, including networking opportunities, advanced workshops, and collaborative sessions. Visit [Events](https://gamma.app/docs/Melody-Moments-Personalized-Event-Harmony-px453jnio3nxg1t?mode=doc) for more info.",
#             reply_markup=get_menu_keyboard()
#         )
#     elif data == "instaskills":
#         callback_query.message.edit_text(
#             "InstaSkills offers short, impactful courses focused on rapidly acquiring digital and AI skills. Visit [InstaSkills](https://gamma.app/docs/InstaSkills-Program-by--3e4p5y2ytrh3e8k?mode=doc) for more info.",
#             reply_markup=get_menu_keyboard()
#         )
#     elif data == "calendly":
#         callback_query.message.edit_text(
#             "Vision Impact uses Calendly to streamline the booking process for discovery calls. Visit [Calendly](https://calendly.com/visionimpacttechnologies/30min?back=1&month=2024-08) for more info.",
#             reply_markup=get_menu_keyboard()
#         )
#     elif data == "linktree":
#         callback_query.message.edit_text(
#             "Linktree is a user-friendly platform that allows you to create a single link containing multiple links to your social profiles. Visit [LinkTree](https://linktr.ee/visionimpacttech) for more info.",
#             reply_markup=get_menu_keyboard()
#         )
#     elif data == "contact":
#         callback_query.message.edit_text(
#             "Address: #338, 6th Cross, 3rd Main, 2nd Block, 1st Stage, Kalyananagara, Nagarabhavi, Bangalore - 560072.\n"
#             "Email: content@visionimpact.ai, visionimpacttechnologies@gmail.com\n"
#             "Phone: +91 9606989902\n"
#             "Visit [Google Maps](https://www.google.com/maps/place/Vision+Impact/@12.968289,77.519199,15z/data=!4m6!3m5!1s0x3bae3d25565e0617:0x98d8394031e828fb!8m2!3d12.968289!4d77.519199!16s%2Fg%2F11v_0932wy?entry=ttu) for the location.",
#             reply_markup=get_menu_keyboard()
#         )

@app.on_callback_query()
def handle_callback_query(client, callback_query):
    data = callback_query.data

    # Define a dictionary with all your callback data and corresponding messages
    responses = {
        "visionimpact": "Vision Impact is a dynamic, tech-driven startup that blends advanced AI technology with creative storytelling to revolutionize digital experiences. Visit [Vision Impact](https://www.visionimpact.ai) for more info.",
        "smart": "The Smart Channel Partner program by Vision Impact enables individuals or businesses to earn commissions by promoting AI-powered services and digital solutions. Visit [Smart Channel](https://honeydew-goldfinch-962912.builder-preview.com/) for more info.",
        "master": "The Master Channel Partner program allows individuals or businesses to sell Vision Impact's services under their own brand. Visit [Master Channel](https://pink-dugong-788341.builder-preview.com/) for more info.",
        "events": "Vision Impact hosts exclusive events, including networking opportunities, advanced workshops, and collaborative sessions. Visit [Events](https://gamma.app/docs/Melody-Moments-Personalized-Event-Harmony-px453jnio3nxg1t?mode=doc) for more info.",
        "instaskills": "InstaSkills offers short, impactful courses focused on rapidly acquiring digital and AI skills. Visit [InstaSkills](https://gamma.app/docs/InstaSkills-Program-by--3e4p5y2ytrh3e8k?mode=doc) for more info.",
        "calendly": "Vision Impact uses Calendly to streamline the booking process for discovery calls. Visit [Calendly](https://calendly.com/visionimpacttechnologies/30min?back=1&month=2024-08) for more info.",
        "linktree": "Linktree is a user-friendly platform that allows you to create a single link containing multiple links to your social profiles. Visit [LinkTree](https://linktr.ee/visionimpacttech) for more info.",
        "contact": "Address: #338, 6th Cross, 3rd Main, 2nd Block, 1st Stage, Kalyananagara, Nagarabhavi, Bangalore - 560072.\n"
                   "Email: content@visionimpact.ai, visionimpacttechnologies@gmail.com\n"
                   "Phone: +91 9606989902\n"
                   "Visit [Google Maps](https://www.google.com/maps/place/Vision+Impact/@12.968289,77.519199,15z/data=!4m6!3m5!1s0x3bae3d25565e0617:0x98d8394031e828fb!8m2!3d12.968289!4d77.519199!16s%2Fg%2F11v_0932wy?entry=ttu) for the location."
    }

    # Get the new content based on the callback data
    new_text = responses.get(data, "")

    # Only edit the message if the new content is different from the current content
    if callback_query.message.text != new_text:
        callback_query.message.edit_text(new_text, reply_markup=get_menu_keyboard())
    else:
        print("Message not modified because the content is the same.")


# /help command handler
@app.on_message(filters.command("help"))
def help_command(client, message):
    message.reply_text(
        "Here are the available commands:\n"
        "/start - Start the bot\n"
        "/help - Get help information\n"
        "/echo - Echo the message back to you\n"
        "/visionimpact - Visit [Vision Impact](https://www.visionimpact.ai) for more info.\n" 
        "/smart - Visit [Smart](https://honeydew-goldfinch-962912.builder-preview.com/) for more info.\n "
        "/master - Visit [Master](https://pink-dugong-788341.builder-preview.com/) for more info.\n"
        "/events - Visit [Events](https://gamma.app/docs/Melody-Moments-Personalized-Event-Harmony-px453jnio3nxg1t?mode=doc) for more info.\n"
        "/instaskills - Visit [InstaSkills](https://gamma.app/docs/InstaSkills-Program-by--3e4p5y2ytrh3e8k?mode=doc) for more info.\n"
        "/calendly - Visit [Calendly](https://calendly.com/visionimpacttechnologies/30min?back=1&month=2024-08) for more info.\n"
        "/linktree - Visit [LinkTree](https://linktr.ee/visionimpacttech) for more info.\n"
        "/contact - Visit [visionimpactcontact](https://www.google.com/maps/place/Vision+Impact/@12.968289,77.519199,15z/data=!4m6!3m5!1s0x3bae3d25565e0617:0x98d8394031e828fb!8m2!3d12.968289!4d77.519199!16s%2Fg%2F11v_0932wy?entry=ttu) for more info.\n"
    )

# /echo command handler
@app.on_message(filters.command("echo"))
def echo_command(client, message):
    text_to_echo = message.text.split(" ", 1)
    if len(text_to_echo) > 1:
        message.reply_text(text_to_echo[1])
    else:
        message.reply_text("Please provide a message to echo.")

# Default handler for any other text message
@app.on_message(filters.text)
def text_message_handler(client, message):
    message.reply_text("You said: " + message.text)

# Step 4: Run the bot
if __name__ == "__main__":
    print("Bot is running...")
    app.run()
