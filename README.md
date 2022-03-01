
# the5thEstate

an  application that lists top trending news headlines across the globe, list various news sources and allows users to choose a source and views the source's top headlines.


## Authors

- [Brian Njoroge](https://github.com/Njoro410)


## Features

- View various news sources around the world
- View top trending headlines
- View top headlines per source



## Deployment-LIVE LINK

This project has been deployed to Heroku 
 - [the5thEstate](https://the5thestate.herokuapp.com/)

## Installation

To Install this project run

- Clone this to your local machine using:
- git clone https://github.com/Njoro410/the-fourth-estate.git
- Open your terminal or command prompt and run the main file.
## Tech Stack

- [Python 3.8.10](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Bootstrap V.5](https://getbootstrap.com/)


## API Reference

### Source
```
https://newsapi.org/
```
#### Get news sources

```http
  GET https://newsapi.org/v2/top-headlines/{}?apiKey={}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id`,`api_key` | `string` | **Required**. Id of item to fetch and API Key |

#### Get articles by source

```http
  GET https://newsapi.org/v2/top-headlines?sources={}&apiKey={}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`,`api_key`      | `string` | **Required**. Id of item to fetch and API Key |

#### Get top trending articles

```http
  GET https://newsapi.org/v2/top-headlines?country={}&apiKey={}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`,`api_key`      | `string` | **Required**. Id of item to fetch and API Key |




Takes two numbers and returns the sum.


## Running Tests

To run tests, run the following command

- in your terminal, run the files with test suffix in their file names.

## License

- [MIT](https://choosealicense.com/licenses/mit/)
- [Apache License 2.0](https://opensource.org/licenses/Apache-2.0)


## Feedback

If you have any feedback, please reach out to me at briannjoroge420@gmail.com

