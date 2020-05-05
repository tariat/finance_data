import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
from matplotlib import rcParams

# 그래프 크기
graph_size = (9.2,5.8)

def use_kor_font():
    fm.get_fontconfig_fonts()
    font_location = '/Library/Fonts/NanumBarunGothicBold.ttf'
    font_name = fm.FontProperties(fname=font_location).get_name()
    plt.rc('font', family=font_name)


# 그래프 스타일을 지정합니다.
def graph_style(style="whitegrid"):
    #스타일 지정
    # darkgrid, whitegrid, dark, white, ticks
    sns.set_style(style)

    # 상단과 우측의 선제거
    sns.despine()

    #그래프 크기 지정
    sns.set(rc={'figure.figsize':graph_size})

    # 그래프 스타일 지정
    # paper, notebook(기본), talk, poster
    sns.set_context("notebook")

    # 한글폰트사용
    use_kor_font()



graph_style()


def xticks(degree=-45):
    plt.figure(figsize=graph_size)
    plt.xticks(rotation=degree)
    graph_style()
    return 0

def countplot(x):
    """
    countplot이용시 값을 출력합니다.
    """
    temp=x.value_counts()
    temp = temp.sort_values(ascending=False)
    g = sns.barplot(x=temp.index, y=temp, order=temp.index)
    for p in g.patches:
        g.annotate(format(p.get_height(), '.0f'), (p.get_x()+p.get_width()/2., p.get_height()),
                   ha='center', va='center', xytext=(0,10), textcoords='offset points')

    return g

def distplot(data, x, hue=None):
    """
    그룹별로 distplot을 그립니다.
    """
    apt_sale_1=data
    apt_sale_gr = apt_sale_1.groupby(hue)
    for d in apt_sale_gr:
        g= sns.distplot(d[1][x], kde_kws={"label":d[1][hue].max()})

    return g


def relplot(*args, **kwargs):
    """
    relplot의 사이즈를 조정합니다.
    """
    fig, ax = plt.subplots()
    # the size of A4 paper
    fig.set_size_inches(graph_size)

    g = sns.relplot(*args, **kwargs , ax=ax)

    graph_style()

    return g

def catplot(*args, **kwargs):
    """
    catplot을 그릴 때 x축 테스트를 -45도 회전합니다.
    """
    chart = sns.relplot(*args, **kwargs )
    chart.set_xticklabels(rotation=-45)

    return chart
