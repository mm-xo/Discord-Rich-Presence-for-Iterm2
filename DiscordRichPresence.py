import iterm2
import asyncio
from pypresence import Presence

clientId = ("1318136746642505738")
RPC = Presence(clientId)

def initConnection():
    try:
        RPC.connect()
    except Exception as c:
        print("Error with connection: {c}")

def getUpdates(localDir):
    try:
        RPC.update(details="In directory:", state=localDir)
    except Exception as u:
        print("Error with updates: {u}")

async def update_presence(session):
    """Update Discord Rich Presence continuously."""
    await asyncio.to_thread(initConnection)
    while True:
        localDir = await session.async_get_variable("session.path")
        await asyncio.to_thread(getUpdates, localDir)
        await asyncio.sleep(1) 

async def main(connection):
    """Main function for iTerm2 scripting."""
    app = await iterm2.async_get_app(connection)
    window = app.current_window
    if window is not None:
        session = window.current_tab.current_session
        if session is not None:
            await update_presence(session)
        else:
            print("No active session found.")
    else:
        print("No active window found.")

# Use asyncio to manage the event loop
if __name__ == "__main__":
    # asyncio.run(iterm2.run_forever(main))
    iterm2.run_forever(main)