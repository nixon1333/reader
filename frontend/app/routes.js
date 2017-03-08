function routesConfig($routeProvider) {
  $routeProvider
    .when("/", {
      templateUrl: _urlPrefixes.TEMPLATES + "components/home/home.html",
      label: "Home"
    })
    .when("/login", {
      templateUrl: _urlPrefixes.TEMPLATES + "components/login/login.html",
      label: "Login"
    })
    .otherwise({
      templateUrl: _urlPrefixes.TEMPLATES + "404.html"
    });
}

routesConfig.$inject = ["$routeProvider"];

module.exports = routesConfig;