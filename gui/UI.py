"""
File: ui.py
Author(s): Daochen LI (daochenl), Yanting Hu (yantingh), Zheng ZHANG (zhengzh2)
Description: Application user interface
"""

import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split


def launch():
    """
    Launch main window with icon and function-oriented buttons
    """
    # Create dataframe for use of the complete application
    global df
    cleaned_data_path = './data/display/cleaned_data.csv'
    df = pd.read_csv(cleaned_data_path)
    
    # Create the root window
    global root
    root = tk.Tk()
    root.title("CityPulse - Relocation Recommendation Application")
    root.geometry("1000x650") # width * height

    # Frame
    centerFrame = Frame(root)
    centerFrame.pack(expand=True)

    # Randomly set app icon
    image_paths = [
        "./icons/_0c1d7967-7c8b-45c8-825f-98f6ef43d164.jpeg",
        "./icons/_1f30ad0d-a231-4e9a-9011-7a35c5644aa3.jpeg",
        "./icons/_5cbb978e-8e3c-4eb9-b1ae-6fb1c715cfcc.jpeg",
        "./icons/_9bf0596f-8504-459a-b25b-65f5d013f85a.jpeg",
        "./icons/_32f51e8a-c3ec-4135-a517-76631f6a8cb1.jpeg",
        "./icons/_49689280-eb9b-4495-b967-3f211140b2bb.jpeg",
        "./icons/_b98a97c6-8659-4680-9bd0-0853f2bb8152.jpeg",
    ]

    # Randomly choose an image path
    selected_image_path = random.choice(image_paths)

    # Open the selected image and resize it
    image = Image.open(selected_image_path).resize((350, 350))

    # Open the PNG image using Pillow
    image_ = image.resize((300, 300))

    # Convert the Pillow image to a Tkinter-compatible photo image
    photo = ImageTk.PhotoImage(image_)
    
    # Create a Canvas widget to display the image
    canvas = tk.Canvas(centerFrame, width=image_.width, height=image_.height)
    
    # Add the image to the canvas
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    canvas.pack()

    # Set app name label
    app_label = tk.Label(centerFrame, text="Welcome to CityPulse!")
    app_label.config(font=("Arial", 20))
    app_label.pack()

    # Set app info button
    app_info_btn = ttk.Button(centerFrame, text='App Info ©', command=app_info_btn_on_click, width=10)
    app_info_btn.pack()

    # Set app description label
    description_label = tk.Label(centerFrame, text="")
    app_description = (
        "Your go-to application for informed and personalized relocation decisions.\n"
        "We understand that moving to a new city is a significant life event, and we are here to make it seamless for you.\n"
    )
    description_label.config(text=f"{app_description}", wraplength=500)
    description_label.pack()

    # Set ttk button style
    style = ttk.Style()
    style.theme_use("aqua")

    # Initialize function buttons
    view_data_btn = ttk.Button(centerFrame, text='View Data', command=view_data_btn_on_click, width=20)
    city_summary_btn = ttk.Button(centerFrame, text='City Summary', command=city_summary_btn_on_click, width=20)
    city_comparison_btn = ttk.Button(centerFrame, text='City Comparison', command=city_comparison_btn_on_click, width=20)
    city_ranking_btn = ttk.Button(centerFrame, text='City Ranking', command=city_ranking_btn_on_click, width=20)
    
    view_data_btn.pack(pady=5)
    city_summary_btn.pack(pady=5)
    city_comparison_btn.pack(pady=5)
    city_ranking_btn.pack(pady=5)


    def quit_application():
        root.destroy()
    
    quit_button = ttk.Button(root, text="Quit", command=quit_application)
    quit_button.pack(padx=10, pady=10)

    # Run the Tkinter event loop
    root.mainloop()


