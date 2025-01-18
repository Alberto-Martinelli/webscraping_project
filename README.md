# User Manual

## Overview
This project extracts, processes, and analyzes hotel reviews in New York City. Using tools like Foursquare API, Playwright, and machine learning models, the project gathers insights into customer sentiments and clusters reviews into actionable categories. The following steps guide users on how to set up, run, and explore the project using Google Colab.

## Prerequisites
- A Google account for accessing Google Colab.
- Access to the project files and data, which can be found in the [GitHub Repository](https://github.com/Alberto-Martinelli/webscraping_project/tree/final).
- Basic familiarity with Python and Jupyter notebooks.

## Getting Started

### Step 1: Open Google Colab
1. Go to [Google Colab](https://colab.research.google.com/).
2. Upload the provided notebooks (`Webscraping_Notebook.ipynb` and `ML_Notebook.ipynb`) by clicking **File > Upload Notebook**.

### Step 2: Install Required Libraries
Run the following command at the beginning of each notebook to install necessary libraries:

```python
!pip install playwright pandas scikit-learn matplotlib seaborn vaderSentiment
```

For Playwright, set it up with:

```python
!playwright install
```

## Starting Repository

When cloning the repository, users will have the following files:
1. **`kayak_hotel_links.txt`**: A text file containing Kayak hotel URLs for the web scraping process.
2. **`Webscraping_Notebook.ipynb`**: The Jupyter Notebook for scraping hotel data.
3. **`api_playwright_aggregated_reviews.csv`**: The output CSV file of the web scraping notebook.
4. **`ML_Notebook.ipynb`**: The Jupyter Notebook for performing machine learning analysis on the scraped data.

## Web Scraping Notebook

### Overview
The `Webscraping_Notebook.ipynb` collects hotel data using:
- **Foursquare API**: Provides hotel metadata and user reviews.
- **Playwright**: Scrapes user reviews dynamically from the Kayak website.

### Instructions
1. **Run API and Web Scraping:**
   - Set your Foursquare API key in the provided cell.
   - Execute the scraping logic for both Foursquare and Kayak as described in the notebook.
2. **Store Data:**
   - The scraped data is saved as a CSV file (`api_playwright_aggregated_reviews.csv`).
   - Modify file paths if necessary for Google Drive or Colab storage.
3. **Review Logs:**
   - The notebook includes error handling for scraping failures. Check logs for details if an issue occurs.

### Output
A dataset containing hotel information, user reviews, and metadata.

## Machine Learning Notebook

### Overview
The `ML_Notebook.ipynb` analyzes the scraped data using:
- **Exploratory Data Analysis (EDA)**
- **Sentiment Analysis**
- **Clustering Techniques**

### Instructions
1. **Load Data:**
   - Upload the CSV file (`api_playwright_aggregated_reviews.csv`) generated from the web scraping notebook.
2. **Perform EDA:**
   - Visualize key patterns using WordClouds and charts.
3. **Run Sentiment Analysis:**
   - Sentiment scores are calculated using VADER.
4. **Apply Clustering:**
   - TF-IDF vectorization and K-Means clustering group reviews by themes.

### Output
- Insights into customer preferences for social and functional hotel features.
- Recommendations for hotel managers and systems based on identified clusters.

## Use Cases
This section highlights practical applications of the project, showcasing how its functionalities can address real-world challenges. From enhancing customer experiences to supporting data-driven marketing strategies, these use cases illustrate the versatility and value of the prototype for hotel managers, travel platforms, and market analysts. Each example provides a scenario, step-by-step guidance, and expected outcomes to demonstrate the impact of the project in actionable terms.

### Use Case 1: Improving Customer Experience
- **Scenario:** A hotel manager wants to improve the rooftop ambiance based on customer feedback.
- **Steps:**
  1. Use the web scraping notebook to gather reviews mentioning the rooftop.
  2. Analyze the sentiment and clustering results in the ML notebook to identify common themes in negative feedback.
  3. Implement targeted improvements, such as better decor or additional services.
- **Outcome:** Enhanced customer satisfaction and improved reviews.

### Use Case 2: Personalized Recommendations
- **Scenario:** A travel platform wants to recommend hotels based on functional and social features.
- **Steps:**
  1. Use clustering insights from the ML notebook to identify hotels with specific strengths (e.g., social features like a rooftop bar).
  2. Match customer preferences with hotel features.
  3. Provide personalized recommendations based on the analysis.
- **Outcome:** More accurate and user-focused hotel suggestions.

### Use Case 3: Market Analysis
- **Scenario:** A market analyst wants to compare customer sentiments across different hotel categories.
- **Steps:**
  1. Aggregate review data from multiple hotels using the web scraping notebook.
  2. Perform sentiment analysis and clustering to identify trends within categories.
  3. Generate a report highlighting strengths and weaknesses across categories.
- **Outcome:** Actionable insights for marketing strategies and competitive positioning.

## Recommendations

### Best Practices
- **Respect API Limits:** Avoid excessive requests to the Foursquare API.
- **Handle Errors:** Use the robust error-handling logic in Playwright to manage dynamic content scraping.
- **Explore Insights:** Use the results from the ML notebook to inform practical strategies for hotel improvements and personalized recommendations.

### Enhancements
- Update scraping logic to include additional review platforms.
- Expand ML analysis to integrate other NLP techniques like topic modeling.

## Troubleshooting

- **Scraping Issues:**
  - Ensure the Playwright framework is properly installed.
  - Adjust scraping delays for JavaScript-rendered content.
- **API Issues:**
  - Check API key validity and rate limits.
- **Colab Errors:**
  - Restart the runtime if memory or resource limits are exceeded.

For further assistance, refer to the [GitHub Repository](https://github.com/Alberto-Martinelli/webscraping_project/tree/final) or contact the project maintainers.
