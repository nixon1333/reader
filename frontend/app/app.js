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

/* App Dependencies */
angular.module("myApp", [
  "ngResource",
  "ngRoute",
]);

/* Config Vars */
// @TODO in Step 13.

/* App Config */
angular.module("myApp").config(routesConfig);