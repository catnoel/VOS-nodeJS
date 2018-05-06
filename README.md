# VOS

To run:

```bash
node app.js
```

## Setting up node and dependencies.

VOS requires the following npm packages (as of 4-15-2018):
 - express
 - body-parser
 - jsonschema
 - fast-json-patch

We recommend that you set up a global node_packages folder.

```bash
mkdir -p `npm config get prefix`/lib/node_modules;
echo 'export NODE_PATH=`npm config get prefix`/lib/node_modules' >> ~/.bash_profile;
source ~/.bash_profile;
```

To install dependencies globally, include a `-g` flag in your call to
npm install.

```bash
npm install -g express;
npm install -g body-parser;
npm install -g jsonschema;
npm install -g fast-json-patch;
```

## A broad overview of how an express server works.

Let's trace the execution path of app.js, through express, and hopefully
over some of its service paths.

We start by invoking `node` from bash. Typing `node app.js` causes a
load of the `node` binary. `node` recognizes that its argument, `app.js`
is a javascript file in this directory. Node sets up a default set of
importable libraries, and then executes `app.js` in the context of this
set.

`app.js` is also able to import libraries vis a vis the `require`
statements. The body of app.js is treated like the `main` method of a C,
or Java, programming environment.

Reading app.js broadly, we see some early, experimental, handlers are
defined in-line. What they are shown to be useful for is setting up the
`express` server application, which is stored in `app`. These inlines
are called handlers.  Ex.

```javascript
const post_handler = (request, response) => {
    let new_profile = request.body;
    new_profile = JSON.parse(new_profile);
    // if typeof new_profile is string throw error
    if(typeof new_profile === "string") {
        throw new Error("Service does not handle raw strings.")
    }
    const identifier = request.params["identifier"];
    store[identifier] = new_profile;
    response.send(identifier);
}
```




```javascript
app.get('/json/:identifier', get_handler);
app.post('/json/:identifier', post_handler);
```