def app_info_btn_on_click():
    """
    Open window displaying app info
    """
    # Window
    app_info_window = tk.Toplevel(root)
    app_info_window.title("Application Information")

    # Frame
    centerFrame = Frame(app_info_window)
    centerFrame.pack(expand=True)

    # Set app name label
    app_label = tk.Label(centerFrame, text="CityPulse")
    app_label.config(font=("Arial", 20))
    app_label.pack()
    
    # Set app description label
    app_description_text = (
        "App Description\n"
        "CityPulse harnesses an extensive array of data, sourcing information from reputable platforms like Salary.com, WalletHub.com, Numbeo.com, and others.\n"
        "The pivotal metrics encompass a spectrum of factors, including 1)Average Household Income, 2)Employment Rate, 3)Cost of Living Percentage, 4)Safety Index,"
        "5)Health Care Exp Index, 6)Pollution Index, and 7)Recreation Total Score.\n"
        "These metrics, carefully weighted and curated, empower users to navigate relocation decisions with a wealth of informed insights.\n"
        "By regularly refreshing the data utilized within the application, CityPulse remains dynamic and aligned with the latest trends and conditions,"
        "offering users a consistently reliable tool for making well-informed decisions about their prospective relocations."
        )
    app_description_label = ttk.Label(centerFrame, text=app_description_text, wraplength=800)
    app_description_label.pack(pady=10)

    # Set metrics description label
    metrics_description_text = (
        "Metrics Description\n"
        "1) Average Household Income: includes pretax cash income of the householder and all other people 15 years old and older in the household, whether or not they are related to the householder;\n"
        "2) Employment Rate: represents the proportion of the total 16 years old and over population that is in the labor force;\n"
        "3) Cost of Living Percentage: mainly uses the Consumer Price Index (CPI) and salary differentials of over 300+ US cities to compare costs and salary;\n"
        "4) Safety Index: opposite to the estimation of the overall level of crime in a given city;\n"
        "5) Health Care Exp Index: reflects the quality of a healthcare system by emphasizing the positive aspects more significantly through an exponential increase while also emphasizing the native aspects more significantly;\n"
        "6) Pollution Exp Scale uses an exponential function to show very high numbers for very polluted cities and very low numbers for unpolluted cities;\n"
        "7) Recreation Total Score: weighted average across Entertainment & Recreational Facilities, Costs, Quality of Parks and Weather.\n"
    )
    metrics_description_label = ttk.Label(centerFrame, text=metrics_description_text, wraplength=800)
    metrics_description_label.pack(pady=10)


    # Set copyright label
    copyrigth_text = (
        "Course 95888 Data Focused Python G2 Team 6 Final Project\n"
        "Kaixin Tian, Louie Sun, Yanting Hu, Zheng Zhang, Daochen Li\n"
        "-----------Copyright © 2023 CMU Heinz College-----------\n"
    )
    copyright_label = ttk.Label(centerFrame, text=copyrigth_text, wraplength=500)
    copyright_label.pack(pady=15)


def view_data_btn_on_click():
    """
    Open window displaying tabulated data
    """

    # Window
    window = Toplevel(root)
    window.title("View Data")

    # Frame
    centerFrame = Frame(window)
    centerFrame.pack(expand=True)

    # Set label
    app_label = tk.Label(centerFrame, text="View Data")
    app_label.config(font=("Arial", 20))
    app_label.pack()
    
    # Create a widget for displaying data
    text_widget = tk.Text(centerFrame, wrap=tk.WORD, width=115, height=50)
    text_widget.pack()

    #file_path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text files", "*.txt")])
    with open("./data/display/tabulated_data.txt", 'r') as file:
        content = file.read()
        text_widget.delete(1.0, tk.END)  # Clear existing content
        text_widget.insert(tk.END, content)  # Insert new content


def city_summary_btn_on_click():
    """
    Open window displaying city summary
    """
    def get_city_summary():
        cityname = entry.get()

        if cityname:
            city_info = {}
            if cityname in df['City'].values: # Check if the city is in the DataFrame
                result_label.config(text=f"{cityname}")

                city_row = df[df['City'] == cityname]

                # Populate the dict with column and value pairs of the given city
                for column in df.columns[2:]: # Start from the third column (index 2)
                    city_info[column] = city_row.iloc[0][column]
        
                city_summary = ""
                for key, value in city_info.items():
                    city_summary += (f"{key}: {value}\n")
                
                text_widget.delete(1.0, tk.END)  # Clear existing content
                text_widget.insert(tk.END, city_summary)  # Insert new content

                ## TODO: Add summary based on column stats

            else:
                text_widget.delete(1.0, tk.END)  # Clear existing content
                city_summary = "City " + cityname + " not found."
                result_label.config(text=f"{city_summary}")
    
    # Window
    window = Toplevel(root)
    window.title("City Summary")

    # Set label
    app_label = tk.Label(window, text="City Summary")
    app_label.config(font=("Arial", 20))
    app_label.pack()

    # Frame
    centerFrame = Frame(window)
    centerFrame.pack(expand=True)

    # Create label, entry and button
    label = tk.Label(centerFrame, text="Search city:")
    entry = tk.Entry(centerFrame)
    enter_button = tk.Button(centerFrame, text="Enter", command=get_city_summary)

    # Use the grid geometry manager to align components
    label.grid(row=0, column=1, sticky=tk.W)
    entry.grid(row=0, column=1)
    enter_button.grid(row=0, column=1, sticky=tk.E)

    # Create a label to display the city name entered
    result_label = tk.Label(centerFrame, text="")
    result_label.grid(row=1, column=1)
    
    # Create a widget for displaying text
    text_widget = tk.Text(centerFrame, wrap=tk.WORD, width=80, height=25)
    text_widget.grid(row=2, column=1)


