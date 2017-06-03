import asyncio
from themachine.core import publish

publish('github.start_user_process', {
    'username': 'tiagoad'
})
