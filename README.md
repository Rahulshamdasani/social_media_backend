# social_media_backend
Creating a private repo to host the Django backend

We need to do this in 3 parts

## Part 1: Github and Heroku CLI

<ol>
<li> Creating app in heroku
    <ul>
        <li> Go to heroku dashboard
        <li> Create new app
        <li> Now choose unique name and region and once u submit ur app is live
    </ul>
<br/>

<li>  Creating git repo for our project
    <ul>
        <li> Now our app is made but its inside heroku to push our data in it, we need to a git repo and link it with our heroku account
        <li> Go to your github account and create a <strong>Private</strong> repo</li>
        <li> Push all the data of your django backend in this repos root
    </ul></li>

<br/>
<li> Linking our terminal to heroku  
    <ul>
        <li> Open terminal and install the heroku CLI
        <li> For mac: <code> brew tap heroku/brew && brew install heroku</code>
        <li> For Windows : There is direct installer available at <code>https://devcenter.heroku.com/articles/heroku-cli</code>
        <li> For Ubuntu <code>sudo snap install --classic heroku</code>
        </ul>
    Now our terminal can be directly connected to heroku

<br/>
<br/>

<li> Connect to heroku
    <ul>
        <li> run command $$ <code>heroku login</code>
        <li> a prompt will open in browser, accept the promt and click login.
        <li> Now our terminal is connected to heroku
        <li> navigate this terminal to ur project folder
        <li> write command $$ <code>heroku git:remote -a YOUR_PROJECT_NAME</code>
        <li> to verify if heroku is setup correctly you should get link to heroku's git repos
        <li> If you get error then go down and check the errors I got now
    </UL>
<br/>
<li> Add build pack to heroku project.<br/>
        go to your app inside heroku and go to settings and select <code>Add Build Pack</code>
        <br/>
        for django choose the python build pack

<br/>
<br/>
<br/>
<br/>
</ol>

## Part 2: Heroku Specific Files in Project
<ol>
    <li> Make a copy of your project and work on copy
    <li> Make sure your virtual env is running properly
    <li> Once everything is good run this command
        <br/> <code>pip install gunicorn whitenoise</code>
        <br/>
        this will be used by heroku server to serve your static files and all
    <li> Now we need to setup three files which are specific to heroku
    <ul>
        <li> <strong> requirements.txt</strong>
            <ul>
            <li> This is the easiest.
            <li> Just run this command and everything will be done
            <li> <code>pip freeze > requirements.txt</code>
            <li> what this command will do is: it will make a file named requirements.txt and list our all the depencies you are using along with versions in your root directory
            </ul><br/>
        <li> runtime.txt
        <ul>
        <li> create a new text file in your root directory names <code>runtime.txt</code>
        <li> copy this content inside that file <br/>
        <code>python-3.9.7</code>
        <li> you can change the version of python based on what you are using.
        </ul><br/>
        <li> Procfile
        <ul> <li> now we need to make a Procfile which will be a process file that will tell heroku about our process
        <li> create an empty file with the name <code>Procfile</code>
        <li> this file should not have any extensions
        <li> copy this content in your proc file
        <code>web: gunicorn backendAPI.wsgi --log-file -</code>
        <li> Copy the contents exactly the same including the spaces, just change one thing.
        <li> You need to change <code>backendAPI</code> to whatever name your folder has which contains settings.py and wsgi.py
        </ul></ul>    

</ol>

## Part 3: Heroku Specific changes in <code>settings.py</code>
<ol>
    <li> Above installed apps we need to write the domains that are allowed<br/> <code>ALLOWED_HOSTS = ['koobecaf12.herokuapp.com','localhost']</code><br/>
    you will change the first field based on whatever url heroku gives you
    <li>Don't allow the debug mode<br/>
    <code> DEBUG = False</code><br/>
    there is already a variable named debug, set it to false
    <li> Above STATIC URL/ MEDIA URL write:
    <br/><code>STATIC_ROOT = os.path.join(BASE_DIR,"staticfiles")</code>
    <li> add this to ur middleware
    <br/> but add this below security
    <br/> <code>'whitenoise.middleware.WhiteNoiseMiddleware'</code>
</ol>

## Final:
### go to heroku => select app => Deploy => github => selectRepo  and deploy.
<br/>




### Backend
create virtual env : python3 -m venv <name>
activate virtual env : source name/bin/activate
pipenv install :   as it is
make migrations  : python manage.py makemigrations
migrate:          python manage.py migrate


Q and A

1: create heroku app from inside the folder

2: what to do to run it in local server.