def city_comparison_btn_on_click():
    """
    Open window displaying city comparison
    """
    def on_button_click(metric):
        result_label.config(text=f"Selected: {metric}, please see the new popped up window")

        # Check if the entered metric is in the DataFrame columns
        if metric in df.columns:
            # Plot the values for all cities under the selected metric
            plt.bar(df['City'], df[metric])
            plt.xlabel('City')
            plt.xticks(rotation=45, ha='right')  # Rotate the x-axis labels for better readability
            plt.ylabel(metric)
            plt.title(f'{metric} for Cities')
            plt.show()

    # Window
    window = Toplevel(root)
    window.title("City Comparison")

    # Frame
    centerFrame = Frame(window)
    centerFrame.pack(expand=True)

    # Set label
    app_label = tk.Label(centerFrame, text="City Comparison")
    app_label.config(font=("Arial", 20))
    app_label.pack()
    
    # Set ttk button style
    style = ttk.Style()
    style.theme_use("aqua")

    # Create a label to display the description
    description_label = tk.Label(centerFrame, text="")
    description = ("Based on the metric of your choice, a histogram plot of each cities' performance in the given metric will be shown")
    description_label.config(text=f"{description}")
    description_label.pack(pady=10)

    # Create buttons for each metric
    metrics = ["Income", "Employment", "Cost", "Safety", "Medical", "Pollution", "Recreation"]

    for metric in metrics:
        button = ttk.Button(centerFrame, text=metric, command=lambda m=metric: on_button_click(m), width=10)
        button.pack(side=TOP)

    # Create a label to display the selected metric
    result_label = tk.Label(centerFrame, text="")
    result_label.pack()


def city_ranking_btn_on_click():
    """
    Open window displaying ranking options
    """
    # Window
    window = Toplevel(root)
    window.title("City Ranking")

    # Frame
    centerFrame = Frame(window)
    centerFrame.pack(expand=True)

    # Set label
    app_label = tk.Label(centerFrame, text="City Ranking")
    app_label.config(font=("Arial", 20))
    app_label.pack()
    
    # label
    description = (
        "Ranking based on default weightings uses MinMaxScaler to find the significance of each metric/factor influencing relocation choices;\n"
        "Based on the significance weightings, top 15 cities are calculated and displayed.\n")
    description_label_1 = ttk.Label(centerFrame, text=description, wraplength=500)
    description_label_1.pack(pady=5)
    
    # button
    default_ranking_btn = tk.Button(centerFrame, text='Ranking based on default weightings', command=default_ranking_btn_on_click, width=40)
    default_ranking_btn.pack(pady=5)

    # label
    description2 = (
        "Ranking based on your preferences asks you to input preference of the metrics on a scale 1-7 (1 being the highest);\n"
        "NOTE: no tie is allowed in the current version, only digits 1-7 are allowed and each digit must be individually included;\n"
        "Based on the preference weightings, top 15 cities are calculated and displayed.\n")
    description_label2 = ttk.Label(centerFrame, text=description2, wraplength=500)
    description_label2.pack(pady=5)

    # button
    preference_ranking_btn = tk.Button(centerFrame, text='Ranking based on your preferences', command=preference_ranking_btn_on_click, width=40)
    preference_ranking_btn.pack(pady=5)


def default_ranking_btn_on_click():
    """
    Using MinMaxScaler, calculates the weightings of each metric/factor
    based on significance of each metric/factor influencing relocation choices;
    
    Using the significance weightings, calculate and display the top N cities
    """

    # Columns to be normalized
    metrics = ["Income", "Employment", "Cost", "Safety", "Medical", "Pollution", "Recreation"]
    
    # Intialize MinMaxScaler
    scaler = MinMaxScaler()

    # Normalizing the data
    df[metrics] = scaler.fit_transform(df[metrics])

    # Initial weights for each column
    weights = {'Income': 1 / 7, 'Employment': 1 / 7, 'Cost': 1 / 7, 'Safety': 1 / 7,
               'Medical': 1 / 7, 'Pollution': 1 / 7, 'Recreation': 1 / 7}

    # Calculate the weighted sum for each city
    df['Score'] = (df[metrics].mul(weights).sum(axis=1) * 100).round(2)

    # Selecting the features and the target variable
    target = 'Score'

    # Splitting the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df[metrics], df[target], test_size=0.2, random_state=42)
    gbm = GradientBoostingRegressor(n_estimators=150, learning_rate=0.095, max_depth=7, subsample=0.75,
                                        min_samples_leaf=1, min_samples_split=3, random_state=42)
    gbm.fit(X_train, y_train)
        
    feature_importance = gbm.feature_importances_

    importance_df = pd.DataFrame({'Feature': metrics, 'Importance': feature_importance})

    importance_df = importance_df.sort_values(by='Importance', ascending=False)  # Sorting in ascending order
        
    weights_ = weights

    for i, key in enumerate(weights_.keys()):
            weights_[key] = feature_importance[i]

    print(weights_)

    # Create new column 'Average Score'
    df['Average Score'] = (df[metrics].mul(weights_).sum(axis=1) * 100).round(2)
    top_fifteen = df.sort_values(by='Average Score', ascending=False).head(15)
    
    window = Toplevel(root)
    window.title("Default Ranking")

    # Set label
    app_label = tk.Label(window, text="Our Top Fifteen Best Cities!")
    app_label.config(font=("Arial", 20))
    app_label.pack()

    # Intialize treeview
    city_columns = ('City', 'Average Score')
    treeview = ttk.Treeview(window, columns=city_columns, show='headings')
    
    for col in city_columns:
        treeview.heading(col, text=col)
        treeview.column(col, anchor='center')

    # Insert data into the treeview
    for index, row in top_fifteen.iterrows():
        treeview.insert("", tk.END, values=(row['City'], row['Average Score']))

    treeview.pack(fill='both', expand=True)
          

