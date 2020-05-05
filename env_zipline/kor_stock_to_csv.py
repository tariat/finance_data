import FinanceDataReader as fdr

"""
code="005930"
year="2019"
"""

def to_csv(code, year):
    """
    :param code: 종목코드
    :param year: 년도, string
    :return:
    """
    output_dir="./korean/daily"

    df=fdr.DataReader(code,year)
    df.head()

    df=df.reset_index(drop=False)
    df=df.drop("Change",1)
    df["dividend"]=0
    df["split"] = 1
    df.columns = [c.lower() for c in df.columns]

    df.to_csv("{}/{}.csv".format(output_dir,code), index=False)

    return 1

if __name__ == '__main__':
    to_csv("005930","2019")



