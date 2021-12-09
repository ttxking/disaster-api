## MahantapaiSudSanook

===========================================

<!-- ABOUT THE PROJECT -->
## Disaster in Thailand API
This API provides information about common natural disaster happening in Thailand. It's sperated into 4 categories:

- Overall monthly natural disaster in each region of Thailand. Raw data provided by Thai Meteorogical DepartMent (TMD).
- Earthquake data in Thailand between 2011 and 2021. Raw data provided by Eathquake Observation Division.
- Landslide risks area in Thailand. Raw data provided by Departmet of Mineral Resources (DMR).
- Rainfall and storm data gathered by our group in Google form.

### Prerequisites
  1. Install [Node.js](https://nodejs.org/en/download/)
  2. Install [Python](https://www.python.org/downloads/)
  

## Installation
1. Clone the repo
   ```sh
   git clone https://github.com/nuttapol-kor/fast-and-foo.git
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
5. Edit `example.env` for your credential
   ```
   OPENAPI_AUTOGEN_DIR="autogen"
   DB_HOST="Your database host"
   DB_USER="Your username"
   DB_PASSWD="Your password"
   DB_NAME="Your table name"
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

## Usage
1. Start the REST API server
   ```sh
   python app.py
   ```
   - swagger tool avalible on http://localhost:8080/disaster-api
2. Start openapi-to-graphql in another terminal
   ```sh
   openapi-to-graphql --cors -u http://localhost:8080/disaster-api openapi/disaster-api.yaml
   ```
   -  GraphQL window avalible on http://localhost:3000/graphql
3. Open the index page in `html\index.html`

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

| Student ID  | Name  | Github  | E-mail |   
|---|---|---|---|
| 6210546714  |  Anusid  Wachiracharoenwong  | [ttxking](https://github.com/ttxking)  | anusid.w@ku.th  |   
| 6210545556  |  Peerasu Watanasirang    | [BellBoyZz](https://github.com/BellBoyZz)  | peerasu.w@ku.th  |   
| 6210546382  |  Kittitouch Ingkasompob    | [kinkinkinxd](https://github.com/kinkinkinxd)  | kittitouch.i@ku.th  |   


<p align="right">(<a href="#top">back to top</a>)</p>