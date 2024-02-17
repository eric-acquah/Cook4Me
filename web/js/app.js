angular.module('liveApp', [
    'liveApp.services',
    'liveApp.controllers',
    'ngRoute'
]).
config(['$routeProvider', function($routeProvider) {
$routeProvider.
    when("/home", {templateUrl: "partials/home.html", controller: "HomePageController"}).
    when("/services", {templateUrl: "partials/services.html", controller: "ServicesPageController"}).
    when("/login", {templateUrl: "partials/login.html", controller: "LoginPageController"}).
    when("/register", {templateUrl: "partials/register.html", controller: "RegisterPageController"}).
    otherwise({redirectTo: '/home'});
}]);