import matplotlib.pyplot as plt
from collections import Counter

choice = int(input('which schedule will you choose? - '))

if choice == 1:
    years = [1980,1990,2000,2010,2020]
    salary = [450,750,1150,1000,2500]

    plt.plot(years, salary)
    plt.ylabel('salary')
    plt.xlabel('year')
    plt.show()

elif choice == 2:
    movies_likes = ['Iron-man','Avengers','Iron-man-3','Iron-man-2']
    likes = [100,50,350,150]

    plt.bar(movies_likes,likes)
    plt.ylabel('likes')
    plt.xlabel('films')
    plt.show()
elif choice == 3:
    grades = [83,95,96,97,89,90,91,100,0,52,67,78]
    histogram = Counter(min(grade//10*10,90) for grade in grades)

    plt.bar([x+5 for x in histogram.keys()],histogram.values(),width=10,edgecolor=(0,0,0))
    plt.ylabel('students')
    plt.xlabel('grade')
    plt.show()
elif choice == 4:
    choice = int(input('Before and after chart (1,2) - '))
    if choice == 1:
        mentions = [500,505]
        years = [2017,2019]
        plt.title('look at the increase')
        plt.bar(years,mentions,0.8)
        plt.axis([2016.5,2019.5,499,510])
        plt.show()
        # y starts at 0 so the graph may confuse people
    elif choice == 2:
        mentions = [500,505]
        years = [2017,2019]
        plt.title('now the increase is not so big')
        plt.bar(years,mentions,0.8)
        plt.axis([2016.5,2019.4,0,510])
        plt.show()
        # the graph starts at 0, so the increase doesn't seem that big
    # in some cases it is not necessary/necessary to use axis, but be careful
elif choice == 5:
    variance = [1,2,4,8,16,32,64,128,256]
    bias_squares = [256,128,64,32,16,8,4,2,1]
    total_error = [x+y for x, y in zip(variance,bias_squares)]
    xs = [i for i, _ in enumerate(variance)]
    # plots:
    plt.plot(xs,variance,'-',label='variance')
    plt.plot(xs,bias_squares,'--',label='bies_squares')
    plt.plot(xs,total_error,'-.',label='total error')
    plt.show()
elif choice == 6:
    choice = int(input('1,2,3 - '))
    if choice == 1:
        friends = [70,60,80,75,47,89]
        minutes = [50,40,90,75,89,90]
        labels = ['a','b','c','d','e','f']
        plt.scatter(friends,minutes)
        for label, friend_count, minute_count, in zip(labels,friends,minutes):
            plt.annotate(label, xy=(friend_count,minute_count))
        plt.show()
    elif choice == 2:
        test_1_grades= [99,90,89,75,74,67]
        test_2_grades = [34,54,74,65,87,65]
        plt.scatter(test_1_grades,test_2_grades)
        plt.title('not comparable')
        plt.show()
    elif choice == 3:
        test_1_grades= [99,90,89,75,74,67]
        test_2_grades = [34,54,74,65,87,65]
        plt.scatter(test_1_grades,test_2_grades)
        plt.title('comparable')
        plt.axis('equal')
        plt.show()
