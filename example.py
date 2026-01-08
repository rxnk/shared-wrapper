from shared_api import SharedAPI

async def main():
    api = SharedAPI("http://server:1337", "api_key")
    user = await api.instagram.story("nba")
    print(user)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
    