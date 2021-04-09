import pandas as pd
import datetime as dt
from pmaw import PushshiftAPI
api = PushshiftAPI()

'''
Reference: 
pmaw: https://medium.com/swlh/how-to-scrape-large-amounts-of-reddit-data-using-pushshift-1d33bde9286
Datatime: https://www.w3schools.com/python/python_datetime.asp

'''

# subreddit = "personalfinance"
# limit = 100000

def scrape(subreddit, limit, before_date, after_date):
    '''
    Input:
        before_date: format '2021-02-01'
        after_date: format '2020-12-01'
    '''
    before = int(dt.datetime.strptime(before_date, '%Y-%m-%d').timestamp())
    after = int(dt.datetime.strptime(after_date, '%Y-%m-%d').timestamp())

    submissions = api.search_submissions(subreddit=subreddit, 
                                   limit=limit, 
                                   before=before, 
                                   after=after)

    print(f'Retrieved {len(submissions)} submissions from Pushshift')

    f = f'{subreddit}_{after_date}_{before_date}'
    submissions_df = pd.DataFrame(submissions)
    submissions_df.to_csv(f, header=True, index=False)

    return submissions_df
    

def selected_columns(df, column_lst=['title','author', 'selftext','url','score','created_utc']):
    return df[column_lst]