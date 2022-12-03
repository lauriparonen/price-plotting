import pandas as pd
import matplotlib.pyplot as plt


# Function for plotting the data
def plot_data(file_path):
    # Read in the csv file and set the Date column as the index
    df = pd.read_csv(file_path, index_col="Date")

    # Plot the "Open" and "Close" columns, using the dates as the x-axis values
    df[["Open", "Close"]].plot()

    # Set the x-axis label
    plt.xlabel("Date")

    # Set the y-axis label
    plt.ylabel("Price")

    # Specify the locations and labels of the tick marks on the x-axis
    plt.xticks(range(0, len(df.index), 30), df.index[::30], rotation=45)

    # Show the plot
    plt.show()


def main():
    # Error handling if the file path is incorrect
    try:
        # Get the file path
        file_path = input("Enter the file path: ")

        # Plot the data
        plot_data(file_path)
    except FileNotFoundError:
        print("File not found; please check the file path and try again.")
        # try again
        main()


if __name__ == "__main__":
    main()
