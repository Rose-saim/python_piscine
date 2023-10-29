from load_csv import load
import matplotlib.pyplot as plt

def main():
    """This functions displays the country information of your campus."""
    try:
        country_name = "France"
        data = load("../life_expectancy_years.csv")
        print(data)

        fr_data = data.loc[data['country'] == country_name]
        plt.plot(x, y)
        x = plt.xlabel('Year')
        y = plt.ylabel('Life expectancy')
        plt.title(f"{country_name} Life expectancy Projections")
        plt.grid(True)
        plt.savefig("test.png")
        plt.show()
        plt.close()
    except Exception as e:
        print('Error:', e)
        exit(1)

if __name__ == "__main__":
    main()