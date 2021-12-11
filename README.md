## MahantapaiSudSanook

===========================================

<!-- ABOUT THE PROJECT -->
## Disaster in Thailand API
This API provides information about common natural disaster happening in Thailand. It's separated into 4 categories:

- Overall monthly natural disaster in each region of Thailand. Raw data provided by Thai Meteorological DepartMent (TMD).
- Earthquake data in Thailand between 2011 and 2021. Raw data provided by Earthquake Observation Division.
- Landslide risks area in Thailand. Raw data provided by Department of Mineral Resources (DMR).
- Rainfall and storm data gathered by our group in Google form.
### API features
1. disaster
<br><img width="618" alt="Screen Shot 2564-12-11 at 23 23 25" src="https://user-images.githubusercontent.com/55922403/145683923-7eb066f7-4d3d-43a8-8566-b386cde4c343.png">
2. earthquake
<br><img width="894" alt="Screen Shot 2564-12-11 at 23 24 09" src="https://user-images.githubusercontent.com/55922403/145683932-e348a9ed-1800-4b23-8448-a5317e927f41.png">
3. landslide
<br><img width="842" alt="Screen Shot 2564-12-11 at 23 28 23" src="https://user-images.githubusercontent.com/55922403/145684109-00d53bd7-b808-4708-8d99-2dcf6ef05e9b.png">
4. survey
<br><img width="865" alt="Screen Shot 2564-12-12 at 00 38 59" src="https://user-images.githubusercontent.com/55922403/145686221-d0905d35-6bbb-4b6e-bc6d-3965685d097c.png">
### Data visualization features
1. Earthquake count by magnitude
    > This graph provides the number of earthquake occur compare with the range of earthquake magnitude 
2. Earthquake count by the risk landslide village
    > This graph provides the number of earthquake occur compare with risk landslide village
3. Average Monthly Rainfalls
   > This graph provides average rain amount and average rain duration from survey
### Prerequisites
  1. Install [Node.js](https://nodejs.org/en/download/) (version 3.6 or higher)
  2. Install [Python](https://www.python.org/downloads/) (version 16.13.0 or higher)
  3. Create database in phpMyAdmin (MySQL)
     - Create 4 tables in your database with schema as follows:
        - disaster
                  <br><img width="628" alt="Screen Shot 2564-12-11 at 22 46 14" src="https://user-images.githubusercontent.com/55922403/145682662-327c2f53-ace3-4683-ad54-2f961206b79b.png">
        - earthquake
                  <br><img width="643" alt="Screen Shot 2564-12-11 at 22 49 52" src="https://user-images.githubusercontent.com/55922403/145682768-cfcda2f7-eaeb-4d5f-9118-d673de46e3d1.png">
        - landslide
                  <br><img width="706" alt="Screen Shot 2564-12-11 at 22 50 55" src="https://user-images.githubusercontent.com/55922403/145682790-c22a618c-3baa-463e-9577-8db3ee594ad4.png">
        - survey
                  <br><img width="701" alt="Screen Shot 2564-12-11 at 22 51 34" src="https://user-images.githubusercontent.com/55922403/145682815-06729feb-0d28-4866-b0ee-be169151665f.png">
  4. Add all disasters data from file data to database
     1. Select import
     <br><img width="845" alt="Screen Shot 2564-12-11 at 22 57 21" src="https://user-images.githubusercontent.com/55922403/145683035-d27da237-b56c-4039-bc18-53d3f8e60e23.png">
     2. Select Choose File
     <br><img width="511" alt="Screen Shot 2564-12-11 at 22 58 35" src="https://user-images.githubusercontent.com/55922403/145683078-0d65f123-4cc3-44c2-b1ac-85fc14c24fd4.png">
     3. Add one number to skip number
     <br><img width="1078" alt="Screen Shot 2564-12-11 at 22 59 29" src="https://user-images.githubusercontent.com/55922403/145683108-f5f9ee5d-ca08-464d-b0d4-81c0eb897a70.png">
     4. Select format
     <br><img width="511" alt="Screen Shot 2564-12-11 at 22 59 40" src="https://user-images.githubusercontent.com/55922403/145683115-e4ef2812-9066-4319-8013-04f1d25a7a62.png">
     5. write column name then click Go
     <br><img width="641" alt="Screen Shot 2564-12-11 at 22 59 59" src="https://user-images.githubusercontent.com/55922403/145683134-54241f72-f50f-4835-b0d0-b81283cdfa41.png">
## Instruction for virtual environment
1. Install virtual environment
   - Linux/MacOS:
      ```sh
      python3 -m pip install virtualenv
      ```
   - Windows:
      ```sh
      python -m pip install virtualenv
      ```
2. Create new virtual environment.
      ```sh
      virtualenv venv
      ```
3. Activate a virtual environment.
   - Linux/MacOS:
      ```sh
      . env/bin/activate
      ```
   - Windows:
      ```sh
      env\Scripts\activate
      ```   
## Installation
1. Clone the repo
   ```sh
   git clone https://github.com/ttxking/disaster-api.git
   ```
2. Change directory
    ```sh
   cd Disaster-API
   ```
3. Install required libraries
   ```sh
   pip install -r requirements.txt
   ```
4. Install OpenAPI-to-GraphQL
   ```sh
   npm install -g openapi-to-graphql-cli@2.5.0
   ```
5. Edit `config.py` for your phpMyAdmin database
   ```
   OPENAPI_AUTOGEN_DIR="autogen"
   DB_HOST="Your database host"
   DB_USER="Your username"
   DB_PASSWD="Your password"
   DB_NAME="Your table name"
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

## Usage
1. Run jar file 
   ```sh
   java -jar openapi-generator-cli-5.3.0.jar generate -i openapi/disaster-api.yaml -o autogen -g python-flask
   ```
3. Start the REST API server
   ```sh
   python app.py
   ```
   - swagger tool avalible on http://localhost:8080/disaster-api
4. Start openapi-to-graphql in another terminal
   ```sh
   openapi-to-graphql --cors -u http://localhost:8080/disaster-api openapi/disaster-api.yaml
   ```
   -  GraphQL window avalible on http://localhost:3000/graphql
5. Open the index page in `html\index.html`

## Interact with our database
1. Your can just download openapi-to-graphql and run with this command
   ```sh
   openapi-to-graphql --cors -u http://localhost:8080/disaster-api/ openapi/disaster-api.yaml
   ```
   - GraphQL window avalible on http://localhost:3000/graphql

But the query it quite slow, you need to wait for 15-30 second

2. Open the index page in `html\index.html`
<p align="right">(<a href="#top">back to top</a>)</p>

## Contributor 
| Student ID  | Name  | Github  | E-mail | University | Faculty| Department|  
|---|---|---|---|---|---|---|
| 6210546714  |  Anusid  Wachiracharoenwong  | [ttxking](https://github.com/ttxking)  | anusid.w@ku.th  |   Kasetsart University|Faculty of Engineering| Software and Knowledge Engineering|
| 6210545556  |  Peerasu Watanasirang    | [BellBoyZz](https://github.com/BellBoyZz)  | peerasu.w@ku.th  |   Kasetsart University|Faculty of Engineering|Software and Knowledge Engineering|
| 6210546382  |  Kittitouch Ingkasompob    | [kinkinkinxd](https://github.com/kinkinkinxd)  | kittitouch.i@ku.th  | Kasetsart University|Faculty of Engineering |Software and Knowledge Engineering|


<p align="right">(<a href="#top">back to top</a>)</p>