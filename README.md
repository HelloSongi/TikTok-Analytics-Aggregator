
# TikTok Analytics Aggregator Data Engineering Project

Demo Video

https://github.com/HelloSongi/TikTok-User-data-analysis/assets/69304233/7d407c04-5bd8-4cd6-8508-5f7d956410b2


This repository contains a data engineering project that fetches TikTok user data, performs data processing, and stores the results in a MongoDB database. The project is built using Python, Flask, BeautifulSoup, requests, and pymongo.

## Project Overview

The TikTok Analytics Data Engineering project aims to collect and analyze user data from the TikTok platform. It provides a web application where users can enter a TikTok username, and the application fetches the user's profile information, including the total number of followers, following, likes, and video views. It also retrieves information about the user's recent videos, such as the video title, views, and a link to watch the video.

The project involves the following main components:

1. **Web Scraping**: The application utilizes the BeautifulSoup library to scrape the TikTok website and extract the required user data. It sends HTTP requests to the TikTok website, parses the HTML response, and extracts the relevant information using CSS selectors.

2. **Data Processing**: The fetched user data is processed and converted into a structured format using pandas/Pyspark. Numeric values, such as follower count, following count, likes, and views, are converted to integers for easier analysis.

3. **Database Integration**: The processed user data is stored in a MongoDB database using the pymongo library. The MongoDB database provides a flexible and scalable solution for storing and querying the collected TikTok user data.

4. **Web Application**: The Flask framework is used to develop a web application that allows users to enter a TikTok username. The application fetches the user data, performs data processing, and displays the results on a web page. Users can view the total followers, following, likes, and video views of the TikTok user, as well as their recent video information.

## Project Structure

The repository structure is organized as follows:

- `tiktok_app.py`: The main Flask application file that handles routing and web request handling.
- `templates/`: A directory containing HTML templates for the web application's user interface.
  - `index.html`: The main template for the home page where users can enter a TikTok username.
  - `result.html`: The template for displaying the fetched user data and analysis results.
  - `visuals.js`: A javascript(chartjs) file that handles dashboard/visualization
- `processing_pandas.py`: A python file processing incoming data with pandas
- `processing_spark.py`: A python file processing data using apache spark

## Getting Started

To run the project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/tiktok-analytics.git`
2. Install the required Python packages: `pip install -r requirements.txt`
3. Update the MongoDB connection string in `tiktok_app.py` with your own MongoDB connection details.
4. Run the Flask application: `python tiktok_app.py`
5. Access the web application in your browser at `http://localhost:5000`.

Make sure you have Python, Flask, and the necessary dependencies installed on your system.

## Contributing

Contributions to the project are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

Feel free to modify and customize this description to suit your specific project details and preferences.
