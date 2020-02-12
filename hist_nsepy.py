import pandas as pd
from datetime import date
from nsepy import get_history

scrip = input('Scrip:')

series = date(2004, 1, 29), date(2004, 2, 26), date(2004, 3, 25), date(2004, 4, 29), date(2004, 5, 27), date(2004, 6, 24), date(2004, 7, 29),\
    date(2004, 8, 26), date(2004, 9, 30), date(2004, 10, 28), date(2004, 11, 25), date(2004, 12, 30), date(2005, 1, 27), date(2005, 2, 24),\
    date(2005, 3, 31), date(2005, 4, 28), date(2005, 5, 26), date(2005, 6, 30), date(2005, 7, 28), date(2005, 8, 25), date(2005, 9, 29),\
    date(2005, 10, 27), date(2005, 11, 24), date(2005, 12, 29), date(2006, 1, 25), date(2006, 2, 23), date(2006, 3, 30), date(2006, 4, 27),\
    date(2006, 5, 25), date(2006, 6, 29), date(2006, 7, 27), date(2006, 8, 31), date(2006, 9, 28), date(2006, 10, 26), date(2006, 11, 30),\
    date(2006, 12, 28), date(2007, 1, 25), date(2007, 2, 22), date(2007, 3, 29), date(2007, 4, 26), date(2007, 5, 31), date(2007, 6, 28),\
    date(2007, 7, 26), date(2007, 8, 30), date(2007, 9, 27), date(2007, 10, 25), date(2007, 11, 29), date(2007, 12, 27), date(2008, 1, 31), \
    date(2008, 2, 28), date(2008, 3, 27), date(2008, 4, 24), date(2008, 5, 29), date(2008, 6, 26), date(2008, 7, 31), date(2008, 8, 28),\
    date(2008, 9, 25), date(2008, 10, 29), date(2008, 11, 27), date(2008, 12, 25), date(2009, 1, 29), date(2009, 2, 26), date(2009, 3, 26),\
    date(2009, 4, 30), date(2009, 5, 28), date(2009, 6, 25), date(2009, 7, 30), date(2009, 8, 27), date(2009, 9, 24), date(2009, 10, 29),\
    date(2009, 11, 26), date(2009, 12, 31), date(2010, 1, 28), date(2010, 2, 25), date(2010, 3, 25), date(2010, 4, 29), date(2010, 5, 27),\
    date(2010, 6, 24), date(2010, 7, 29), date(2010, 8, 26), date(2010, 9, 30), date(2010, 10, 28), date(2010, 11, 25), date(2010, 12, 30),\
    date(2011, 1, 27), date(2011, 2, 24), date(2011, 3, 31), date(2011, 4, 28), date(2011, 5, 26), date(2011, 6, 30), date(2011, 7, 28),\
    date(2011, 8, 25), date(2011, 9, 29), date(2011, 10, 25), date(2011, 11, 24), date(2011, 12, 29), date(2012, 1, 25), date(2012, 2, 23),\
    date(2012, 3, 29), date(2012, 4, 26), date(2012, 5, 31), date(2012, 6, 28), date(2012, 7, 26), date(2012, 8, 30), date(2012, 9, 27),\
    date(2012, 10, 25), date(2012, 11, 29), date(2012, 12, 27), date(2013, 1, 31), date(2013, 2, 28), date(2013, 3, 28), date(2013, 4, 25),\
    date(2013, 5, 30), date(2013, 6, 27), date(2013, 7, 25), date(2013, 8, 29), date(2013, 9, 26), date(2013, 10, 31), date(2013, 11, 28),\
    date(2013, 12, 26), date(2014, 1, 30), date(2014, 2, 26), date(2014, 3, 27), date(2014, 4, 24), date(2014, 5, 29), date(2014, 6, 26),\
    date(2014, 7, 31), date(2014, 8, 28), date(2014, 9, 25), date(2014, 10, 30), date(2014, 11, 27), date(2014, 12, 24), date(2015, 1, 29),\
    date(2015, 2, 26), date(2015, 3, 26), date(2015, 4, 30), date(2015, 5, 28), date(2015, 6, 25), date(2015, 7, 30), date(2015, 8, 27),\
    date(2015, 9, 24), date(2015, 10, 29), date(2015, 11, 26), date(2015, 12, 31), date(2016, 1, 28), date(2016, 2, 25), date(2016, 3, 31),\
    date(2016, 4, 28), date(2016, 5, 26), date(2016, 6, 30), date(2016, 7, 28), date(2016, 8, 25), date(2016, 9, 29), date(2016, 10, 27),\
    date(2016, 11, 24), date(2016, 12, 29), date(2017, 1, 25), date(2017, 2, 23), date(2017, 3, 30), date(2017, 4, 27), date(2017, 5, 25),\
    date(2017, 6, 29), date(2017, 7, 27), date(2017, 8, 31), date(2017, 9, 28), date(2017, 10, 26), date(2017, 11, 30), date(2017, 12, 28),\
    date(2018, 1, 25), date(2018, 2, 22), date(2018, 3, 28), date(2018, 4, 26), date(2018, 5, 31), date(2018, 6, 28), date(2018, 7, 26),\
    date(2018, 8, 30), date(2018, 9, 27), date(2018, 10, 25), date(2018, 11, 29), date(2018, 12, 27), date(2019, 1, 31), date(2019, 2, 28),\
    date(2019, 3, 28), date(2019, 4, 25), date(2019, 5, 30), date(2019, 6, 27), date(2019, 7, 25), date(2019, 8, 29), date(2019, 9, 26), \
    date(2019, 10, 31), date(2019, 11, 28), date(2019, 12, 26)


col = pd.DataFrame({'Date': [], 'Symbol': [], 'Expiry': [], 'Open': [], 'High': [], 'Low': [], 'Close': [], 'LTP': [], 'Settlement Price': [],
                    'Number of Contracts': [], 'Turnover': [], 'Open Interest': [], 'Change in OI': [], 'Underlying': []})


open(f'D:\homework\dataset\{scrip}.csv', 'w')

col.to_csv(f'D:\homework\dataset\{scrip}.csv', header=True, index=False)

for i in series:
    df_fut = get_history(symbol=scrip, start=date(2000, 1, 1), end=date(2020, 1, 20), futures=True, expiry_date=i)
    df_fut.to_csv(f'D:\homework\dataset\{scrip}.csv', mode='a', header=False)

