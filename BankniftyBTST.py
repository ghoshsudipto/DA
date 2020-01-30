import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
plt.style.use('ggplot')
pd.set_option('display.max_column', 500)
pd.set_option('display.max_row', 50000)
pd.set_option('display.width', 5000)

slippage = 0.0005

df = pd.read_csv(r'C:\Users\Sudipto\Dropbox\Python\DA\datasets\BN.csv')
df[['Date','Expiry']] = df[['Date','Expiry']].apply(pd.to_datetime)
df.sort_values('Date', inplace=True)
df.set_index('Date', inplace=True)
df.drop(df.columns[[5, 6, 7, 8, 9, 10]], axis= 1, inplace=True)

long_state = (df['Expiry'] == df['Expiry'].shift(1)) & (df['Expiry'] == df['Expiry'].shift(-1)) & (df['Close'] > df['Close'].shift(1))
short_state = (df['Expiry'] == df['Expiry'].shift(1)) & (df['Expiry'] == df['Expiry'].shift(-1)) & (df['Close'] < df['Close'].shift(1))
state_condition = [long_state, short_state]
state_choice = [1, -1]
df['State'] = np.select(state_condition, state_choice)

LkaSL = (df['State'].shift(1) == 1) & (df['Low'].shift(1) > df['Low'])
SkaSL = (df['State'].shift(1) == -1) & (df['High'].shift(1) < df['High'])
SL_condition = [LkaSL, SkaSL]
SL_choice = [((df['Low'].shift(1) - df['Close'].shift(1))/df['Close'].shift(1)) - (2 * slippage),
            ((df['Close'].shift(1) - df['High'].shift(1))/df['Close'].shift(1)) - (2 * slippage)]
df['SL'] = np.select(SL_condition, SL_choice)

long_exit = (df.SL == 0) & (df.State.shift(1) == 1) & (df.State != 1)
long_carry = (df.SL == 0) & (df.State.shift(1) == 1) & (df.State == 1)
short_exit = (df.SL == 0) & (df.State.shift(1) == -1) & (df.State != -1)
short_carry = (df.SL == 0) & (df.State.shift(1) == -1) & (df.State == -1)
sl_exit = df.SL != 0
Payoff_condition = [long_exit, long_carry, short_exit, short_carry, sl_exit]
Payoff_choice = [df.Close.pct_change() - (2 * slippage), (df.Close.pct_change()),
                 -1*(df.Close.pct_change()) - (2 * slippage), -1*(df.Close.pct_change()), df.SL]

df['Payoff'] = np.select(Payoff_condition, Payoff_choice)
df['Cumulative'] = 100 * df.Payoff.cumsum()

print(' \n-o-o-o-o-o  RISK MEASURES  o-o-o-o-o-\n')

netPL = np.around(df.Cumulative.iloc[-1], decimals=2)
print('Net P/L:\n\t',netPL)

df['Payoff'].replace(0, np.NaN, inplace=True)
sharpe = np.around((252**0.5)*(df['Payoff'].mean()/np.std(df.Payoff)), decimals=4)
print('Sharpe Ratio:\n\t', sharpe)

hit_rate = np.around((len(df.loc[df.Payoff > 0])/ len(df.Payoff))*100, decimals=2)
print('Hit Rate:\n\t', hit_rate, '%')

gain_mean = df[df['Payoff'] >= 0].Payoff.mean()
loss_mean = df[df['Payoff'] <= 0].Payoff.mean()
win_loss = np.around(abs(gain_mean/loss_mean), decimals=2)
print('Win/Loss:\n\t', win_loss)

max_gain = np.around((np.nanmax(df['Payoff'].values)*100), decimals=2)
# max_gain = np.around((df['Payoff'].max()*100), decimals=2)
print('Max Gain:\n\t', max_gain, '%')

max_loss = np.around((np.nanmin(df['Payoff'].values)*100), decimals=2)
print('Max Loss:\n\t', max_loss, '%')

prev = float("-inf")
drawdown = []
for i in df['Cumulative']:
    drawdown.append((max(prev, i) - i))
    prev = max(prev, i)
df['Drawdown'] = drawdown
max_drawdown = np.around((np.nanmax(df['Drawdown'].values)), decimals=2)
print('Max Drawdown:\n\t', max_drawdown, '%')

plt.plot(df.index, df['Cumulative'], 'b', label='BTST BankNifty')
plt.title('BN Equity Curve')
plt.xlabel('Date')
plt.ylabel('Percentage return')
plt.gcf().autofmt_xdate()
plt.legend()
plt.tight_layout()
plt.show()



df.to_csv(line_terminator="\n")
its a window issue, its adding "\r" which is  a carriage return meaning "Enter"
line_terminator will help
