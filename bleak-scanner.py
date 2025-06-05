import asyncio, logging 
from bleak import BleakScanner
logging.basicConfig(level=logging.DEBUG)
async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)

asyncio.run(main())

