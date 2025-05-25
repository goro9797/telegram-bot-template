from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# ─── 여기에 네 토큰·관리자 ID를 그대로 넣어주세요 ───
BOT_TOKEN = '7786486975:AAGedIINrR2k53NRvyqewdEV-mSzso2a_E8'
ADMIN_ID  = 7327455864
# ──────────────────────────────────────────────────────

async def forward_to_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user     = update.message.from_user
    text     = update.message.text
    username = user.username or "(no username)"
    user_id  = user.id

    # 관리자에게 보낼 알림 메시지
    admin_msg = (
        f"📥 입장 요청 도착\n"
        f"👤 사용자: @{username}\n"
        f"🆔 ID: {user_id}\n"
        f"💬 메시지: {text}"
    )
    await context.bot.send_message(chat_id=ADMIN_ID, text=admin_msg)

    # 사용자에게 자동 답장
    await update.message.reply_text("입장 요청이 접수되었습니다! 잠시만 기다려주세요 😊")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    # 텍스트 메시지(커맨드 제외) 모두 처리
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), forward_to_admin))

    print("🚀 봇 실행 중입니다. 메시지를 기다리는 중...")
    app.run_polling()
