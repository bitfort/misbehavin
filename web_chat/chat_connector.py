import asyncio
from playwright.async_api import async_playwright

from abc import ABC, abstractmethod


class ChatConnector(ABC):
    def __init__(self):
        pass

    @abstractmethod
    async def start(self, browser, url):
        pass

    @abstractmethod
    async def chat(self, message):
        pass


class BestBuyChatConnector(ChatConnector):
    def __init__(self):
        super().__init__()
        self.browser = None
        self.context = None
        self.page = None
        self.chat_started = False

    async def start(self, browser, url):
        self.browser = browser
        self.context = await self.browser.new_context()
        self.page = await self.context.new_page()
        await self.page.goto(url)
        # wait 5 seconds
        await asyncio.sleep(5)
        # close the survey invite
        if await self.page.query_selector("button#survey_invite_no"):
            await self.page.click("button#survey_invite_no")
            await asyncio.sleep(5)
        await self.page.get_by_label("Best Buy Help. Hi, need").click()

    async def chat(self, message):
        if self.chat_started:
            await self.page.get_by_placeholder("Type your message to the").click()
            await self.page.get_by_placeholder("Type your message to the").fill(message)
            await self.page.get_by_role("button", name="Send message").click()
            await asyncio.sleep(10)
        else:
            await self.page.get_by_placeholder("Ask our chatbot").click()
            await self.page.get_by_placeholder("Ask our chatbot").fill(message)
            await self.page.get_by_test_id("submit-btn").click()
            self.chat_started = True
            await asyncio.sleep(20)


async def main():
    connector = BestBuyChatConnector()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        await connector.start(browser=browser, url="https://www.bestbuy.com/")
        await connector.chat("Hello")
        await connector.chat("What is your name?")


if __name__ == "__main__":
    asyncio.run(main())
