import nest_asyncio
import asyncio
import atexit
import pandas as pd
from playwright.async_api import async_playwright

# Allow nested event loops
nest_asyncio.apply()

async def scrape_reviews_with_playwright_async(hotel_url):
    reviews = []

    pw = await async_playwright().start()
    browser = await pw.chromium.launch(headless=False)  # Set to False for debugging
    page = await browser.new_page()

    # All methods are async (use the "await" keyword)
    # Navigate to the hotel details page
    await page.goto(hotel_url)

    try:
        # Accept cookies if the cookie banner is present
        if await page.locator("button:has-text('Accept')").is_visible():
            await page.locator("button:has-text('Accept')").click()
            print("Cookies accepted.")

        # Extract the hotel name
        hotel_name_element = await page.query_selector("h1.c3xth-hotel-name")  # Updated selector for the hotel name
        hotel_name = (await hotel_name_element.inner_text()).strip() if hotel_name_element else "Unknown Hotel"
        print(f"Hotel Name: {hotel_name}")

        # Wait for the reviews section to load
        await page.wait_for_selector(".acD_-reviews-row-header", timeout=30000)

        # Locate review containers
        review_elements = await page.query_selector_all(".acD_")

        for review in review_elements:
            try:
                # Extract rating
                rating_element = await review.query_selector(".wdjx-positive")
                rating = (await rating_element.inner_text()).strip() if rating_element else None
                # Extract score description
                score_description_element = await review.query_selector(".acD_-score-description")
                score_description = (
                    await score_description_element.inner_text()).strip() if score_description_element else None
                # Extract user name and date
                user_name_date_element = await review.query_selector(".acD_-userName")
                user_name_date = (await user_name_date_element.inner_text()).strip() if user_name_date_element else None
                # Extract pros/advantages
                pros_element = await review.query_selector(".acD_-pros")
                pros = (await pros_element.inner_text()).strip() if pros_element else None
                # Extract the full review text
                full_review_element = await review.query_selector("span[id^='showMoreText']")
                full_review = (await full_review_element.inner_text()).strip() if full_review_element else None

                # Append review data
                reviews.append({
                    'Hotel Name': hotel_name,
                    'Rating': rating,
                    'Score Description': score_description,
                    'User and date': user_name_date,
                    'Pros': pros,
                    'Full Review': full_review
                })
            except Exception as e:
                print(f"Error processing review: {e}")

    except Exception as e:
        print(f"Error loading reviews: {e}")
    finally:
        await browser.close()

    # Function to close browser and stop Playwright
    async def shutdown_playwright():
        await browser.close()
        await pw.stop()

    # Register shutdown hook for when the program exits
    atexit.register(lambda: asyncio.run(shutdown_playwright()))

    return reviews

async def scrape():
    links_file = "kayak_hotel_links.txt"  # Ensure this file exists in the same directory
    with open(links_file, 'r') as file:
        hotel_urls = file.read().splitlines()
        all_reviews = []

        for hotel_url in hotel_urls:
            print(f"Scraping reviews for: {hotel_url}")
            reviews_data = await scrape_reviews_with_playwright_async(hotel_url)

            if reviews_data:
                all_reviews.extend(reviews_data)
                print(f"Scraped {len(reviews_data)} reviews from {hotel_url}.")
            else:
                print(f"No reviews found for {hotel_url}.")

        if all_reviews:
            reviews_df = pd.DataFrame(all_reviews)
            if 'User and date' in reviews_df.columns:
                reviews_df['User and date'] = reviews_df['User and date'].str.split(pat=', ')
                reviews_df['User and date'] = reviews_df['User and date'].transform(
                    lambda l: l[1] if isinstance(l, list) and len(l) > 1 else None)
                reviews_df.rename(columns={'User and date': 'Date'}, inplace=True)
                reviews_df['Date'] = pd.to_datetime(reviews_df['Date'], format='%b %Y', errors='coerce')
            reviews_df.to_csv("hotel_reviews_playwright.csv", index=False)
            print("All reviews saved to hotel_reviews_playwright.csv.")
        else:
            print("No reviews were scraped.")

if __name__ == '__main__':
    asyncio.run(scrape())
