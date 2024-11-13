import csv
import pandas as pd

def main() -> None:
    
    data = pd.read_csv('../day_25/2018_Squirrel_Data.csv')
    
    fur_color = data['Primary Fur Color'].value_counts().reset_index()
    
    fur_color.to_csv("squirrel_color_counts.csv")
    
    print(fur_color)


if __name__ == '__main__':
    main()