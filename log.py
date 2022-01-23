def create_log_message(update):
    text = str(update.message.text)
    from_user = str(update.message.from_user)
    message_id = str(update.message.message_id)
    update_id = str(update.update_id)
    return "{'update_id': " + update_id +\
           ", 'message_id': " + message_id +\
           ", 'user': " + from_user +\
           ", 'text command': '" + text + "'}"