def preference_ranking_btn_on_click():
    """
    Rankings of all cities based on user's preference
    """
    def validate_rank(new_value):
        """
        Validate that the input is a valid integer between 1 and 7
        """
        if new_value == "":
            return True  # Allow empty string for intermediate editing
        try:
            rank = int(new_value)
            return 1 <= rank <= 7
        except ValueError:
            return False

    def submit_ranks():    
        ranked_metrics = {metric: int(ranks[metric].get()) for metric in metrics}

        # Calculate weightings based on user rankings
        weightings = {metric: (8 - rank) for metric, rank in ranked_metrics.items()}

        # Normalize weightings to ensure they add up to 1
        total_weighting = sum(weightings.values())
        normalized_weightings = {metric: weighting / total_weighting for metric, weighting in weightings.items()}

        # Create new column 'Average Score'
        df['Average Score'] = (df[metrics].mul(normalized_weightings).sum(axis=1) * 100).round(2)
        top_fifteen = df.sort_values(by='Average Score', ascending=False).head(15)
        
        window = Toplevel(root)
        window.title("Preference Ranking")

        # Set label
        app_label = tk.Label(window, text="Our Top Fifteen Best Cities!")
        app_label.config(font=("Arial", 20))
        app_label.pack()

        # Intialize treeview
        city_columns = ('City', 'Average Score')
        treeview = ttk.Treeview(window, columns=city_columns, show='headings')
        
        for col in city_columns:
            treeview.heading(col, text=col)
            treeview.column(col, anchor='center')

        # Insert data into the Treeview
        for index, row in top_fifteen.iterrows():
            treeview.insert("", tk.END, values=(row['City'], row['Average Score']))

        # Arrange the Treeview
        treeview.pack(fill='both', expand=True)

        # Set result label text
        result_str = "\n".join([f"{metric}: {normalized_weightings[metric]:.4f}" for metric in metrics])
        result_label.config(text=f"Weightings:\n{result_str}")
        result_label.pack(pady=10)

    
    ranking_window = tk.Toplevel(root)
    ranking_window.title("Preference Ranking")

    # Set label
    app_label = tk.Label(ranking_window, text="Preference Ranking")
    app_label.config(font=("Arial", 20))
    app_label.pack()

    metrics = ["Income", "Employment", "Cost", "Safety", "Medical", "Pollution", "Recreation"]
    ranks = {metric: tk.StringVar() for metric in metrics}

    # Instruction label
    ttk.Label(ranking_window, text="Please rank the following metrics from 1 to 7 (1 being the highest priority):").pack(pady=10)

    # Create label and entry widgets for each metric
    for metric in metrics:
        metric_frame = ttk.Frame(ranking_window)
        metric_frame.pack(side=tk.TOP, pady=5)

        ttk.Label(metric_frame, text=metric, width=10).pack(side=tk.LEFT, padx=10)
        entry = ttk.Entry(metric_frame, textvariable=ranks[metric], validate='key', validatecommand=(ranking_window.register(validate_rank), '%P'), width=15)
        entry.pack(side=tk.LEFT, padx=10)

    # Submit button
    ttk.Button(ranking_window, text="Submit", command=submit_ranks).pack(pady=20)

    # Create the result label
    result_label = ttk.Label(ranking_window)


if __name__ == "__main__":
    # Create dataframe for use of the complete application
    global df
    cleaned_data_path = './data/display/cleaned_data.csv'
    df = pd.read_csv(cleaned_data_path)

    # Launch application main window
    launch()

    