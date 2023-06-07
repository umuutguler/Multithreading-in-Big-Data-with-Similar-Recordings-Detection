# Multithreading in Big Data with Similar Recordings Detection

This project is a Python application that aims to compare text data from a CSV file. It first reads the CSV file using the pandas library and selects the necessary columns. Then, the data is divided into different lists and distributed to two separate threads for processing using a queue. Each thread takes a text item and compares it with the other text items. The comparison calculates the similarity ratio, which is then added to a result list. The results are displayed in a window designed as a graphical user interface (GUI). The user can filter the results based on a specific similarity range and view the results in a table format. This project showcases text comparison and multithreading programming concepts.

## Dataset
https://www.kaggle.com/datasets/selener/consumer-complaint-database

## Interface
![image](https://github.com/umuutguler/Multithreading-in-Big-Data-with-Similar-Recordings-Detection/assets/74297248/864d2d08-a5db-4752-9f87-c2d50640537a)
