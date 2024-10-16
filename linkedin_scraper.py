import csv
import logging
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData, EventMetrics
from linkedin_jobs_scraper.query import Query, QueryOptions, QueryFilters
from linkedin_jobs_scraper.filters import RelevanceFilters, TimeFilters, TypeFilters, ExperienceLevelFilters, OnSiteOrRemoteFilters


# Change root logger level (default is WARN)
logging.basicConfig(level=logging.INFO)

LI_AT_COOKIE= "AQEDAUAit4YDaoAMAAABhpsBFTwAAAGHvtnc804Afl5g_SxbzFa_jkYJyc7H07BTqTjR-CRgzurvywRe_kJpRW_kAR-J9rYdh9vt0MCh-GPZdal1gSNvpYRK1Ko8IdFmrq-yg2oSuvd2In08CoXeY5s1"

# Create a CSV file and set up a writer
with open('jobs.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Title', 'Company', 'Date', 'Job Link', 'Description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()


# Fired once for each successfully processed job
def on_data(data: EventData):
    print('[ON_DATA]', data.title, data.company, data.date, data.link,
          len(data.description))

    # Write the job information to the CSV file
    with open('jobs.csv', 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Company', 'Date', 'Job Link', 'Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({
            'Title': data.title,
            'Company': data.company,
            'Date': data.date,
            'Job Link': data.link,
            'Description': data.description
        })


# Fired once for each page (25 jobs)
def on_metrics(metrics: EventMetrics):
    print('[ON_METRICS]', str(metrics))


def on_error(error):
    print('[ON_ERROR]', error)


def on_end():
    print('[ON_END]')


scraper = LinkedinScraper(
    chrome_executable_path=None,  # Custom Chrome executable path (e.g. /foo/bar/bin/chromedriver) 
    chrome_options=None,  # Custom Chrome options here
    headless=True,  # Overrides headless mode only if chrome_options is None
    max_workers=1,  # How many threads will be spawned to run queries concurrently (one Chrome driver for each thread)
    slow_mo=5,  # Slow down the scraper to avoid 'Too many requests 429' errors (in seconds)
    page_load_timeout=40  # Page load timeout (in seconds)    
)

# Add event listeners
scraper.on(Events.DATA, on_data)
scraper.on(Events.ERROR, on_error)
scraper.on(Events.END, on_end)

queries = [
    Query(
        query='Data Analyst',
        options=QueryOptions(
            limit=25,  # Limit the number of jobs to scrape.
            locations=['United States'],
            apply_link=False,  # Try to extract apply link (easy applies are skipped). If set to True, scraping is slower because an additional page mus be navigated. Default to False.
            skip_promoted_jobs=True,  # Skip promoted jobs. Default to False.
            filters=QueryFilters(
                relevance=RelevanceFilters.RECENT,
                time=TimeFilters.MONTH,
                type=[TypeFilters.FULL_TIME],
                on_site_or_remote=[OnSiteOrRemoteFilters.REMOTE]
            )
        )
    ),
]

scraper.run(queries)