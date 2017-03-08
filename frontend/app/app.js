/**
 * Created by nixon on 04-Mar-17.
 */
require("angular/angular");
require("angular-route/angular-route");
require("angular-resource/angular-resource");

/* Globals */
_ = require("lodash");
_urlPrefixes = {
  API: "api/",
  TEMPLATES: "static/app/"
};

/* Components */

require("./components/home/home");
require("./components/login/login");
//
/* App Dependencies */
angular.module("myApp", [
    "Home", // this is our component
    "Login",
    "ngResource",
    "ngRoute"
]);

/* Config Vars */
// @TODO in Step 13.
var routesConfig = require("./routes");

/* App Config */
angular.module("myApp").config(routesConfig);