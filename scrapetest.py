from playwright.sync_api import sync_playwright
import pandas as pd

def scrape_reviews_with_playwright(hotel_url):
    reviews = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to False for debugging
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the hotel details page
        page.goto(hotel_url)

        try:
            # Accept cookies if the cookie banner is present
            if page.locator("button:has-text('Accetta')").is_visible():
                page.locator("button:has-text('Accetta')").click()
                print("Cookies accepted.")

            # Wait for the reviews section to load
            page.wait_for_selector(".acD_-reviews-row-header", timeout=30000)

            # Locate review containers
            review_elements = page.query_selector_all(".acD_")

            for review in review_elements:
                try:
                    # Extract rating
                    rating = review.query_selector(".wdjx-positive").inner_text().strip() if review.query_selector(".wdjx-positive") else None
                    # Extract score description
                    score_description = review.query_selector(".acD_-score-description").inner_text().strip() if review.query_selector(".acD_-score-description") else None
                    # Extract user name and date
                    user_name_date = review.query_selector(".acD_-userName").inner_text().strip() if review.query_selector(".acD_-userName") else None
                    # Extract pros/advantages
                    pros = review.query_selector(".acD_-pros").inner_text().strip() if review.query_selector(".acD_-pros") else None
                    # Extract the full review text
                    full_review = review.query_selector("span[id^='showMoreText']").inner_text().strip() if review.query_selector("span[id^='showMoreText']") else None

                    # Append review data
                    reviews.append({
                        'Rating': rating,
                        'Score Description': score_description,
                        'User': user_name_date,
                        'Pros': pros,
                        'Full Review': full_review
                    })
                except Exception as e:
                    print(f"Error processing review: {e}")

        except Exception as e:
            print(f"Error loading reviews: {e}")
        finally:
            browser.close()

    return reviews


if __name__ == "__main__":
    # Replace with the Kayak hotel URL
    hotel_url = "https://www.kayak.it/hotels/InterContinental-New-York-Barclay,New-York-p59560-h14931-details"
    print("Scraping reviews for the hotel...")
    reviews_data = scrape_reviews_with_playwright(hotel_url)

    # Save reviews to CSV
    if reviews_data:
        reviews_df = pd.DataFrame(reviews_data)
        reviews_df.to_csv("hotel_reviews_playwright.csv", index=False)
        print("Reviews saved to hotel_reviews_playwright.csv.")
    else:
        print("No reviews found.")