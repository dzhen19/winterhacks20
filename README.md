## Installing dependencies

The basic prerequisites for running the repo are:
●	node v14 (LTS) and npm v6+
●	pipenv v2018
●	heroku CLI v7

To get everything running for the first time, you’ll need to make sure that the command line software above is properly installed on your machine. 

First, make sure that you are using Node 14.15.0. If you don’t have Node installed, you can install it from the NodeJS website. You can check your version by running: 

node -v
> 14.15.0

This should also install npm for you automatically. You can check by running:

npm -v
> 6.xx.x

Now we also need to install pipenv. Pipenv is a package manager for python packages. It’s similar to npm but for python. If you’re not using a Mac, follow the system-specific instructions for installing pipenv - this section is just added as a reference. 

The easiest way to install pipenv on Mac is to use Brew. You can install brew by following the instructions on the brew website. This is the version of brew that I’m running:

`brew -v`
> Homebrew 2.1.2
> Homebrew/homebrew-core (git revision 1b95; last commit 2019-05-15)

Now use brew to install pipenv:

`brew install pipenv`

After installing, this is the version of pipenv that I’m running on my machine:

pipenv --version
> pipenv, version 2018.11.26

You don’t necessarily have to have the same exact version for it to work properly, but I’m just listing the version I have here for completeness sake (and if something doesn’t work for you, you can try switching to the version listed here). 

Great! You should now have pipenv, node, and npm installed on your machine. Now we will use these binaries to install the dependencies to run the project. Navigate to the root directory of the interview repo:

`cd interview`

Use pipenv to install the server dependencies:

`pipenv install`

Now that we’ve installed the server dependencies, we also need to install the client side dependencies:

```
npm install
npm run build
```

You might get a number of warnings due to slightly outdated packages, but it should compile correctly in the end. Now that the dependencies are installed, we can run both servers to start our app. The first server is the flask server that handles requests. The other server is a local webpack server that makes it easy to develop within React. In the root directory, type:

npm run start

If everything works properly, your browser should automatically open and be navigated to http://localhost:3000/. If not, let us know, and we can help! You should see the basic project homepage:

 

Optional: If you are running into issues running the client and server in the same tab, you can alternatively try running the servers separately. In two separate terminal windows, you can run:

```
npm run start-client
npm run start-server
```

These are alias commands and you can see the commands that they are actually running in package.json. If you are having a specific issue, it might be helpful to run the commands in separate windows to see if there is a specific error. 

The next step is to push this website to the internet. Heroku is an awesome service with a free tier that allows you to easily push projects online. 

If you’ve never used Heroku before, visit their website and create an account. You’ll use your account credentials to push the site online. Then, install the Heroku Cli: 

`brew tap heroku/brew && brew install heroku`
`heroku login`

Now that the cli is installed, we’ll create a Heroku app and push the site online. The Heroku CLI should provide a URL that you can visit to view your site online. In my case, the URL is https://protected-beach-47576.herokuapp.com/. 

`heroku create`

Add the appropriate buildpacks (make sure to add python first, then nodejs, as follows):

`heroku buildpacks:add heroku/python`
`heroku buildpacks:add heroku/nodejs`

Now push the site to Heroku:

`git push heroku main`

Awesome, you have successfully set up the project and pushed it live to the internet!

Be sure to deploy early and often. Errors often will arise in the deployment process, but if you deploy every time you push to main, that will make your life much easier!
