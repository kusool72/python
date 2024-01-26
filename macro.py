import FinanceDataReader as fdr
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import sys

plt.rcParams["figure.figsize"] = (14, 8)
plt.rcParams['lines.linewidth'] = 1

# 코스피 vs 나스닥
df = fdr.DataReader('KS11', '2010')
df.plot()

# df = fdr.DataReader('DJI', '2010')
# df.plot()

# # 1. 나스닥지수 종합지수
# df = fdr.DataReader('FRED:NASDAQCOM')
# df.plot()
#
# # 2. 주간 실업수당 청구 건수 (ICSA)
# df = fdr.DataReader('FRED:NASDAQCOM,ICSA', start='2006')
# df.tail()
# df.plot(secondary_y='NASDAQCOM')
#
# # 3. 소비자심리지수 (UMCSENT)
# df = fdr.DataReader('FRED:NASDAQCOM,UMCSENT', start='2006')
# ax = df.plot(secondary_y='NASDAQCOM')
# ax.axvspan('2007-12-01', '2009-03-30', color='gray', alpha=0.2)
# ax.axvspan('2021-03-01', '2022-03-30', color='gray', alpha=0.2)
#
# # 4. 주택 판매 지수 (HSN1F)
# df = fdr.DataReader('FRED:NASDAQCOM,HSN1F', start='2005')
# ax = df.plot(secondary_y='NASDAQCOM')
# ax.axvspan('2007-12-01', '2009-03-30', color='gray', alpha=0.2)
# ax.axvspan('2021-03-01', '2022-03-30', color='gray', alpha=0.2)
#
# # 5. 실업률 (UNRATE)
df = fdr.DataReader('FRED:NASDAQCOM,UNRATE', start='2005')
ax = df.plot(secondary_y='NASDAQCOM')
ax.axvspan('2007-12-01', '2009-03-30', color='gray', alpha=0.2)
ax.axvspan('2021-03-01', '2022-03-30', color='gray', alpha=0.2)
#
# # 6. M2 통화량(M2SL)
# df = fdr.DataReader('FRED:NASDAQCOM,M2SL', start='2005')
# ax = df.plot(secondary_y='NASDAQCOM')
# ax.axvspan('2007-12-01', '2009-03-30', color='gray', alpha=0.2)
# ax.axvspan('2021-03-01', '2022-03-30', color='gray', alpha=0.2)
#
# # 7. 하이일드 채권 스프레드 (BAMLH0A0HYM2)
# df = fdr.DataReader('FRED:NASDAQCOM,BAMLH0A0HYM2', start='2005')
# ax = df.plot(secondary_y='NASDAQCOM')
# ax.axvspan('2007-12-01', '2009-03-30', color='gray', alpha=0.2)
# ax.axvspan('2021-03-01', '2022-03-30', color='gray', alpha=0.2)

plt.show()
