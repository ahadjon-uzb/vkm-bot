from aiogram import Dispatcher


def setup(dispatcher: Dispatcher):
    from .is_owner import IsOwner

    text_messages = [
        dispatcher.message_handlers,
        dispatcher.edited_message_handlers,
    ]

    dispatcher.filters_factory.bind(IsOwner, event_handlers=text_messages)
