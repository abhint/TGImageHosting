# TGImageHosting

## What is about this bot ?
* This bot uploads telegram files to a third-party server.
## Usage
* Send any file or bot. Then select the third-party server you want to upload to.

## Heroku Deploy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Installation

#### 1. Clone the project repository

```sh
// With GitHub CLI
gh repo clone AbhijithNT/TGImageHosting
```
```sh
// With GitHub CLI 
$ git clone git@github.com:AbhijithNT/TGImageHosting.git
```
```sh
// With GitHub CLI
$ git clone https://github.com/AbhijithNT/TGImageHosting.git
```

#### 2. change directory

```sh
$ cd TGImageHosting
```
#### 3. Install requirements

```sh
pip3 install -r requirements.txt 
```

### Config / Secrets environment variables

Copy .env.sample to .env and add your private information

```ev
API_ID=
API_HASH=
BOT_TOKEN=
```

#### 4. Run the application
```sh
$ python -m bot
```

