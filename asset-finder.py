#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: Muneer Muhammed
The below given Python script is used to fetch data out of Yahoo databases and few other to
find out the history of previous investments in stock.
Here in this I have used Python Numpy to generate a graphical representation of data.
"""

import bt

# user inputs the start date and end date

start = '2000-01-01'
end = '2017-01-01'

# user inputs the strategic allocation. this is what the form is based off
# needs to be looped so that user can input less than 10 assets or more than 10
# the algorithm for the strategic portfolio is below
# Strategic Allocation

asset1, asset2, asset3, asset4, asset5, asset6, asset7, asset8, asset9, asset10 = 'spy', 'jnj', 'wmt', 'c', 'jpm', 'gs', 'aapl', 'hd', 'luv', 'cat'

# user inputs weights, each asset must be matched to a weight
# weights must add to 1 or 100%
# Strategic Weights

weights2 = {'sticker1': 0.20, 'sticker2': 0.20, 'sticker3': 0.20, 'sticker4': 0.15, 'sticker5': 0.15, 'sticker6': 0.10,
            'sticker7': 0.00, 'sticker8': 0.00, 'sticker9': 0.00, 'sticker10': 0.00
            }


def perissos_allweather(ticker, start=start, end=end, name='perissos_allweather'):
    data = bt.get(ticker, start=start, end=end)
    data = data.asfreq(freq='M', method='pad')
    EntryAlgorithm = data.ewm(span=6).mean()
    ExitAlgorithm = data.ewm(span=12).mean()
    tw = EntryAlgorithm.copy()
    tw[EntryAlgorithm > ExitAlgorithm] = 1.0
    tw[EntryAlgorithm <= ExitAlgorithm] = 0.00
    Perissos = bt.Strategy(name, [bt.algos.WeighTarget(tw),
                                  bt.algos.RunMonthly(),
                                  bt.algos.Rebalance()], [ticker])
    return bt.Backtest(Perissos, data)


aticker1, aticker2, aticker3, aticker4, aticker5, aticker6, aticker7, aticker8, aticker9, aticker10 = 'spy', 'vustx', 'vgpmx', 'jnj', 'cat', 'gs', 'jpm', 'c', 'mcd', 'f'

aasset1 = perissos_allweather(aticker1, name='aticker1')
aasset2 = perissos_allweather(aticker2, name='aticker2')
aasset3 = perissos_allweather(aticker3, name='aticker3')
aasset4 = perissos_allweather(aticker4, name='aticker4')
aasset5 = perissos_allweather(aticker5, name='aticker5')
aasset6 = perissos_allweather(aticker6, name='aticker6')
aasset7 = perissos_allweather(aticker7, name='aticker7')
aasset8 = perissos_allweather(aticker8, name='aticker8')
aasset9 = perissos_allweather(aticker9, name='aticker9')
aasset10 = perissos_allweather(aticker10, name='aticker10')

res1 = bt.run(aasset1, aasset2, aasset3, aasset4, aasset5, aasset6, aasset7, aasset8, aasset9, aasset10)

data1 = bt.merge(res1['aticker1'].prices, res1['aticker2'].prices, res1['aticker3'].prices, res1['aticker4'].prices,
                 res1['aticker5'].prices, res1['aticker6'].prices, res1['aticker7'].prices, res1['aticker8'].prices,
                 res1['aticker9'].prices, res1['aticker10'].prices,
                 )

weights = {'aticker1': .70, 'aticker2': 0.30, 'aticker3': 0.00, 'aticker4': 0.00, 'aticker5': 0.00, 'aticker6': 0.00,
           'aticker7': 0.00, 'aticker8': 0.00, 'aticker9': 0.00, 'aticker10': 0.00,
           }

perissos_allweather = bt.Strategy('Perissos All-Weather',
                                  [bt.algos.SelectAll(), bt.algos.WeighSpecified(**weights), bt.algos.Rebalance()])
t = bt.Backtest(perissos_allweather, data1)


# Perissos Aggressive

def perissos_aggressive(ticker, start=start, end=end, name='valerian_aggressive'):
    data = bt.get(ticker, start=start, end=end)
    data = data.asfreq(freq='M', method='pad')

    EntryAlgorithm = data.ewm(span=6).mean()
    ExitAlgorithm = data.ewm(span=12).mean()

    tw = EntryAlgorithm.copy()
    tw[EntryAlgorithm > ExitAlgorithm] = 1.0
    tw[EntryAlgorithm <= ExitAlgorithm] = 0.00

    Perissos2 = bt.Strategy(name, [bt.algos.WeighTarget(tw), bt.algos.RunMonthly(), bt.algos.Rebalance()], [ticker])
    return bt.Backtest(Perissos2, data)


ticker1, ticker2, ticker3, ticker4, ticker5, ticker6, ticker7, ticker8, ticker9, ticker10, = 'spy', 'vustx', 'vgpmx', 'jnj', 'cat', 'wmt', 'jnj', 'c', 'gs', 'mcd'

vasset1 = perissos_aggressive(ticker1, name='ticker1')
vasset2 = perissos_aggressive(ticker2, name='ticker2')
vasset3 = perissos_aggressive(ticker3, name='ticker3')
vasset4 = perissos_aggressive(ticker4, name='ticker4')
vasset5 = perissos_aggressive(ticker5, name='ticker5')
vasset6 = perissos_aggressive(ticker6, name='ticker6')
vasset7 = perissos_aggressive(ticker7, name='ticker7')
vasset8 = perissos_aggressive(ticker8, name='ticker8')
vasset9 = perissos_aggressive(ticker9, name='ticker9')
vasset10 = perissos_aggressive(ticker10, name='ticker10')

res2 = bt.run(vasset1, vasset2, vasset3, vasset4, vasset5, vasset6, vasset7, vasset8, vasset9, vasset10)

data = bt.merge(res2['ticker1'].prices, res2['ticker2'].prices, res2['ticker3'].prices, res2['ticker4'].prices,
                res2['ticker5'].prices, res2['ticker6'].prices, res2['ticker7'].prices, res2['ticker8'].prices,
                res2['ticker9'].prices, res2['ticker10'].prices)

weights = {'ticker1': 1.0, 'ticker2': 0.00, 'ticker3': 0.00, 'ticker4': 0.00, 'ticker5': 0.00, 'ticker6': 0.00,
           'ticker7': 0.00, 'ticker8': 0.00, 'ticker9': 0.00, 'ticker10': 0.00}

perissos_aggressive = bt.Strategy('Perissos Aggressive',
                                  [bt.algos.SelectAll(),
                                   bt.algos.WeighSpecified(**weights),
                                   bt.algos.Rebalance()])

t2 = bt.Backtest(perissos_aggressive, data)
res6 = bt.run(t2)


# Strategic

def strategic_model(ticker, start=start, end=end, name='strategic_model'):
    data0 = bt.get(ticker, start=start, end=end)
    data0 = data0.asfreq(freq='M', method='pad')
    Strategic = bt.Strategy(name, [bt.algos.SelectAll(), bt.algos.WeighEqually(), bt.algos.Rebalance()], [ticker])
    return bt.Backtest(Strategic, data0)


sticker1 = strategic_model(asset1, name='sticker1')
sticker2 = strategic_model(asset2, name='sticker2')
sticker3 = strategic_model(asset3, name='sticker3')
sticker4 = strategic_model(asset4, name='sticker4')
sticker5 = strategic_model(asset5, name='sticker5')
sticker6 = strategic_model(asset6, name='sticker6')
sticker7 = strategic_model(asset7, name='sticker7')
sticker8 = strategic_model(asset8, name='sticker8')
sticker9 = strategic_model(asset9, name='sticker9')
sticker10 = strategic_model(asset10, name='sticker10')

res3 = bt.run(sticker1, sticker2, sticker3, sticker4, sticker5, sticker6, sticker7, sticker8, sticker9, sticker10)

data2 = bt.merge(res3['sticker1'].prices, res3['sticker2'].prices, res3['sticker3'].prices, res3['sticker4'].prices,
                 res3['sticker5'].prices, res3['sticker6'].prices, res3['sticker7'].prices, res3['sticker8'].prices,
                 res3['sticker9'].prices, res3['sticker10'].prices,
                 )

weights = weights2
Strategic = bt.Strategy('Strategic', [bt.algos.SelectAll(),
                                      bt.algos.RunMonthly(),
                                      bt.algos.WeighSpecified(**weights),
                                      bt.algos.Rebalance()])

t3 = bt.Backtest(Strategic, data2)
res5 = bt.run(t3)

# Benchmark
# user inputs benchmark symbol

data3 = bt.get('spy', start=start, end=end)

data3 = data3.asfreq(freq='M', method='pad')

Bench = bt.Strategy('S&P 500', [bt.algos.SelectAll(),
                                bt.algos.RunMonthly(), bt.algos.WeighEqually(),
                                bt.algos.Rebalance()])
t4 = bt.Backtest(Bench, data3)

# Results

res = bt.run(t, t2, t3, t4)

# Plots & Graphics
# To show the graph of comparison algorithm.

res.plot()

# To show the data in tabular form withing the selected start and end date.
res.display()
print 'S&P 500'

# To display the data in the basis of each month.
res.display_monthly_returns('S&P 500')

# To display the in 'Strategic' algorithm
# Display data in every month.
res.display_monthly_returns('Strategic')

# Aggressive monthly returns.
res.display_monthly_returns('Perissos Aggressive')

# All weather monthly returns
res.display_monthly_returns('Perissos All-Weather')
res.plot_correlation()

