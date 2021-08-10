import asyncio
from pyppeteer import launch


async def main():
    browser = await launch()
    page = await browser.newPage()
    width, height = await screen_size()
    await page.setViewport({'width': width, 'height': height})
    await page.goto('http://baidu.com')
    await page.screenshot({'path': 'example.png'})
    await browser.close()


async def screen_size():
    """使用tkinter获取屏幕大小"""
    import tkinter
    tk = tkinter.Tk()
    width = tk.winfo_screenwidth()
    height = tk.winfo_screenheight()
    tk.quit()
    return width, height


if __name__ == '__main__':
    main()
    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(main())
    loop.run_until_complete(asyncio.wait([task]))
