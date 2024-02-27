angular.module('liveApp.services', [])
  .factory('FlaskApiService', function ($http){
        let url = 'http://localhost:5000/api/v1/';  // URL prefix for api
        let flaskApi = {};

        /*For Retreiving data from the api*/
        flaskApi.getData = function(endpoint){
            return new Promise(function(resolve, reject){
                $http.get(url + endpoint).then(function(response){
                    resolve(response.data)
                    // console.log(response.data)
                });
            });
        }

        /*For Creating new objects to be saved to database*/
        flaskApi.postData = function(endpoint, data){
            return new Promise(function(resolve, reject){
                $http.post(url + endpoint, data).then(function(response){
                    resolve(response.data)
                    // console.log(response.data)
                });
            });
        }

        /*For updating data*/
        flaskApi.updateData = function(endpoint, data){
            return new Promise(function(resolve, reject){
                $http.put(url + endpoint, data).then(function(response){
                    resolve(response.data)
                    // console.log(response.data)
                });
            });
        }

        /*For deleting data*/
        flaskApi.deleteData = function(endpoint, id){
            return new Promise(function(resolve, reject){
                $http.delete(url + endpoint + "/" + id).then(function(response){
                        resolve(response.data)
                        // console.log(response.data)
                });
            });
        }

        return flaskApi
  }
  ).factory('ReviewsAccess', function(FlaskApiService){
        let store = [];
        let feedbackStore = {};
        let endpoint = "reviews";

        feedbackStore.addReview = function(review){

            return new Promise(function(resolve, reject){
                FlaskApiService.postData(endpoint, angular.toJson(review)).then(function(response){
                    resolve(response)
            });
            });

        }

        feedbackStore.getReview = function(){
            return new Promise(function(resolve, reject){
                // Retrives all reviews
                FlaskApiService.getData(endpoint).then(function(response){
                    resolve(response)
            });
            });
        };  
        
        return feedbackStore;

  }

  ).factory('RegisterService', function(FlaskApiService){

    let registration = {};

    registration.registerCook = function(endpoint, data){
        return new Promise(function(resolve, reject){
            FlaskApiService.postData(endpoint, angular.toJson(data)).then(function(response){
                resolve(response);
            });
        });
    };

    registration.registerClient = function(endpoint, data){
        return new Promise(function(resolve, reject){
            FlaskApiService.postData(endpoint, angular.toJson(data)).then(function(response){
                resolve(response);
            });
        });
    };

    return registration;

  });



/*Referance code. Big thanks to @Rsgyan*/

//   .factory('restAPIservice', function($http) {
//     var api_url = 'http://localhost/gevibepos/api/api.php';                                                                                                                                                                                                                                                                                                                                                                                                                      
//     var restAPI = {};

//     restAPI.appInit = function() {
//         return new Promise((resolve, reject) => {
//             resolve(true)
//         });
//     }

//     restAPI.getData = function(action) {
//         var classAction = '?actions='+ action;
//         return new Promise((resolve, reject) => {
//             $http.get(api_url + classAction).then(function(res){
//                 resolve(res)
//             });
//         })
//     }

//     restAPI.postData = function(action,data) {
//         var classAction = '&actions='+ action;
//         return new Promise((resolve, reject) => {
//             $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
//             $http.post(api_url + classAction,data).then(function(res){
//                 resolve(res)
//             });
//         });
//     }

//     return restAPI;
//   })
