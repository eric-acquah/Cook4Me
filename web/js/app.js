angular.module('liveApp', [
    'liveApp.services',
    'liveApp.controllers',
    'ngRoute',
    'ngAnimate',
]).
config(['$routeProvider', function($routeProvider) {
$routeProvider.
    when("/home", {templateUrl: "partials/home.html", controller: "HomePageController"}).
    when("/services", {templateUrl: "partials/services.html", controller: "ServicesPageController"}).
    when("/login", {templateUrl: "partials/login.html", controller: "LoginPageController"}).
    when("/register", {templateUrl: "partials/register.html", controller: "RegisterPageController"}).
    when("/about", {templateUrl: "partials/about.html", controller: "AboutPageController"}).
    when("/feed", {templateUrl: "partials/feed.html", controller: "FeedPageController"}).
    when("/contact", {templateUrl: "partials/contact.html", controller: "ContactPageController"}).
    otherwise({redirectTo: '/home'});
}]).config(function($animateProvider) {
    $animateProvider.classNameFilter(/ng-hide|ng-show/);
});