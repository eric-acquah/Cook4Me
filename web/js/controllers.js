angular.module('liveApp.controllers', []).
  controller('HomePageController', function($scope, restAPIservice) {
    $scope.appName = 'Cook4Me';
    $scope.nameFilter = null;
    $scope.driversList = [];

    restAPIservice.appInit().then(function() {
        const token = sessionStorage.getItem('_token');
        if(!token){
            $scope.initApp();
        }
    })

    $scope.initApp = function(){
        var action = 'initapp';
        restAPIservice.getData(action).then(function(response) {
            if(response.data.msg === 'success'){
                const repo = response.data.data;
                sessionStorage.setItem('_token',repo.token);
                sessionStorage.setItem('_id',repo.id);
                sessionStorage.setItem('_cipher',repo.cipher);
                sessionStorage.setItem('_payment',repo.payment);
                sessionStorage.setItem('_company',repo.company);
                sessionStorage.setItem('_img_url',repo.imgurl);
            }else{
                console.log('Error loading data: ',response.data.data);
            }
        });
    }
  }).
  /* Service Controller */
  controller('ServicesPageController', function($scope, restAPIservice) {
   
  }).
  /* Login Controller */
  controller('LoginPageController', function($scope, restAPIservice) {
   
  }).
  /* Register Controller */
  controller('RegisterPageController', function($scope, restAPIservice) {
   
  }).
  /* About Controller */
  controller('AboutPageController', function($scope, restAPIservice) {
   
  }).
  /* Feed Controller */
  controller('FeedPageController', function($scope, restAPIservice) {
   
  }).
  /* Contact Controller */
  controller('ContactPageController', function($scope, restAPIservice) {
   
  });