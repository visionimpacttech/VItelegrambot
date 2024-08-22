const TelegramBot = require('node-telegram-bot-api');

// Step 1: Define your bot's configuration
const api_id = "20201694";
const api_hash = "383cdc7a9c6967d056fbcab8b3271c43";
const bot_token = "7354187331:AAFr3KsvLouDqOMlGkMEQuGeTtofPWha5VE";

// Step 2: Initialize the bot client
const bot = new TelegramBot(bot_token, { polling: true });

// Function to generate the inline keyboard menu
function getMenuKeyboard() {
    return {
        reply_markup: {
            inline_keyboard: [
                [
                    { text: "Vision Impact", callback_data: "visionimpact" },
                    { text: "Smart", callback_data: "smart" },
                    { text: "Master", callback_data: "master" },
                    { text: "Events", callback_data: "events" }
                ],
                [
                    { text: "InstaSkills", callback_data: "instaskills" },
                    { text: "Calendly", callback_data: "calendly" },
                    { text: "LinkTree", callback_data: "linktree" },
                    { text: "Contact", callback_data: "contact" }
                ]
            ]
        }
    };
}

// /start command handler with an inline keyboard menu
bot.onText(/\/start/, (msg) => {
    const chatId = msg.chat.id;
    bot.sendMessage(
        chatId,
        "Hello!! The Vision Impact Bot is an AI-driven tool designed to educate and assist the User's by explaining the company’s services, innovations and particularly in AI-powered visual content creation and digital transformation. For more info...\n Choose an option from the menu below:",
        getMenuKeyboard()
    );
});

// Handle the callbacks from the inline keyboard
bot.on('callback_query', (callbackQuery) => {
    const msg = callbackQuery.message;
    const data = callbackQuery.data;

    let responseText = '';

    if (data === "visionimpact") {
        responseText = "Vision Impact is a dynamic, tech-driven startup that blends advanced AI technology with creative storytelling to revolutionize digital experiences. Visit [Vision Impact](https://www.visionimpact.ai) for more info.";
    } else if (data === "smart") {
        responseText = "The Smart Channel Partner program by Vision Impact enables individuals or businesses to earn commissions by promoting AI-powered services and digital solutions. Visit [Smart Channel](https://honeydew-goldfinch-962912.builder-preview.com/) for more info.";
    } else if (data === "master") {
        responseText = "The Master Channel Partner program allows individuals or businesses to sell Vision Impact's services under their own brand. Visit [Master Channel](https://pink-dugong-788341.builder-preview.com/) for more info.";
    } else if (data === "events") {
        responseText = "Vision Impact hosts exclusive events, including networking opportunities, advanced workshops, and collaborative sessions. Visit [Events](https://gamma.app/docs/Melody-Moments-Personalized-Event-Harmony-px453jnio3nxg1t?mode=doc) for more info.";
    } else if (data === "instaskills") {
        responseText = "InstaSkills offers short, impactful courses focused on rapidly acquiring digital and AI skills. Visit [InstaSkills](https://gamma.app/docs/InstaSkills-Program-by--3e4p5y2ytrh3e8k?mode=doc) for more info.";
    } else if (data === "calendly") {
        responseText = "Vision Impact uses Calendly to streamline the booking process for discovery calls. Visit [Calendly](https://calendly.com/visionimpacttechnologies/30min?back=1&month=2024-08) for more info.";
    } else if (data === "linktree") {
        responseText = "Linktree is a user-friendly platform that allows you to create a single link containing multiple links to your social profiles. Visit [LinkTree](https://linktr.ee/visionimpacttech) for more info.";
    } else if (data === "contact") {
        responseText = "Address: #338, 6th Cross, 3rd Main, 2nd Block, 1st Stage, Kalyananagara, Nagarabhavi, Bangalore - 560072.\nEmail: content@visionimpact.ai, visionimpacttechnologies@gmail.com\nPhone: +91 9606989902\nVisit [Google Maps](https://www.google.com/maps/place/Vision+Impact/@12.968289,77.519199,15z/data=!4m6!3m5!1s0x3bae3d25565e0617:0x98d8394031e828fb!8m2!3d12.968289!4d77.519199!16s%2Fg%2F11v_0932wy?entry=ttu) for the location.";
    }

    bot.sendMessage(msg.chat.id, responseText, getMenuKeyboard());
});

// /help command handler
bot.onText(/\/help/, (msg) => {
    const chatId = msg.chat.id;
    bot.sendMessage(
        chatId,
        "Here are the available commands:\n" +
        "/start - Start the bot\n" +
        "/help - Get help information\n" +
        "/echo - Echo the message back to you\n" +
        "/visionimpact - Visit [Vision Impact](https://www.visionimpact.ai) for more info.\n" +
        "/smart - Visit [Smart](https://honeydew-goldfinch-962912.builder-preview.com/) for more info.\n" +
        "/master - Visit [Master](https://pink-dugong-788341.builder-preview.com/) for more info.\n" +
        "/events - Visit [Events](https://gamma.app/docs/Melody-Moments-Personalized-Event-Harmony-px453jnio3nxg1t?mode=doc) for more info.\n" +
        "/instaskills - Visit [InstaSkills](https://gamma.app/docs/InstaSkills-Program-by--3e4p5y2ytrh3e8k?mode=doc) for more info.\n" +
        "/calendly - Visit [Calendly](https://calendly.com/visionimpacttechnologies/30min?back=1&month=2024-08) for more info.\n" +
        "/linktree - Visit [LinkTree](https://linktr.ee/visionimpacttech) for more info.\n" +
        "/contact - Visit [Google Maps](https://www.google.com/maps/place/Vision+Impact/@12.968289,77.519199,15z/data=!4m6!3m5!1s0x3bae3d25565e0617:0x98d8394031e828fb!8m2!3d12.968289!4d77.519199!16s%2Fg%2F11v_0932wy?entry=ttu) for more info."
    );
});

// /echo command handler
bot.onText(/\/echo (.+)/, (msg, match) => {
    const chatId = msg.chat.id;
    const resp = match[1]; // the captured "echo" message
    bot.sendMessage(chatId, resp);
});

// Default handler for any other text message
bot.on('message', (msg) => {
    const chatId = msg.chat.id;
    if (!msg.text.startsWith('/')) {
        bot.sendMessage(chatId, "You said: " + msg.text);
    }
});

// Step 4: Run the bot
console.log("Bot is running...");
