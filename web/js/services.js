angular.module('liveApp.services', [])
  .factory('restAPIservice', function($http) {
    var api_url = 'http://localhost/gevibepos/api/api.php';                                                                                                                                                                                                                                                                                                                                                                                                                      
    var restAPI = {};

    restAPI.appInit = function() {
        return new Promise((resolve, reject) => {
            resolve(true)
        });
    }

    restAPI.getData = function(action) {
        var classAction = '?actions='+ action;
        return new Promise((resolve, reject) => {
            $http.get(api_url + classAction).then(function(res){
                resolve(res)
            });
        })
    }

    restAPI.postData = function(action,data) {
        var classAction = '&actions='+ action;
        return new Promise((resolve, reject) => {
            $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
            $http.post(api_url + classAction,data).then(function(res){
                resolve(res)
            });
        });
    }

    return restAPI;
  });