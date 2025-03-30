import iterm2
import asyncio
from pypresence import AioPresence

client_id = ("1318136746642505738")
RPC = AioPresence(client_id)

async def update_presence(session):
    """Update Discord Rich Presence continuously."""
    try:
        await RPC.connect()
        while True:
            local_dir = await session.async_get_variable("session.path")
            await RPC.update(details="In directory:", state=local_dir)
            await asyncio.sleep(1) 
    except Exception as e:
        print(f"Error with RPC: {e}")

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
    asyncio.run(iterm2.run_forever(main))