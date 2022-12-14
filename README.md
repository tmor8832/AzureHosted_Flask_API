# Flask weather API hosted in Azure using Azure SQL database

This is a weather API with the data stored in azure SQL database, the user can make requests to add, update, get and remove data from the azure hosted API.

By Tom M for JHub scheme.

First I created the SQL database 'weather' to hold the data. Then I created a flask app to act as the API to communicate with the database using requests and SQL. Then after testing on localhost, deployed to Azure using the instructions which are linked in the app.py file at the appropriate points they were needed.

This was a very useful and interesting project which I enjoyed.

<h2>Creating the web app in VSCode using the azure extension</h2>

![Screenshot from 2022-10-13 18-58-48](https://user-images.githubusercontent.com/64171887/195674023-95f4841c-2b46-4435-ac30-aa87dc3fb134.png)

![Screenshot from 2022-10-13 18-58-48](https://user-images.githubusercontent.com/64171887/195672114-153c303b-973a-418f-bffa-7b74a7906040.png)

<h2>Config details for the SQL database which was created to hold the data </h2>

![Screenshot from 2022-10-13 18-59-31](https://user-images.githubusercontent.com/64171887/195672257-942ae2cc-21de-4c8a-bbf9-bc656b4e369f.png)

![Screenshot from 2022-10-13 19-00-25](https://user-images.githubusercontent.com/64171887/195672375-3779beb2-0fd7-40e3-b46d-e7521c8ae1ef.png)

<h2> App creation details on portal and also URL for the site used for the requests </h2>

![Screenshot from 2022-10-13 19-01-47](https://user-images.githubusercontent.com/64171887/195672437-5d2c5fb5-a74d-4970-9695-a8e35f13d154.png)

<h2> Testing the API through requests to that URL from a separate VSCode window, now using the cloud </h2>

![image](https://user-images.githubusercontent.com/64171887/195677327-f16d0c9a-0a88-46cd-9a6a-06b783e31e59.png)

<h2> Results of writing to, reading from and delete info in the database using the API</h2>

![image](https://user-images.githubusercontent.com/64171887/195676918-f08f1734-a498-49c1-b051-a7e94f384bba.png)

![image](https://user-images.githubusercontent.com/64171887/195677538-3d862110-2dc2-4af4-828b-788b28b57a8d.png)


<h2> App hosted in the cloud - note the URL </h2>

![image](https://user-images.githubusercontent.com/64171887/195676697-34b5c950-5b74-49a0-b879-72501df6cb51.png)

![image](https://user-images.githubusercontent.com/64171887/195677050-093afb33-6655-4672-914d-6664cb6c5e54.png)


